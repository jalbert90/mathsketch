import keras

model = keras.models.load_model("mathsketch/trained_model.keras")

model.export("trained_model_tf")
