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

        if (f1 > 300 and f1 < 900) and (f2 > 800 and f2 < 2800):
            return [
                "F1:" + " " + str(round(f1, 2)),
                "F2:" + " " + str(round(f2, 2)),
                "O primeiro formante, F1, está relacionado principalmente com a abertura do trato vocal, enquanto o segundo formante, F2, está relacionado principalmente com a posição da língua no trato vocal.",
            ]
        elif f1 > 900 and (f2 > 800 and f2 < 2800):
            f1_range = f1 + (f1 * 0.25)
            return [
                "F1:" + " " + str(round(f1, 2)),
                "F2:" + " " + str(round(f2, 2)),
                "O primeiro formante, F1, está relacionado principalmente com a abertura do trato vocal, enquanto o segundo formante, F2, está relacionado principalmente com a posição da língua no trato vocal.",
                "Com base em estudos visualizamos que o F1 está maior que o paramentros encontrados pela equipe, então realizamos um estudo de que um range de 25% no F1. "
            ]

        else:
            return [
                "F1:" + " " + str(round(f1, 2)),
                "F2:" + " " + str(round(f2, 2)),
                "O primeiro formante, F1, está relacionado principalmente com a abertura do trato vocal, enquanto o segundo formante, F2, está relacionado principalmente com a posição da língua no trato vocal.",
                 "Com base em estudos visualizamos que o F1 está maior que o paramentros encontrados pela equipe, então realizamos um estudo de que um range de 25% no F1."
            ]
