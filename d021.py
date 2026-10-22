from pygame import init, mixer, event
from time import sleep

print('Abrir e reproduzir MP3')
init()
mixer.music.load('d021.mp3')
mixer.music.play()
event.wait()

sleep(100)