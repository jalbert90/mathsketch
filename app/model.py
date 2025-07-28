from keras.models import load_model
import numpy as np
import io
from PIL import Image
import PIL

model = load_model('app/trained_model.keras')

def preprocess_image_bytes(image_bytes: bytes) -> np.ndarray:
    # Wrap the sequence of bytes (image_bytes) with a container that exposes read, write, seek, etc., file operations.
    image_stream = io.BytesIO(image_bytes)

    image = Image.open(image_stream)