import keras

model = keras.models.load_model("models/trained_model.keras")

model.export("models/trained_model_tf")
