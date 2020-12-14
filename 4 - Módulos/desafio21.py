# reprodução de um mp3

import pygame
musica = 'Guns N Roses - Sweet Child Mine'
print(f'\033[36m{musica:=^50}\033[m')
pygame.mixer.init()
pygame.init()
pygame.mixer.music.load('desafio21.mp3')
pygame.mixer.music.play()
pygame.event.wait()
