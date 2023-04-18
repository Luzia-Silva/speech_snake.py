import librosa
import librosa.display
import parselmouth
import numpy as np
import matplotlib.pyplot as plt
import base64
import io
from io import BytesIO
import os


def Waveshow():
    filename = "./upload/4_z5e2af608a48f876a8d70071c_f1068c9b138f01d2e_d20230418_m142104_c005_v0501001_t0001_u01681827664597"
    y, sr = librosa.load(filename)
    spec = librosa.feature.melspectrogram(y=y, sr=sr)
    fig, ax = plt.subplots(figsize=(10, 4))
    img = librosa.display.specshow(librosa.power_to_db(spec, ref=np.max),
                            y_axis='mel', fmax=8000,
                            x_axis='time', ax=ax)
    ax.set(title='Espectrograma')
    plt.colorbar(img, ax=ax, format='%+2.0f dB')
    plt.tight_layout()
    buf = io.BytesIO()
    fig.savefig(buf, format='png', dpi=300, bbox_inches='tight')
    buf.seek(0)
    data = base64.b64encode(buf.read()).decode("utf-8")
    return f'<img src="data:image/png;base64,{data}"/>'



# class FundamentalFrequency:
#     def __init__(self, audio_file):
#         self.audio_file = audio_file

#     def fundamentalFrequencyImage(self):
#         y, sr = librosa.load(self.audio_file)
#         f0_yin = librosa.yin(y, fmin=librosa.note_to_hz(
#             'C2'), fmax=librosa.note_to_hz('C7'))
#         plt.plot(f0_yin)
#         plt.xlabel('Tempo (Amostras)')
#         plt.ylabel('Frequência (Hz)')
#         buffer = BytesIO()
#         plt.savefig(buffer, format='png')
#         image_base64 = base64.b64encode(buffer.getvalue()).decode('utf-8')
#         return image_base64


# class Spectrogram:
#     def __init__(self, audio_file):
#         self.audio_file = audio_file

#     def spectrogramImage(self):
#         y, sr = librosa.load(self.audio_file)
#         S = np.abs(librosa.stft(y))
#         fig, ax = plt.subplots()
#         img = librosa.display.specshow(librosa.amplitude_to_db(S,
#                                                                ref=np.max),
#                                        y_axis='log', x_axis='time', ax=ax)
#         fig.colorbar(img, ax=ax, format="%+2.0f dB")
#         buffer = BytesIO()
#         plt.savefig(buffer, format='png')
#         image_base64 = base64.b64encode(buffer.getvalue()).decode('utf-8')
#         return image_base64


# class HeatSpectrogram:
#     def __init__(self, audio_file):
#         self.audio_file = audio_file

#     def heatSpectrogramImage(self):
#         snd = parselmouth.Sound(self.audio_file)
#         intensity = snd.to_intensity()
#         spectrogram = snd.to_spectrogram()
#         plt.figure()
#         X, Y = spectrogram.x_grid(), spectrogram.y_grid()
#         sg_db = 10 * np.log10(spectrogram.values)
#         plt.pcolormesh(X, Y, sg_db, vmin=sg_db.max() - 70, cmap='afmhot')
#         plt.ylim([spectrogram.ymin, spectrogram.ymax])
#         plt.xlabel("Tempo [Amostras]")
#         plt.ylabel("Frequência[Hz]")
#         plt.twinx()
#         plt.plot(intensity.xs(), intensity.values.T, linewidth=3, color='w')
#         plt.plot(intensity.xs(), intensity.values.T, linewidth=1)
#         plt.grid(False)
#         plt.ylim(0)
#         plt.ylabel(" Intensidade [dB]")
#         plt.xlim([snd.xmin, snd.xmax])
#         buffer = BytesIO()
#         plt.savefig(buffer, format='png')
#         image_base64 = base64.b64encode(buffer.getvalue()).decode('utf-8')
#         return image_base64
