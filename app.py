from flask import Flask, request
import requests

app = Flask(__name__)

@app.route('/')
def home():
    return "Server is running!"

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.json
    print(data)
    return "ok"

app.run(host="0.0.0.0", port=10000)
