from app.models.graphics import Spectrogram, Waveshow, FundamentalFrequency, HeatSpectrogram


def analyzes(image):
    analyzesJson = [
        {
            "title": "Waveshow",
            "description": "Esse tipo de gráfico é útil para visualizar a forma de onda do sinal de áudio ao longo do tempo. Ele permite identificar características importantes do sinal, como sua duração, periodicidade, amplitude, presença de picos ou ruídos, entre outras informações. Ele analisa a amplitude como eixo y do áudio em decorrer do tempo como eixo x, essa informação é fundamental para entender as características do sinal antes de aplicar mais análise.",
            "graphic": image,
            "analyzedUser": "Frequência do áudio inserido",
            "graphicSalveel": image,
        },

    ]
    return analyzesJson
