import json
from flask import Flask, jsonify
from flask import Flask, send_file, render_template
import base64
from io import BytesIO
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
import matplotlib.pyplot as plt
import seaborn as sns
from app import app
import json
import librosa

from app.static.data.metricsTheAudios import metricsTheAudios
from app.static.data.analyzes import analyzes
from app.models.graphics import Spectrogram, Waveshow

audio_file_user = librosa.ex('trumpet')
audio_file_test = librosa.ex('trumpet')


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/audioupload")
def audioupload():
    return render_template("audioupload.html")


@app.route('/metrics')
def metrics():
    unpackingJsonFunction = json.dumps(metricsTheAudios)
    dados = json.loads(unpackingJsonFunction)
    return render_template("metrics.html", dados=dados)


@app.route("/analyzes")
def graphics():
    spectrogram = Spectrogram()
    waveshow = Waveshow()
    analyzesJson = analyzes(
        spectrogram=spectrogram.image_base64, waveshow=waveshow.image_base64)
    return render_template("analyzes.html", dados=analyzesJson)
