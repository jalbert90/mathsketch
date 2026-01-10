from keras.models import load_model
import numpy as np
import io
from PIL import Image

model = load_model('models/trained_model.keras')

def preprocess_image_bytes(image_bytes: bytes) -> np.ndarray:
    # Wrap the sequence of bytes (image_bytes) with a container that exposes read, write, seek, etc., file operations.
    img_stream = io.BytesIO(image_bytes)

    # Create image object from file-like object.
    # Pillow is able to parse the stream to make a grid of pixels by looking at the header of the stream.
    img = Image.open(img_stream)
    
    img = img.resize((28, 28))

    # Make image grayscale (L = luminance)
    img = img.convert("L")

    img_array = np.array(img)

    # Reshape so that model receives the shape it expects.
    img_array = np.reshape(img_array, (1, 28, 28))

    Image.fromarray(img_array[0]).save('digit-preview/drawn_image.png')

    img_array = img_array / 255.0

    return img_array

def predict_digit(image_bytes: bytes) -> int:
    img_array = preprocess_image_bytes(image_bytes)
    probability_array = model.predict(img_array)
    
    # Take index of max and return.
    index_of_highest_probability = np.argmax(probability_array)
    # Convert from NumPy int (intp) to regular int.
    index_of_highest_probability = int(index_of_highest_probability)
    return index_of_highest_probability
