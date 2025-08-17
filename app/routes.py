from flask import Blueprint, render_template, request, jsonify
from .models.wine_predictor import WinePredictor
import joblib

main = Blueprint('main', __name__)
predictor = WinePredictor()

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.form
        wine_type = data['wine_type']
        features = [
            float(data['fixed_acidity']),
            float(data['volatile_acidity']),
            float(data['citric_acid']),
            float(data['residual_sugar']),
            float(data['chlorides']),
            float(data['free_sulfur_dioxide']),
            float(data['total_sulfur_dioxide']),
            float(data['density']),
            float(data['pH']),
            float(data['sulphates']),
            float(data['alcohol'])
        ]
        prediction = predictor.predict(wine_type, features)
        quality_label = predictor.interpret_quality(prediction)
        return render_template('prediction.html', prediction=prediction, quality_label=quality_label, wine_type=wine_type)
    except Exception as e:
        return jsonify({'error': str(e)}), 400
