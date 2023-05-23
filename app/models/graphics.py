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
        plt.xlabel('Tempo')
        plt.ylabel('Frequência (Hz)')
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
        plt.xlabel('Tempo')
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
        plt.xlabel('Tempo')
        plt.ylabel('Frequência (Hz)')
        fig.colorbar(img, ax=ax, format="%+2.0f dB")
        image = Save_image()
        return image


class SpectrogramMfcc:
    def __init__(self, y, sr):
        self.y = y
        self.sr = sr

    def spectrogramMfccImage(self):
        y = self.y
        sr = self.sr
        fig, ax = plt.subplots()
        mfccs = librosa.feature.mfcc(y=y, sr=sr, n_mfcc=40)
        mfccs_db = librosa.amplitude_to_db(np.abs(mfccs))
        img = librosa.display.specshow(
            mfccs_db, x_axis="time", y_axis='log', ax=ax, cmap='Spectral')
        fig.colorbar(img, ax=ax)
        ax.set(title='MFCC')
        image = Save_image()
        return image

