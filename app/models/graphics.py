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

audio_file = librosa.ex('trumpet')

class Spectrogram():
    y, sr = librosa.load(audio_file)
    spectrogram = librosa.feature.melspectrogram(y=y, sr=sr)
    librosa.display.specshow(librosa.power_to_db(
        spectrogram, ref=np.max), y_axis='mel', x_axis='time')
    plt.colorbar(format='%+2.0f dB')
    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    image_base64 = base64.b64encode(buffer.getvalue()).decode('utf-8')


class Waveshow():
    y, sr = librosa.load(audio_file, sr=None)
    plt.figure(figsize=(14, 5))
    librosa.display.waveshow(y, sr=sr)
    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    image_base64 = base64.b64encode(buffer.getvalue()).decode('utf-8')


# class StartDetectionAndClickSynthesis():
#     y, sr = librosa.load(audio_file)
#     onset_env = librosa.onset.onset_strength(y=y, sr=sr, max_size=5)
#     onset_frames = librosa.onset.onset_detect(onset_envelope=onset_env, sr=sr)
#     times = librosa.times_like(onset_env, sr=sr)
#     plt.plot(times, onset_env, label='Força inicial')
#     plt.vlines(times[onset_frames], 0, onset_env.max(),
#                color='r', linestyle='--', label='Inicio')
#     plt.legend()
#     buffer = BytesIO()
#     plt.savefig(buffer, format='png')
#     image_base64 = base64.b64encode(buffer.getvalue()).decode('utf-8')
