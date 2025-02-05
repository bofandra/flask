from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({'message': 'Hello, World! This is a Flask API.'})

@app.route('/status')
def status():
    return jsonify({'status': 'running'})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({'message': 'Hello, World! This is a Flask API.'})

@app.route('/status')
def status():
    return jsonify({'status': 'running'})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
