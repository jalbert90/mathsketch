from keras.datasets import mnist
from keras.utils import to_categorical
from keras import Sequential
from keras.layers import Flatten, Dense, ReLU, Softmax

(x_train, y_train), _ = mnist.load_data()
x_train = x_train / 255.0
y_train = to_categorical(y_train, num_classes=10)

model = Sequential(
    Flatten((28, 28)),
    Dense(128, activation="reLU")
)