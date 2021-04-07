import os
import cv2
from keras.models import load_model
import numpy as np


seq_len = 75
classes = ["Fight", "NonFight"]
img_height, img_width = 64, 64
known_Y = True

def frames_extraction(video_path):
    frames_list = []

    vidObj = cv2.VideoCapture(video_path)
    # Used as counter variable
    count = 1

    while count <= seq_len:

        success, image = vidObj.read()
        if success:
            image = cv2.resize(image, (img_height, img_width))
            frames_list.append(image)
            count += 1
        else:
            print("Defected frame")
            break

    return frames_list


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

                if len(frames) == seq_len:
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
            if len(frames) == seq_len:
                X.append(frames)

    X = np.asarray(X)
    if not known_Y:
        return X, files_list
    else:
        Y = np.asarray(Y)
        return X, Y

# returns a compiled model
# identical to the previous one
model = load_model('RNN_Project.h5')


# For the undecidable videos of the Mother code
data_dir = "video_data_test/"
X_unknown, files_list = create_data(data_dir, False)
y_pred_unknown = model.predict(X_unknown)
y_pred_unknown = np.argmax(y_pred_unknown, axis=1)
for i in range(len(files_list)):
    print("X=%s, Predicted=%s" % (files_list[i], y_pred_unknown[i]))
