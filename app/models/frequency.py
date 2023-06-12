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
        time = 0.1 # Inicialização da leitura do áudio
        f1 = formants.get_value_at_time(1, time)
        f2 = formants.get_value_at_time(2, time)
        f1_range = f1 - (f1 * 0.25)

        if (f1_range > 300 and f1_range < 900) and (f2 > 800 and f2 < 2800):
            return [
                "Resultado: VOZ CLARA (range de 25% " + "aplicado)",
                "Primeiro Formante (F1): " + " " + str(round(f1_range, 2)),
                "Segundo Formante: (F2):" + " " + str(round(f2, 2)),
            ]

        else:
            return [
                "Resultado: VOZ CONFUSA",
                "Primeiro Formante: (F1)" + " " + str(round(f1, 2)),
                "Segundo Formante: (F2):" + " " + str(round(f2, 2)),
            ]
