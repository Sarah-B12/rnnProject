from keras.models import load_model
from rnn import create_data
import numpy as np




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
