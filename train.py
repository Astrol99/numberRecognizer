import tensorflow as tf
from tensorflow import keras
import numpy as np
import matplotlib.pyplot as plt

MNIST = keras.datasets.mnist

(train_images, train_labels), (test_images, test_labels) = MNIST.load_data()