import librosa
import seaborn as sn
import librosa.display as ld
from IPython.display import HTML, Audio
import numpy as np
import time
from datetime import datetime
import math
import matplotlib.pyplot as plt
from io import BytesIO
import base64


class StartDetectionAndClickSynthesis():
    y, sr = librosa.load(librosa.ex('trumpet'))
    onset_env = librosa.onset.onset_strength(y=y, sr=sr, max_size=5)
    onset_frames = librosa.onset.onset_detect(onset_envelope=onset_env, sr=sr)
    times = librosa.times_like(onset_env, sr=sr)
    plt.plot(times, onset_env, label='Força inicial')
    plt.vlines(times[onset_frames], 0, onset_env.max(),
               color='r', linestyle='--', label='Inicio')
    plt.legend()
    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    image_base64 = base64.b64encode(buffer.getvalue()).decode('utf-8')
