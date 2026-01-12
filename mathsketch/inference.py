import onnxruntime as ort
import numpy as np
import io
from PIL import Image
from pathlib import Path

session = ort.InferenceSession('models/trained_model.onnx', providers=['CPUExecutionProvider'])

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

    # Save for viewing and debugging
    save_path = Path('digit-preview/drawn_image.png')
    save_path.parent.mkdir(parents=True, exist_ok=True)
    Image.fromarray(img_array[0][0]).save(save_path)

    img_array = img_array / 255.0
    img_array = img_array.astype(np.float32)
    return img_array

def predict_digit(image_bytes: bytes) -> int:
    img_array = preprocess_image_bytes(image_bytes)

    outputs = session.run(None, {'input_layer': img_array})
    
    # Take index of max and return.
    index_of_highest_probability = np.argmax(outputs[0])
    # Convert from NumPy int (intp) to regular int.
    return int(index_of_highest_probability)
