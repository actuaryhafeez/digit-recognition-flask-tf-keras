import tensorflow as tf
from tensorflow import keras
from flask import Flask, render_template, request, jsonify
import numpy as np
import base64
from PIL import Image

app = Flask(__name__)

# Load the model
model = keras.models.load_model('model/digit_model.h5')


@app.route('/predict', methods=['POST'])
def predict():
    img_data = request.get_json()['data'].split(',')[1]
    with open("image.png", "wb") as f:
        f.write(base64.b64decode(img_data))
    img = Image.open("image.png")
    img = img.convert('L')  # Convert to grayscale
    img = img.resize((28, 28))  # Resize to (28, 28)
    img_array = np.array(img)
    img_array = img_array.astype('float32') / 255.0
    img_array = img_array.reshape(1, 28, 28, 1)  # Reshape to (1, 28, 28, 1)
    prediction = model.predict(img_array)
    result = {'digit': str(np.argmax(prediction))}
    return jsonify(result)

# Render the home page
@app.route('/')
def home():
    return render_template('home.html')


if __name__ == '__main__':
    app.run(debug=True)
