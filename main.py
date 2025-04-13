from flask import Flask, request, jsonify
import random

app = Flask(_name_)

@app.route('/')
def home():
    return "Fridge AI is running!"

@app.route('/upload-image', methods=['POST'])
def handle_image():
    file = request.files['file']
    result = random.choice(["ارور F1", "ارور E2", "ارور dF"])
    return jsonify({"نوع ارور": result})

@app.route('/upload-audio', methods=['POST'])
def handle_audio():
    file = request.files['file']
    result = random.choice(["فن سالم است", "مشکل در بلبرینگ فن", "فن صدا غیرعادی دارد"])
    return jsonify({"نتیجه بررسی فن": result})

if _name_ == '_main_':
    app.run()
