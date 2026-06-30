from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({"status": "healthy", "message": "Welcome to Flask on GitHub Actions!"})

@app.route('/multiply/<int:x>/<int:y>')
def multiply(x, y):
    return jsonify({"result": x * y})

if __name__ == '__main__':
    app.run(debug=True)
