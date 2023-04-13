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
from app.models.frequency import Frequency
from app.controllers.file_type import allowed_file


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/audioupload")
def audioupload():
    return render_template("audioupload.html")


@app.route("/analyzes", methods=["POST", "GET"])
def upload():
    size_audio = request.content_length
    UPLOAD_FOLDER = os.path.join(
        os.getcwd() + "\\app\\static\\upload")  # !temporario
    if request.method == "POST":
        file = request.files["audio"]
        if file.filename == "":
            flash("Por favor, faça o upload de um áudio", "warning")
            return render_template("audioupload.html")
        elif size_audio > 134986:
            flash(
                "Por favor, faça o upload de um áudio de no máximo de 1 minuto", "danger")
            return render_template("audioupload.html")
        elif file and allowed_file(file.filename):
            user_save_audio = os.path.join(
                UPLOAD_FOLDER, secure_filename(file.filename))
            file.save(user_save_audio)
            analyzesJson = analyzes(
                audio_file_analyzed=user_save_audio, audio_file_user=user_save_audio)
            return render_template("analyzes.html", dados=analyzesJson)
        else:
            flash("Por favor, informe um áudio dos seguintes tipos: mp3 ou wva", "danger")
    else:
        return render_template("audioupload.html")


@app.route("/about")
def metrics():
    unpackingJsonFunction = json.dumps(metricsTheAudios)
    dados = json.loads(unpackingJsonFunction)
    return render_template("about.html", dados=dados)
