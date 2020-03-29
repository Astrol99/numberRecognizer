import tensorflow as tf
from tensorflow import keras
import numpy as np

print(f"[*] GPUs Available: {len(tf.config.experimental.list_physical_devices('GPU'))}")

MNIST = keras.datasets.mnist

(train_images, train_labels), (test_images, test_labels) = MNIST.load_data()

train_images = train_images / 255.0
test_images  = test_images  / 255.0

model = keras.Sequential([
    keras.layers.Flatten(input_shape=(28,28)),
    keras.layers.Dense(128, activation='relu'),
    keras.layers.Dense(10)
])

model.compile(optimizer='adam', loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True), metrics=['accuracy'])

model.fit(train_images, train_labels, epochs=50)

# Eval Accuracy
test_loss, test_acc = model.evaluate(test_images, test_labels, verbose=2)
print(f"[*] Test Accuracy: {test_acc} Test Loss: {test_loss}")

# Convert layer from logits to probabilities
probability_model = tf.keras.Sequential([model, keras.layers.Softmax()])

# Save model
probability_model.save("MNIST.h5")
print("[+] Saved model as: MNIST.h5")
