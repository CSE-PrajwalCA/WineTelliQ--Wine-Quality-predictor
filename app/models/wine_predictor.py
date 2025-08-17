import joblib
import os

class WinePredictor:
    def __init__(self):
        self.red_model = None
        self.white_model = None
        self.load_models()

    def load_models(self):
        try:
            self.red_model = joblib.load(os.path.join(os.path.dirname(__file__), 'saved_models/red_wine_model.joblib'))
            self.white_model = joblib.load(os.path.join(os.path.dirname(__file__), 'saved_models/white_wine_model.joblib'))
        except FileNotFoundError:
            raise FileNotFoundError("Model files not found. Please run train_models.py first.")

    def predict(self, wine_type, features):
        model = self.red_model if wine_type.lower() == 'red' else self.white_model
        prediction = model.predict([features])[0]
        return round(prediction, 2)

    def interpret_quality(self, prediction):
        if prediction >= 7:
            return "Excellent"
        elif prediction >= 5:
            return "Good"
        else:
            return "Poor"
