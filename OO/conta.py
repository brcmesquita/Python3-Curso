

class Conta:

    def __init__(self, numero, titular, saldo, limite):
        print("Conta criada com sucesso!")
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite

    def extrato(self):
        print("Senhor(a) {}, seu saldo é de R${} Reais.".format(self.__titular, self.__saldo))

    def depositar(self, valor):
        self.__saldo += valor

    def sacar(self, valor):
        if self.__saldo < valor:
            print("Desculpe! Saldo insuficiente.")
        else:
            self.__saldo -= valor

    def transferir(self, valor, destino):
        if self.__saldo < valor:
            print("Desculpe! Saldo insuficiente.")
        else:
            self.sacar(valor)
            destino.depositar(valor)
            print("Transferência realizada com sucesso.")


