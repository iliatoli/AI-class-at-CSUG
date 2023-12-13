"""
Created on Wed Nov 29 22:05:19 2023

@author: iliat
"""

import numpy as np

# Activation function (sigmoid)
def sigmoid(x):
    return 1 / (1 + np.exp(-x))

# Derivative of the sigmoid function
def sigmoid_derivative(x):
    return x * (1 - x)

# Function to train the neural network
def train_neural_network(X, y, iterations):
    input_size = X.shape[1]
    hidden_size = 4  # Number of neurons in the hidden layer
    output_size = 1

    # Initialize weights and biases for the layers
    weights_input_hidden = np.random.rand(input_size, hidden_size)
    biases_input_hidden = np.random.rand(1, hidden_size)
    weights_hidden_output = np.random.rand(hidden_size, output_size)
    biases_hidden_output = np.random.rand(1, output_size)

    learning_rate = 0.1

    for i in range(iterations):
        # Feedforward
        hidden_layer_input = np.dot(X, weights_input_hidden) + biases_input_hidden
        hidden_layer_output = sigmoid(hidden_layer_input)
        output_layer_input = np.dot(hidden_layer_output, weights_hidden_output) + biases_hidden_output
        predicted_output = sigmoid(output_layer_input)

        # Calculate error
        error = y - predicted_output

        # Backpropagation
        d_predicted_output = error * sigmoid_derivative(predicted_output)
        error_hidden_layer = d_predicted_output.dot(weights_hidden_output.T)
        d_hidden_layer = error_hidden_layer * sigmoid_derivative(hidden_layer_output)

        # Update weights and biases using gradient descent
        weights_hidden_output += hidden_layer_output.T.dot(d_predicted_output) * learning_rate
        biases_hidden_output += np.sum(d_predicted_output, axis=0, keepdims=True) * learning_rate
        weights_input_hidden += X.T.dot(d_hidden_layer) * learning_rate
        biases_input_hidden += np.sum(d_hidden_layer, axis=0, keepdims=True) * learning_rate

    return predicted_output

# Sample input and output (modify as needed)
X = np.array([[0, 1], [1, 0], [1, 1], [0, 0]])  # Input
y = np.array([[1], [1], [0], [0]])  # Output

# Train the neural network
iterations = 1000
predicted_output = train_neural_network(X, y, iterations)

print("Predicted output after training:")
print(predicted_output)
