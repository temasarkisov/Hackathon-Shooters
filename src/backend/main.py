import numpy as np
import tensorflow as tf
from tensorflow import keras

from keras.models import Sequential
from keras.layers import Dense, Dropout, Activation
from keras.models import load_model

import librosa

import pandas as pd

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
    mfccs_processed_np = np.array(mfccs_processed.tolist())
    print(mfccs_processed_np.shape, type(mfccs_processed_np))
    #result = model.predict(mfccs_processed_np)
    return mfccs_processed


def get_result():
    file_name = '99710-9-0-5.wav'  # Сделать нормально, по пути, а не по имени файла
    features = extract_features(file_name)
    #featuresdf = pd.DataFrame(features, columns=['feature'])
    #data = np.array(featuresdf.feature.tolist())
    #print(featuresdf)

    #test = load_audio(file_name)
    #result = model.predict(test)
    #return result


#model = create_model()
#model.load_weights("../training/model_model.h5")
model = load_model("../training/model_model.h5")
get_result()
