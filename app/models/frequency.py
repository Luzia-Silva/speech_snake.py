import parselmouth
from pydub import AudioSegment


class Frequency:
    def __init__(self, audio_file, filename):
        self.audio_file = audio_file
        self.filename = filename

    def audioFrequency(self):
        sound = parselmouth.Sound(self.audio_file)
        pitch = sound.to_pitch()
        pitch_values = pitch.selected_array['frequency']
        f0_mean = sum(pitch_values) / len(pitch_values)
        return f0_mean

    def frequencyFromFilteredAudioSave(self):
        audio_file = AudioSegment.from_wav(self.audio_file)
        cutoff_freq = 2000
        filtered_audio = audio_file.low_pass_filter(cutoff_freq)
        filtered_audio.export("app/static/upload_export/" +
                              self.filename, format='wav')
