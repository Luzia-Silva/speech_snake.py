import parselmouth
import tempfile
from pydub import AudioSegment


class Frequency:
    def __init__(self, audio_file):
        self.audio_file = audio_file

    def audioFormants(self):
        tmp_file_path = self.audio_file
        sound = parselmouth.Sound(tmp_file_path)
        formants = sound.to_formant_burg()
        time = 0.1
        f1 = formants.get_value_at_time(1, time)
        f2 = formants.get_value_at_time(2, time)
        if f1 < 600 and f2 > 2000:
            return "Frequências Formantes da voz está clara"
        else:
            return "Frequências Formantes está confusa"
