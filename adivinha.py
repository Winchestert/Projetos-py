from random import randint
from time import sleep

#Welcome
print('Seja bem vindo ao jogo da adivinhação! ')

#Fazer o computador pensar
print('_-_' *15)
pc = randint(0, 10)
print('Tente adivinhar um numero de 0 a 10 !')
print('_-_' *15)

#Agora o jogador tenta adivinhar
gamer = int(input('Qual número que eu pensei ? *-*: '))
print('Um momento...')
sleep(1)

#As condições
if gamer == pc:
    print('Parabéns!!! Você adivinhou.!.! \o/')
else:
    print('Oh, que pena, eu pensei no número {}, e não no número {}. '.format(pc, gamer))
