# Instalando o pytube:
# No terminal, "pip install pytube".

# Importando a biblioteca pytube:
from pytube import YouTube

# Link do vídeo desejado:
link_video = YouTube('https://www.youtube.com/watch?v=5bId3N7QZec&list=PLhW07ChsTWK9FuWS1TTURuUoEXBWwQ9jv&index=4')

# Selecionar resolução e baixar vídeo:
resolucao_video = link_video.streams.get_highest_resolution() # Mesmo se o vídeo for 4k, baixa no máximo em HD 1280x720.
baixar_video = resolucao_video.download()

# O vídeo irá aparecer no seu atual diretório:
print('Vídeo Baixado!')
