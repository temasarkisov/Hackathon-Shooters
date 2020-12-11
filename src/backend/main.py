import numpy as np
import tensorflow as tf
from tensorflow import keras

from keras.models import Sequential
from keras.layers import Dense, Dropout, Activation
from keras.models import load_model

import librosa

import pandas as pd

import os


PACKAGE_PARENT = '../../media'
SCRIPT_DIR = os.path.dirname(os.path.realpath(os.path.join(os.getcwd(), os.path.expanduser(__file__))))
PATH_TO_MEDIA = os.path.normpath(os.path.join(SCRIPT_DIR, PACKAGE_PARENT))


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
    print(mfccs_processed_np)
    #print(mfccs_processed_np.shape, type(mfccs_processed_np))
    return mfccs_processed_np


def get_result():
    # model = load_model("../training/model_model.h5")
    model = load_model("src/training/model_model.h5")

    only_files = [f for f in os.listdir(PATH_TO_MEDIA) if os.path.isfile(os.path.join(PATH_TO_MEDIA, f))]
    file_name = only_files[0]
    path_to_file = PATH_TO_MEDIA + '/' + file_name
    mfccs_processed_np = extract_features(path_to_file)
    #result = model.predict(mfccs_processed_np)
    result = 1
    return result


#model = create_model()
#model.load_weights("../training/model_model.h5")
#result = get_result()
