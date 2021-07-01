from config import GENERATED_DATA_PATH, MODEL_PATH
from formation_indus_ds_avancee.feature_engineering import prepare_features
from formation_indus_ds_avancee.train_and_predict import predict
from config import MODEL_PATH
from flask import Flask, jsonify, request
import pandas as pd


app = Flask(__name__)


@app.route('/health')
def health():
    return jsonify({
        "status": "ok"
    })


@app.route('/predict')
def predict_endpoint():
    raise NotImplementedError
