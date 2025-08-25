from keras.datasets import mnist
from keras.utils import to_categorical
from keras import Sequential, layers

(x_train, y_train), _ = mnist.load_data()
x_train = x_train / 255.0
y_train = to_categorical(y_train, num_classes=10)

model = Sequential([
    layers.Input(shape=(28, 28)),
    layers.Flatten(),
    layers.Dense(128, activation='relu'),
    layers.Dense(10, activation='softmax')
])

model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])
model.fit(x_train, y_train, epochs=5, validation_split=0.2)
model.save('mathsketch/trained_model.keras')