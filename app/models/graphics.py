import librosa
import librosa.display
import numpy as np
import matplotlib.pyplot as plt
import base64
import io
from io import BytesIO


class Spectrogram:
    def __init__(self, audio_file):
        self.audio_file = audio_file
    def spectrogramImage(self):
        y, sr = librosa.load(self.audio_file)
        S = np.abs(librosa.stft(y))
        fig, ax = plt.subplots()
        img = librosa.display.specshow(librosa.amplitude_to_db(S,
                                                               ref=np.max),
                                       y_axis='log', x_axis='time', ax=ax)
        fig.colorbar(img, ax=ax, format="%+2.0f dB")
        buffer = BytesIO()
        plt.savefig(buffer, format='png')
        image_base64 = base64.b64encode(buffer.getvalue()).decode('utf-8')
        return image_base64


class Waveshow:
    def __init__(self, audio_file):
        self.audio_file = audio_file
    def waveshowImage(self):
        y, sr = librosa.load(self.audio_file)
        plt.figure(figsize=(14, 5))
        librosa.display.waveshow(y, sr=sr)
        buffer = BytesIO()
        plt.savefig(buffer, format='png')
        image_base64 = base64.b64encode(buffer.getvalue()).decode('utf-8')
        return image_base64
