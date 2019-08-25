from flask import Flask, redirect, url_for, request, render_template
from tensorflow.python.keras.applications import ResNet50
from PIL import Image
import numpy as np

app = Flask(__name__, template_folder='templates')

MODEL_PATH = 'models/your_model.h5'
model = ResNet50(weights='imagenet')
file_path = 'uploads'


@app.route('/')
def index():
	return render_template('index.html')

def model_predict(img_path, model):
	img = Image.open(img_path)
	x = np.array(img)
	preds = model.predict(x)
	return preds

@app.route('/predict')
def upload():
	if request.method == 'POST':
		f = request.files['file']
		f.save(file_path)
		preds = model_predict(file__path, model)
		pred_class = decode_predictions(preds, top=1)
		return pred_class