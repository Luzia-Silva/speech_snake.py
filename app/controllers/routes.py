import json
import matplotlib.pyplot as plt
import seaborn as sns
import io
from io import BytesIO
import soundfile as sf
from six.moves.urllib.request import urlopen
import librosa
import time
import requests
import os
import parselmouth
import numpy as np
import tempfile
from b2sdk.v2 import api as b2
from flask import jsonify, redirect
from flask import send_file, render_template, request, flash, abort

from app import app
from app.static.data.aboutTheTeams import aboutTheTeams
from app.static.data.analyzes import analyzes
from app.models.frequency import Frequency
from app.enum.allowed_file import Allowed_file

b2_api = b2.B2Api()
b2_api.authorize_account("production", os.environ.get(
    "KEYID"), os.environ.get("APPLICATION_KEY"))
bucket = b2_api.get_bucket_by_name(os.environ.get(
    "BUCKETS"))


@app.errorhandler(404)
def page_not_found(e):
    return render_template('http.html', code=e), 404


@app.errorhandler(500)
def internal_server_error(e):
    return render_template('http.html', code=e), 500


def loading():
    return render_template("loading.html")


@ app.route("/")
def index():
    return render_template("index.html")

@ app.route("/audioupload", methods=["POST", "GET"])
def audioUpload():
    if request.method == "POST":
        file = request.files["audio"]
        if file.filename == "":
            flash("Por favor, faça o upload de um áudio", "warning")
            return render_template("audioupload.html")
        elif not Allowed_file(file.filename):
            flash("Não é possível realizar upload desse tipo de arquivo. Por favor, informe um arquivo de áudio desses tipos: MP3 ou WVA", "danger")
            return render_template("audioupload.html")
        elif request.content_length > 3539180:
            flash(
                "Por favor, faça o upload de um áudio de no máximo de 1 minuto", "danger")
            return render_template("audioupload.html")
        else:
            bucket.upload_bytes(file.read(), file.filename,
                                content_type='audio/wav')
            file_info = bucket.get_file_info_by_name(file.filename)
            file_id = file_info.id_
            return redirect("/formants/" + file_id)
    else:
        return render_template("audioupload.html")


@ app.route("/formants/<filename>")
def formants(filename):
    url = b2_api.get_download_url_for_fileid(filename)
    response = requests.get(url)
    if response.status_code == 200:
        bytes_io = io.BytesIO(urlopen(url).read())
        with tempfile.NamedTemporaryFile(suffix=".wav", delete=False) as tmp_file:
            tmp_file.write(bytes_io.read())
            tmp_file_path = tmp_file.name
        formants = Frequency(audio_file=tmp_file_path).audioFormants()
        os.remove(tmp_file_path)
        return render_template("formants.html", formants=formants, filename=filename)
    else:
        abort(500)


@ app.route("/analyzes/<filename>")
def analyzesUpload(filename):
    url = b2_api.get_download_url_for_fileid(filename)
    response = requests.get(url)
    if response.status_code == 200:
        bytes_io = io.BytesIO(urlopen(url).read())
        y, sr = librosa.load(bytes_io)
        analyzesJson = analyzes(y=y, sr=sr)
        return render_template("analyzes.html", dados=analyzesJson)
    else:
        abort(500)


@ app.route("/about")
def about():
    unpackingJsonFunction = json.dumps(aboutTheTeams)
    dados = json.loads(unpackingJsonFunction)
    return render_template("about.html", dados=dados)
