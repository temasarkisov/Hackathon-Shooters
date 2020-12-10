import numpy as np
import tensorflow as tf
from tensorflow import keras

from keras.models import Sequential
from keras.layers import Dense, Dropout, Activation
from keras.models import load_model


def create_model(input_shape=(40,)):
    num_labels = 10
    model = Sequential()
    model.add(Dense(256))
    model.add(Activation('relu'))
    model.add(Dropout(0.5))
    model.add(Dense(256))
    model.add(Activation('relu'))
    model.add(Dropout(0.5))
    model.add(Dense(num_labels))
    model.add(Activation('softmax'))
    model.compile(loss='categorical_crossentropy', metrics=['accuracy'], optimizer='adam')
    return model


def extract_features(file_name):
  audio, sample_rate = librosa.load(file_name, res_type='kaiser_fast') 
  mfccs = librosa.feature.mfcc(y=audio, sr=sample_rate, n_mfcc=40)
  mfccs_processed = np.mean(mfccs.T,axis=0)
     
  return mfccs_processed


def get_result():
    file_name = '99710-9-0-5.wav'  # Сделать нормально, по пути, а не по имени файла
    data = extract_features(file_name)
    print(data)

    return data


model = load_model("../training/model/shooters_model.h5")
data = get_result()
model.predict(data)


