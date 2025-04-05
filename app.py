from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/api/v1.0/predict', methods=['POST'])
def predict():
    data = request.get_json() or {}

    # Pobierz liczby, wstaw 0 jeśli brak
    x1 = float(data.get('x1', 0))
    x2 = float(data.get('x2', 0))

    # Reguła decyzyjna
    prediction = 1 if (x1 + x2) > 5.8 else 0

    response = {
        "prediction": prediction,
        "features": {"x1": x1, "x2": x2}
    }
    return jsonify(response)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)