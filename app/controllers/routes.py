import json
import matplotlib.pyplot as plt
import seaborn as sns
import io
from io import BytesIO
import soundfile as sf
from six.moves.urllib.request import urlopen
import librosa
import os
from b2sdk.v2 import api as b2
from flask import jsonify, redirect
from flask import send_file, render_template, request, flash
from app import app
from app.static.data.aboutTheTeams import aboutTheTeams
from app.static.data.analyzes import analyzes
from app.models.frequency import Frequency
from app.enum.type_file import Allowed_file


b2_api = b2.B2Api()
b2_api.authorize_account("production", os.environ.get(
    "KEYID"), os.environ.get("APPLICATION_KEY"))
bucket = b2_api.get_bucket_by_name(os.environ.get(
    "BUCKETS"))


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
        elif request.content_length > 3539180:
            flash(
                "Por favor, faça o upload de um áudio de no máximo de 1 minuto", "danger")
            return render_template("audioupload.html")
        elif not Allowed_file(file.filename):
            flash("Por favor, informe um áudio dos seguintes tipos: mp3 ou wva", "danger")
        else:
            bucket.upload_bytes(file.read(), file.filename,
                                content_type='audio/wav')
            file_info = bucket.get_file_info_by_name(file.filename)
            file_id = file_info.id_
            return redirect("/analyzes/" + file_id)
    else:
        return render_template("audioupload.html")


@ app.route("/analyzes/<filename>")
def audioupload(filename):
    url = b2_api.get_download_url_for_fileid(filename)
    print(url)
    bytes_io = io.BytesIO(urlopen(url).read())
    y, sr = librosa.load(bytes_io)
    analyzesJson = analyzes(y=y, sr=sr)
    return render_template("analyzes.html", dados=analyzesJson)


@ app.route("/about")
def metrics():
    unpackingJsonFunction = json.dumps(aboutTheTeams)
    dados = json.loads(unpackingJsonFunction)
    return render_template("about.html", dados=dados)
