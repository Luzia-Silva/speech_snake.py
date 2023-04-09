from app.models.graphics import Spectrogram, Waveshow


def analyzes(audio_file_user, audio_file_analyzed):
    analyzesJson = [
        {
            "title": "Espectograma",
            "description": "São as frequências de ressonância da cavidade vocal que amplificam certas frequências da fonte sonora, tornando a voz mais distinta e distinguível. São usadas para caracterizar a qualidade vocal ou o timbre. Formantes mais baixas(por exemplo, F1 abaixo de 600 Hz) podem sugerir uma voz 'mais escura' ou 'mais grave'. Formantes mais altas(por exemplo, F1 acima de 800 Hz e F2 acima de 2000 Hz) podem sugerir uma voz 'mais brilhante' ou 'mais aguda'. Uma distância maior entre as formantes pode sugerir uma voz mais clara e inteligível, enquanto uma distância menor pode sugerir uma voz mais confusa ou menos clara.",
            "graphic": Spectrogram(audio_file=audio_file_user).spectrogramImage(),
            "analyzedUser": "Áudio analisado",
            "graphicSalveel": Spectrogram(audio_file=audio_file_analyzed).spectrogramImage()
        },
        {
            "title": "Waveshow",
            "description": "Esse gráfico mostra a frequência do áudio em relação a duração dele, utiliza os pontos gerados na taxa de amostragem para transformalas em colunas de tamanhos proporcionais ao valor da frequência por ponto temporal no áudio.",
            "graphic": Waveshow(audio_file=audio_file_user).waveshowImage(),
            "analyzedUser": "Frequência do áudio inserido",
            "graphicSalveel": Waveshow(audio_file=audio_file_analyzed).waveshowImage()
        }
    ]
    return analyzesJson
