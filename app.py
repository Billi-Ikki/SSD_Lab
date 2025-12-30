from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({"message": "Hello World", "status": "running"})

@app.route('/health')
def health():
    return jsonify({"status": "healthy"}), 200

def add(a, b):
    return a + b

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)