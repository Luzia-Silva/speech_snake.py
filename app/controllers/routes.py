import json
from flask import Flask, jsonify
from flask import Flask, send_file, render_template, request, flash
import base64
from io import BytesIO
import matplotlib.pyplot as plt
import seaborn as sns
import os
from werkzeug.utils import secure_filename

from app import app
import json
import librosa

from app.static.data.metricsTheAudios import metricsTheAudios
from app.static.data.analyzes import analyzes
from app.models.graphics import Spectrogram, Waveshow


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/audioupload")
def audioupload():
    return render_template("audioupload.html")


@app.route("/analyzes", methods=["POST", "GET"])
def upload():
    UPLOAD_FOLDER = os.path.join(os.getcwd() + "\\app\\static\\upload") #temporario
    if request.method == "POST":
        file = request.files['audio']
        if file.filename == '':
            flash('Por favor, faça o upload de um áudio')
            return render_template("audioupload.html")
        else:
            savePath = os.path.join(
                UPLOAD_FOLDER, secure_filename(file.filename))
            file.save(savePath)
            analyzesJson = analyzes(
                spectrogram=Spectrogram(audio_file=savePath).spectrogramImage(), waveshow=Waveshow(audio_file=savePath).waveshowImage())
            return render_template("analyzes.html", dados=analyzesJson)
    else:
        return render_template("audioupload.html")


@app.route('/metrics')
def metrics():
    unpackingJsonFunction = json.dumps(metricsTheAudios)
    dados = json.loads(unpackingJsonFunction)
    return render_template("metrics.html", dados=dados)
