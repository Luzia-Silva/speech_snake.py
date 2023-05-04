from app.models.graphics import Spectrogram, Waveshow, FundamentalFrequency


def analyzes(y, sr):
    analyzesJson = [
        {
            "title": "Waveshow",
            "description": "Esse tipo de gráfico é útil para visualizar a forma de onda do sinal de áudio ao longo do tempo. Ele permite identificar características importantes do sinal, como sua duração, periodicidade, amplitude, presença de picos ou ruídos, entre outras informações. Ele analisa a amplitude como eixo y do áudio em decorrer do tempo como eixo x, essa informação é fundamental para entender as características do sinal antes de aplicar mais análise. Essa informação é fundamental para entender as características do sinal antes de aplicar outras análises.",
            "graphic": Waveshow(y=y, sr=sr).waveshowImage(),
            "type": "Gráfico gerado com dados do áudio analisado",
        },
         {
            "title": "Frequência fundamental f0",
            "description": "O gráfico mostra como a frequência fundamental varia ao longo do tempo no sinal de áudio. Isso pode ser útil para análise e caracterização de diferentes tipos de sons, como música, voz e ruídos, por exemplo. O eixo horizontal (x) representa o tempo em amostras do sinal de áudio, e o eixo vertical (y) representa a frequência fundamental (F0) estimada em Hz.",
            "graphic": FundamentalFrequency(y=y, sr=sr).fundamentalFrequencyImage(),
            "type": "Gráfico gerado com dados do áudio analisado",
        },
        {
            "title": "Espectograma",
            "description": "O espectrograma apresenta graficamente como a energia do som muda em diferentes frequências ao longo do tempo. Como parâmetro são utilizados a frequência no eixo y, tempo no eixo x e as cores mais escuras correspondem a amplitude calculada em Decibéis(dB). Quanto maior a energia contida em cada ponto da frequência, mais intensa será a cor exibida. As seguintes análises são realizadas: identificação de eventos sonoros, análise de frequência, processamento de sinal entre outros.",
            "graphic": Spectrogram(y=y, sr=sr).spectrogramImage(),
            "type": "Gráfico gerado com dados do áudio analisado",

        },
        

    ]
    return analyzesJson
# {
#             "title": "Espectograma de calor",
#             "description": "O espectrograma de calor possui o mesmo conceito do espectrograma comum, o que difere é a utilização de paletas de cores quentes como fogo. A amplitude mantém a característica de quanto maior a intensidade, mais escura a cor exibida no gráfico. A linha azul representa todos os picos da amplitude no áudio e é útil para identificar os padrões rítmicos e melódicos do sinal de áudio, bem como para detectar mudanças na intensidade sonora ao longo do tempo.",
#             "graphic":  HeatSpectrogram(audio_file=audio_file_user).heatSpectrogramImage(),
#             "type": "Gráfico gerado com dados do áudio analisado",

#         },
