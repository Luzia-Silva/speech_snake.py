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

from app.static.data.metricsTheAudios import metricsTheAudios
from app.models.analyzes import StartDetectionAndClickSynthesis, Spectrogram


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
    images = StartDetectionAndClickSynthesis()
    return render_template("analyzes.html", img_base64=images.image_base64)
