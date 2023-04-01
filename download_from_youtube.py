# Instalando o pytube:
# No terminal, "pip install pytube".

# Importando a biblioteca pytube:
from pytube import YouTube

# Link do vídeo desejado:
link_video = YouTube('https://www.youtube.com/watch?v=VLW1ieY4Izw&list=RDVLW1ieY4Izw&start_radio=1')

# Selecionar resolução e baixar vídeo:
resolucao_video = link_video.streams.get_highest_resolution()
baixar_video = resolucao_video.download()

# O vídeo irá aparecer no seu atual diretório:
print('Vídeo Baixado!')
