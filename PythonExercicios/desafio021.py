import webbrowser
import pygame
#import vlc

# Inicializando o mixer PyGame
pygame.mixer.init()

# Iniciando o Pygame
pygame.init()

pygame.mixer.music.load('E:\LEGIÃO URBANA\/1985 - Legi+úo Urbana\/10  Teorema.mp3')
pygame.mixer.music.play(loops=0, start=0.0)
pygame.event.wait()
#webbrowser.open('E:\LEGIÃO URBANA\/1985 - Legi+úo Urbana\/10  Teorema.mp3')
#p = vlc.MediaPlayer('E:\LEGIÃO URBANA\/1985 - Legi+úo Urbana\/10  Teorema.mp3')
#p.play()