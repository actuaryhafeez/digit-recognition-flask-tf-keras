# digit-recognition-flask-tf-keras
The digit recognition project using TensorFlow, Keras, and Flask aims to build a web application that allows users to draw a digit on a canvas and get a prediction of the digit using a Convolutional Neural Network (CNN) model.

The project involves building a CNN model to classify hand-drawn digits, training it on the MNIST dataset, and then integrating it into a Flask web application. The user can draw a digit on a canvas and submit it to the Flask backend for prediction. The backend will preprocess the image, pass it through the CNN model, and return the predicted digit to the user.

# Installation
## To install and run this application, follow these steps:

### Clone the repository to your local machine.
    https://github.com/actuaryhafeez/handwritten-digits-classification.git
### Create a new virtual environment in the project directory.
    python3 -m venv venv
### Activate the virtual environment. 
    source venv/bin/activate
### Jupyter Notebook has also been installed in the virtual environment. Install the necessary dependencies by running the command
    pip install -r requirements.txt.
### Run Jupyter Notebook using the following command to open notebook.ipynb
    jupyter notebook
### Start the Flask server by running the command python app.py in the terminal.
    flask run
### Open a web browser and navigate to http://localhost:5000 to access the home page of the application.
### Upload digit image from data directory and click "Predict" to see the predicted species.

## Project Structure 

    Digits Recognition App/
        ├── data/
        │   
        ├── model/
        │   └── digit_model.h5
        ├── static/
        │   └── image.png
        └── templates/
        |   └── home.html
        ├── app.py/
        │  
        ├── notebook.ipynb/
        ├── requirements.txt/
        ├── README.md/

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

This project adheres to the [Open Source Initiative's](https://opensource.org) definition of open source software and the [Open Source Initiative's Approved License List](https://opensource.org/licenses/alphabetical).

