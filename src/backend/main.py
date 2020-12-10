import numpy as np
import tensorflow as tf
from tensorflow import keras

from keras.models import Sequential
from keras.layers import Dense, Dropout, Activation


def build_model_graph(input_shape=(40,)):
    #num_labels = ...
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

#model = keras.models.load_model("../training/model/shooters_model.h5")
model = build_model_graph()
model.load_weights("../training/model/shooters_model.h5")

model.predict('test_input')


