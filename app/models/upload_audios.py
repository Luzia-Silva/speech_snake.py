
from pydub import AudioSegment

# !Mapeado para próxima entrega 

class UploadAudios:
    def __init__(self, file):
        self.file = file

    def ConvertAudio(self):
        ALLOWED_EXTENSIONS = {'mp3', 'wav', 'opus'}
        type = self.file.filename.rsplit('.', 1)[1].lower()
        filename = self.file.filename.rsplit('.', 0)[0].lower()
        audio = AudioSegment.from_file(self.file, format=type)
        return audio.export(filename, format="wav")
