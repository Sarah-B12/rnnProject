import keras
from keras import applications
from keras.preprocessing.image import ImageDataGenerator
from keras import optimizers
from keras.models import Sequential, Model
from keras.layers import *
from keras.callbacks import ModelCheckpoint, LearningRateScheduler, TensorBoard, EarlyStopping
from keras.models import load_model

import os
import cv2
import numpy as np
from sklearn.model_selection import train_test_split
from dynamicImage import get_dynamic_image

from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
from sklearn.metrics import precision_score
from sklearn.metrics import recall_score
from sklearn.metrics import f1_score
from sklearn.metrics import cohen_kappa_score
from sklearn.metrics import roc_auc_score
from sklearn.metrics import multilabel_confusion_matrix

data_dir = "video_data_test/"
seq_len = 150
classes = ["Fight", "NonFight"]
img_height, img_width = 256, 256
known_Y = True
# known_Y = True if test or train

#  Creating frames from videos

def frames_extraction(video_path):
    frames_list = []
    dyn_image_list = []

    vidObj = cv2.VideoCapture(video_path)
    # Used as counter variable
    count = 1

    while count <= seq_len:

        success, image = vidObj.read()
        if success and (count % 2) == 0:
            image = cv2.resize(image, (img_height, img_width))
            frames_list.append(image)
            count += 1
        elif (count % 2) != 0:
            count += 1
        else:
            print("Defected frame")
            break
        if (count % 10) == 0:
            dyn_image = get_dynamic_image(frames_list, normalized=True)
            # cv2.imwrite("a.jpg", dyn_image)
            dyn_image_list.append(dyn_image)
            frames_list.clear()

    return dyn_image_list


def create_data(input_dir, known_Y):
    X = []
    if known_Y:
        Y = []

    if known_Y:
        classes_list = os.listdir(input_dir)
        exists1 = ".DS_Store" in classes_list
        if exists1:
            classes_list.remove(".DS_Store")
        for c in classes_list:
            print(c)
            files_list = os.listdir(os.path.join(input_dir, c))
            exists2 = ".DS_Store" in files_list
            if exists2:
                files_list.remove(".DS_Store")
            for f in files_list:
                frames = frames_extraction(os.path.join(os.path.join(input_dir, c), f))

                '''
                for ff in frames:
                    cv2.imwrite("frame%d.jpg" % counter, ff)
                    counter += 1
                '''

                if len(frames) == seq_len/10:
                    X.append(frames)
                    y = [0] * len(classes)
                    y[classes.index(c)] = 1
                    Y.append(y)
    else:
        files_list = os.listdir(input_dir)
        exists2 = ".DS_Store" in files_list
        if exists2:
            files_list.remove(".DS_Store")
        for f in files_list:
            frames = frames_extraction(os.path.join(input_dir, f))
            if len(frames) == seq_len / 10:
                X.append(frames)

    X = np.asarray(X)
    if not known_Y:
        return X, files_list
    else:
        Y = np.asarray(Y)
        return X, Y


X, Y = create_data(data_dir, known_Y)

X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.20, shuffle=True, random_state=0)

model = Sequential()
model.add(ConvLSTM2D(filters=64, kernel_size=(3, 3), return_sequences=False, data_format="channels_last",
                     input_shape=(int(seq_len/10), img_height, img_width, 3)))
model.add(Dropout(0.2))
model.add(Flatten())
model.add(Dense(512, activation="relu"))
model.add(Dropout(0.3))
model.add(Dense(512, activation="relu"))
model.add(Dropout(0.3))
model.add(Dense(2, activation="sigmoid"))

model.summary()

opt = keras.optimizers.SGD(lr=0.001)
model.compile(loss='binary_crossentropy', optimizer=opt, metrics=["accuracy"])

earlystop = EarlyStopping(monitor='val_loss', mode='min', patience=7)
callbacks = [earlystop]


history = model.fit(x=X_train, y=y_train, epochs=80, batch_size=8, shuffle=True, validation_split=0.2, callbacks=callbacks)


y_pred = model.predict(X_test)
y_pred = np.argmax(y_pred, axis=1)
y_test = np.argmax(y_test, axis=1)

print(classification_report(y_test, y_pred))
print(confusion_matrix(y_test, y_pred))


model.save('RNN_Project.h5')  # creates a HDF5 file
