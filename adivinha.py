from random import randint

print('#### Iníciando Jogo ####')

random = randint(0, 100)
chute = 0
chances = 10
for _ in range (chances):
    chute = input('Chute um número entre 0 a 100: ')
    if chute.isnumeric():
        chute = int(chute)
        chances = chances - 1
        if chute == random:
            print('Parabéns, você venceu! O número era {} e você a inda tinha {} chances.'.format(random, chances))
        else:
          if chute > random:
                print('Você errou!!! Dica: É um número menor.')
          else:
                print('Você errou!!! Dica: É um número maior.')
        if chances == 0:
            print('Suas chances acabaram, você perdeu!')
    if chances == 0 or chute == random:
      break;
print('#### Fim do Jogo ####')
