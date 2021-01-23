import random


def jogar():
    print('*********************************')
    print('Bem vindo ao Jogo de Adivinhação!')
    print('*********************************')

    numero_secreto = random.randrange(1, 101)
    rodada = 1
    pontos = 1000
    tentativas = 1

    print("Escolha uma dificuldade:")
    print("(1) Fácil")
    print("(2) Médio")
    print("(3) Difícil")
    print('*********************************')
    dificuldade = int(input("-> "))

    if dificuldade == 1:
        tentativas = 20
    elif dificuldade == 2:
        tentativas = 10
    elif dificuldade == 3:
        tentativas = 5
    else:
        print("Por favor, digite um número de 1 a 3")
        exit()

    while rodada <= tentativas:
        # modo normal
        # print('Você tem', rodada, 'de', tentativas, 'tentativas.')

        # modo com string interpolation
        print('Você tem {} de {} tentativas.'.format(rodada, tentativas))
        chute_str = input('Digite o seu número: ')
        print('Você digitou', chute_str)
        chute = int(chute_str)

        if chute < 0 or chute > 100:
            print('Você deve digitar um número entre 1 e 100!')
            print('*********************************')
            continue

        palpite = chute == numero_secreto
        maior = chute > numero_secreto
        menor = chute < numero_secreto

        if palpite:
            print('*********************************')
            print('Você acertou!')
            break
        else:
            if maior:
                print('Você errou! O seu chute foi maior do que o número secreto.')
            elif menor:
                print('Você errou! O seu chute foi menor do que o número secreto.')
            pontos = pontos - (abs(chute - numero_secreto))

        rodada = rodada + 1
        print('*********************************')

    print('O número secreto era: {}'.format(numero_secreto))
    print('Você acertou com {} tentativas.'.format(rodada))
    print('Sua pontuação é: {} pontos.'.format(pontos))
    print('Fim do jogo!')


if __name__ == "__main__":
    jogar()
