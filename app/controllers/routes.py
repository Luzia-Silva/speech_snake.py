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


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/audioupload")
def audioupload():
    return render_template("audioupload.html")


@app.route("/analyzes", methods=["POST", "GET"])
def upload():
    UPLOAD_FOLDER = os.path.join(
        os.getcwd() + "\\app\\static\\upload")  # temporario
    size_audio = request.content_length
    if request.method == "POST":
        file = request.files['audio']
        if file.filename == '':
            flash('Por favor, faça o upload de um áudio', 'warning')
            return render_template("audioupload.html")
        elif size_audio > 134986:
            print(size_audio)
            flash(
                'Por favor, faça o upload de um áudio de no máximo de 1 minuto', 'danger')
            return render_template("audioupload.html")
        else:
            savePath = os.path.join(
                UPLOAD_FOLDER, secure_filename(file.filename))
            file.save(savePath)
            analyzesJson = analyzes(
                audio_file_analyzed=savePath, audio_file_user=savePath)
            return render_template("analyzes.html", dados=analyzesJson)

    else:
        return render_template("audioupload.html")


@app.route('/metrics')
def metrics():
    unpackingJsonFunction = json.dumps(metricsTheAudios)
    dados = json.loads(unpackingJsonFunction)
    return render_template("metrics.html", dados=dados)
