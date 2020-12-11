import numpy as np
import tensorflow as tf
from tensorflow import keras

from keras.models import Sequential
from keras.layers import Dense, Dropout, Activation
from keras.models import load_model

import librosa

import pandas as pd

import os

from scipy.io import wavfile as wav

import matplotlib.pyplot as plt

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
    # Extract features
    audio, sample_rate = librosa.load(file_name, res_type='kaiser_fast')
    mfccs = librosa.feature.mfcc(y=audio, sr=sample_rate, n_mfcc=40)
    mfccs_processed = np.mean(mfccs.T, axis=0)

    # Load image
    scipy_sample_rate, scipy_audio = wav.read(file_name)
    plt.figure(figsize=(12, 4))
    plt.plot(scipy_audio)
    plt.savefig(PATH_TO_MEDIA + '/audio.png')

    return mfccs_processed


def get_result(file_name):
    # Get path
    path_to_file = PATH_TO_MEDIA + '/' + file_name

    # Load data
    data = extract_features(path_to_file)
    features = []
    features.append([data, 'none'])
    featuresdf = pd.DataFrame(features, columns=['feature', 'class_label'])
    data_to_predict = np.array(featuresdf.feature.tolist())

    # Load model
    model = load_model("src/training/model_model.h5")
    model.compile(loss='categorical_crossentropy', metrics=['accuracy'], optimizer='adam')
    model.summary()

    # Loading data to model and predict
    weights_array = []
    result_weights = model.predict(data_to_predict)
    for weight in result_weights[0]:
        weights_array.append(weight)
    result = weights_array.index(max(weights_array))
    print(result)
    print(result_weights)
    return result


# model = create_model()
# model.load_weights("../training/model_model.h5")
# result = get_result()