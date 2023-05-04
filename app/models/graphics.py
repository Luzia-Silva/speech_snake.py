import librosa
import librosa.display
import parselmouth
import numpy as np
import matplotlib.pyplot as plt

from app.enum.save_image import Save_image

class Waveshow:
    def __init__(self, y, sr):
       self.y = y
       self.sr = sr

    def waveshowImage(self):
        y = self.y
        sr = self.sr
        plt.figure(figsize=(14, 5))
        librosa.display.waveshow(y, sr=sr)
        image = Save_image()
        return image


class FundamentalFrequency:
    def __init__(self, y, sr):
        self.y = y
        self.sr = sr

    def fundamentalFrequencyImage(self):
        y = self.y
        sr = self.sr
        f0_yin = librosa.yin(y, fmin=librosa.note_to_hz(
            'C2'), fmax=librosa.note_to_hz('C7'))
        plt.plot(f0_yin)
        plt.xlabel('Tempo (Amostras)')
        plt.ylabel('Frequência (Hz)')
        image = Save_image()
        return image


class Spectrogram:
    def __init__(self, y, sr):
        self.y = y
        self.sr = sr

    def spectrogramImage(self):
        y = self.y
        sr = self.sr
        S = np.abs(librosa.stft(y))
        fig, ax = plt.subplots()
        img = librosa.display.specshow(librosa.amplitude_to_db(S,
                                                               ref=np.max),
                                       y_axis='log', x_axis='time', ax=ax)
        fig.colorbar(img, ax=ax, format="%+2.0f dB")
        image = Save_image()
        return image


# ! Em analise 
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
#         image = Save_image()
#         return image
