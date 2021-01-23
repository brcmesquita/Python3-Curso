import random


def jogar():

    imprime_mensagem_abertura()
    palavra_secreta = carrega_palavra_secreta()

    letras_acertadas = inicializa_letras_acertadas(palavra_secreta)
    print(letras_acertadas)

    enforcou = False
    acertou = False
    tentativas = 0

    while not enforcou and not acertou:

        chute = pedir_chute()

        if chute in palavra_secreta:
            marca_chute_correto(chute, letras_acertadas, palavra_secreta)
        else:
            tentativas += 1

        enforcou = tentativas == 6
        acertou = "_" not in letras_acertadas
        print(letras_acertadas)

    if acertou:
        imprime_mensagem_vencedor()
    else:
        imprime_mensagem_perdedor(palavra_secreta)

def imprime_mensagem_abertura():
    print('***************************')
    print('Bem vindo ao Jogo da Forca!')
    print('***************************')

def imprime_mensagem_vencedor():
    print("Você ganhou!!")

def imprime_mensagem_perdedor(palavra_secreta):
    print("Você perdeu!!")
    print("A palavra era: {}.".format(palavra_secreta))

def marca_chute_correto(chute, letras_acertadas, palavra_secreta):
    index = 0
    for letra in palavra_secreta:
        if chute == letra:
            letras_acertadas[index] = letra
            index += 1

def pedir_chute():
    chute = input("Digite uma letra? ")
    chute = chute.strip().upper()
    return chute

def inicializa_letras_acertadas(palavra):
    lista = ["_" for letra in palavra]
    return lista

def carrega_palavra_secreta():
    arquivo = open("palavras.txt", "r")
    palavras = []

    for linha in arquivo:
        linha = linha.strip()
        palavras.append(linha)

    arquivo.close()

    numero = random.randrange(0, len(palavras))
    palavra_secreta = palavras[numero].upper()
    return palavra_secreta

if __name__ == "__main__":
    jogar()
