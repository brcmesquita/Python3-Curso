def jogar():
    print('***************************')
    print('Bem vindo ao Jogo da Forca!')
    print('***************************')

    enforcou = False
    acertou = False
    tentativas = 0

    palavra_secreta = "banana".upper()
    letras_acertadas = ["_" for letra in palavra_secreta]
    print("A palavra é: {}.".format(letras_acertadas))

    while not enforcou and not acertou:

        chute = input("Digite uma letra? ")
        chute = chute.strip().upper()

        if chute in palavra_secreta:
            index = 0
            for letra in palavra_secreta:
                if chute == letra:
                    letras_acertadas[index] = letra
                index = index + 1
            print("Jogando...")
        else:
            tentativas += 1

        enforcou = tentativas == 6
        acertou = "_" not in letras_acertadas

        print(letras_acertadas)

    if acertou:
        print("Você ganhou!!")
    else:
        print("Você perdeu!!")

    print("Fim do Jogo!")


if __name__ == "__main__":
    jogar()
