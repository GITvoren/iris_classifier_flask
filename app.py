from flask import Flask, request, jsonify
import iris_model
from flask_cors import CORS

app = Flask(__name__)

CORS(app)

@app.route('/', methods=['GET'])
def api_ready():
    return jsonify("API Ready")

@app.route('/predict', methods=['POST'])
def predict_specie():
     sepal_length = request.json['sepallength']
     sepal_width = request.json['sepalwidth']
     petal_length = request.json['petallength']
     petal_width = request.json['petalwidth']
     y_pred = [[sepal_length, sepal_width, petal_length, petal_width]]
     trained_model = iris_model.training_model()
     prediction_value = trained_model.predict(y_pred)

     if prediction_value == 0:
         return jsonify("Setosa")
     elif prediction_value == 1:
         return jsonify("Versicolor")
     else:
         return jsonify("Virginica")


if __name__ == '__main__':
     app.run(debug=False)
 