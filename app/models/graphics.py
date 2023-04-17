import librosa
import librosa.display
import parselmouth
import numpy as np
import matplotlib.pyplot as plt
import base64
import io
from io import BytesIO
import os

local_file_path = os.path.join(
    os.path.join(
        os.getcwd() + "\\app\\static\\upload"), "4_z5e2af608a48f876a8d70071c_f119835116d90c79b_d20230417_m023040_c005_v0501002_t0027_u01681698640183")


class Waveshow:
    y, sr = librosa.load(local_file_path)
    plt.figure(figsize=(14, 5))
    librosa.display.waveshow(y, sr=sr)
    img = BytesIO()
    plt.savefig(img, format='png')
    img.seek(0)
    image_base64 = base64.b64encode(img.getvalue()).decode()


class FundamentalFrequency:
    def __init__(self, audio_file):
        self.audio_file = audio_file

    def fundamentalFrequencyImage(self):
        y, sr = librosa.load(self.audio_file)
        f0_yin = librosa.yin(y, fmin=librosa.note_to_hz(
            'C2'), fmax=librosa.note_to_hz('C7'))
        plt.plot(f0_yin)
        plt.xlabel('Tempo (Amostras)')
        plt.ylabel('Frequência (Hz)')
        buffer = BytesIO()
        plt.savefig(buffer, format='png')
        image_base64 = base64.b64encode(buffer.getvalue()).decode('utf-8')
        return image_base64


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


class HeatSpectrogram:
    def __init__(self, audio_file):
        self.audio_file = audio_file

    def heatSpectrogramImage(self):
        snd = parselmouth.Sound(self.audio_file)
        intensity = snd.to_intensity()
        spectrogram = snd.to_spectrogram()
        plt.figure()
        X, Y = spectrogram.x_grid(), spectrogram.y_grid()
        sg_db = 10 * np.log10(spectrogram.values)
        plt.pcolormesh(X, Y, sg_db, vmin=sg_db.max() - 70, cmap='afmhot')
        plt.ylim([spectrogram.ymin, spectrogram.ymax])
        plt.xlabel("Tempo [Amostras]")
        plt.ylabel("Frequência[Hz]")
        plt.twinx()
        plt.plot(intensity.xs(), intensity.values.T,
                 linewidth=3, color='w')
        plt.plot(intensity.xs(), intensity.values.T, linewidth=1)
        plt.grid(False)
        plt.ylim(0)
        plt.ylabel(" Intensidade [dB]")
        plt.xlim([snd.xmin, snd.xmax])
        buffer = BytesIO()
        plt.savefig(buffer, format='png')
        image_base64 = base64.b64encode(buffer.getvalue()).decode('utf-8')
        return image_base64
