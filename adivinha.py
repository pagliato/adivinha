from random import randint
print('#### Iníciando Jogo ####')
random = randint(0, 100)
chute = 0;
chances = 10;
for _ in range (chances):
    chute = input('Chute um número entre 0 a 100: ')
    if chute.isnumeric():
        chute = int(chute)
        chances = chances - 1
        if chute == random:
            print('')
            print('Parabéns, você acertou! O número era {} e você a inda tinha {} chances.'.format(random, chances))
            break;
        else:
            print('')
            if chute > random:
                print('Você errou!!! Dica: É menor.')
                print('Chances restantes: {} .'.format(chances))
            else:
                print('Você errou!!! Dica: É um número maior.')
                print('Chances restantes: {} .'.format(chances))
            print('')
        if chances == 0:
            print('')
            print('Suas chances acabaram. O número correto era {}.'.format(random))
            print('')
            break;
print('#### Fim do Jogo ####')
