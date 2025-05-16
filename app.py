from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def hello():
    return f"Hola desde Cloud Run! 🚀 (versión: {os.getenv('VERSION', '1.0')})"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)