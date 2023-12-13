# -*- coding: utf-8 -*-
"""
Created on Sun Dec  3 14:51:05 2023

@author: iliat
"""

import tensorflow as tf
import numpy as np

# Generating some dummy data
np.random.seed(42)
X = np.random.rand(100, 1)
y = 3 * X + 2 + np.random.randn(100, 1) * 0.1  # y = 3X + 2 + noise

# Creating the model architecture
model = tf.keras.Sequential([
    tf.keras.layers.Dense(units=1, input_shape=[1]),  # Input layer with one neuron
])

# Defining the loss function and optimizer
loss_fn = tf.keras.losses.mean_squared_error
optimizer = tf.keras.optimizers.SGD(learning_rate=0.01)

# Compiling the model
model.compile(optimizer=optimizer, loss=loss_fn)

# Training the model
model.fit(X, y, epochs=100)

# Predicting using the trained model
predictions = model.predict(X)

# Printing the predicted values
print(predictions)
