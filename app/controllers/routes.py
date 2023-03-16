from flask import Flask, send_file, render_template
import base64
from io import BytesIO
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
import matplotlib.pyplot as plt
import seaborn as sns
from app import app

from app.models.analyzes import StartDetectionAndClickSynthesis


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/analyzes")
def graphics():
    images = StartDetectionAndClickSynthesis()
    return render_template("analyzes.html", img_base64=images.image_base64)


@app.route("/analyzes")
def graphic03():
    images = StartDetectionAndClickSynthesis()
    return "teste"
