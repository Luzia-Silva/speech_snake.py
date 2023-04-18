# from app.models.graphics import Spectrogram, Waveshow, FundamentalFrequency, HeatSpectrogram

# def analyzes(audio_file_user, audio_file_analyzed):
#     analyzesJson = [
#         {
#             "title": "Waveshow",
#             "description": "Esse tipo de gráfico é útil para visualizar a forma de onda do sinal de áudio ao longo do tempo. Ele permite identificar características importantes do sinal, como sua duração, periodicidade, amplitude, presença de picos ou ruídos, entre outras informações. Ele analisa a amplitude como eixo y do áudio em decorrer do tempo como eixo x, essa informação é fundamental para entender as características do sinal antes de aplicar mais análise.",
#             "graphic": Waveshow(audio_file=audio_file_user).waveshowImage(),
#             "analyzedUser": "Frequência do áudio inserido",
#             "graphicSalveel": Waveshow(audio_file=audio_file_analyzed).waveshowImage()
#         },
#         {
#             "title": "Frequência fundamental f0",
#             "description": "O gráfico mostra como a frequência fundamental varia ao longo do tempo no sinal de áudio. Isso pode ser útil para análise e caracterização de diferentes tipos de sons, como música, voz e ruídos, por exemplo. O eixo horizontal (x) representa o tempo em amostras do sinal de áudio, e o eixo vertical (y) representa a frequência fundamental (F0) estimada em Hz.",
#             "graphic": FundamentalFrequency(audio_file=audio_file_user).fundamentalFrequencyImage(),
#             "analyzedUser": "Áudio analisado",
#             "graphicSalveel": FundamentalFrequency(audio_file=audio_file_analyzed).fundamentalFrequencyImage()
#         },
#         {
#             "title": "Espectograma",
#             "description": "O espectrograma apresenta graficamente como a energia do som muda em diferentes frequências ao longo do tempo. Onde são utilizados como parâmetro a frequência no eixo y, tempo no eixo x e as cores escurecendo são a amplitude calculada com o nome de Decibéis(dB) e quanto maior a energia contida em cada ponto da frequência, mais intenso será a cor mostrada. São usados para as seguintes análises: Identificação de eventos sonoros, Análise de frequência, Análise de frequência, Processamento de sinal entre outros.",
#             "graphic": Spectrogram(audio_file=audio_file_user).spectrogramImage(),
#             "analyzedUser": "Áudio analisado",
#             "graphicSalveel": Spectrogram(audio_file=audio_file_analyzed).spectrogramImage()
#         },
#         {
#             "title": "Espectograma de calor",
#             "description": "O espectograma de calor segue a mesma ideia do espectrograma comum, sua característica é que se utiliza de paletas de cores quentes voltadas a cores que representam o fogo, e a amplitude segue o mesmo conceito do anterior onde quanto maior a intensidade, mais escuramente é representado no gráfico. A linha azul representa todos os picos da amplitude no áudio e é útil para identificar os padrões rítmicos e melódicos do sinal de áudio, bem como para detectar mudanças na intensidade sonora ao longo do tempo.",
#             "graphic":  HeatSpectrogram(audio_file=audio_file_user).heatSpectrogramImage(),
#             "analyzedUser": "Áudio analisado",
#             "graphicSalveel":  HeatSpectrogram(audio_file=audio_file_analyzed).heatSpectrogramImage()
#         },
#     ]
#     return analyzesJson
