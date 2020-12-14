#contar de 10 a 0 e no final estourar fogos de artificio

from time import sleep
import emoji

for c in range(10, -1, -1):
    print(c)
    sleep(1)
print('Boom ', end='')
print(emoji.emojize(':fireworks:'))
