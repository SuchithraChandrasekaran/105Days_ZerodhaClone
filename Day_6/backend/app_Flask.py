from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return "Zerodha Clone Backend is Running!"

@app.route('/api/recommendations', methods=['GET'])
def get_recommendations():
    # Example response
    return jsonify({
        "recommendations": [
            {"stock": "INFY", "confidence": 0.92},
            {"stock": "MPHASIS", "confidence": 0.89}
        ]
    })

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)

