from b2sdk.v2 import api as b2
from flask import jsonify, redirect
from flask import send_file, render_template, request, flash
import base64
from io import BytesIO
import matplotlib.pyplot as plt
import seaborn as sns
import os
from werkzeug.utils import secure_filename

import librosa
import librosa.display
import numpy as np
import io

from app import app
from app.static.data.metricsTheAudios import metricsTheAudios
from app.models.frequency import Frequency
from app.enum.type_file import Allowed_file
from app.models.graphics import Waveshow

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
        elif request.content_length > 134986:
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


@ app.route("/analyzes")
def audioupload():
    plot_html = Waveshow()
    return f'''
        <html>
            <head><title>Gráfico</title></head>
            <body>
                {plot_html}
            </body>
        </html>
    '''


@ app.route("/about")
def metrics():
    unpackingJsonFunction = json.dumps(metricsTheAudios)
    dados = json.loads(unpackingJsonFunction)
    return render_template("about.html", dados=dados)
