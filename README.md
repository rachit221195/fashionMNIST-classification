# fashionMNIST-classification

This repository contains my learnings related to using PyTorch for building a basic Deep Learning Model.

The first file is `handwritten_digit_classification.ipynb` which contains a very basic neural network to identify handwritten digits. This notebook is pretty rough and contains how a model evolves and shapes of different variables here and there

The second file is `fashion-MNIST-classification.ipynb` which contains a neural network to identify images of fashion items like shoes, sneaker, jackets, trousers, shirts, etc.
The methodology used in this notebook is more sophisticated. The structure of neural network contains a dropout layer for regularization. The model is evaluated at each epoch for both training and validation error. This helps in understanding how the error evolves.

The end of the notebook contains an inference sample.

Since the model is very basic, with Linear Leayers and ReLU activations the accuracy achieved by the model is close of 90% only! This can be improved by making the model more complicated.