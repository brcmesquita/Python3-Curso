

class Conta:

    def __init__(self, numero, titular, saldo, limite):
        print("Conta criada com sucesso!")
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite

    def extrato(self):
        print("***************")
        print("*    SALDO    *")
        print("***************")
        print("Conta:    {}".format(self.__numero))
        print("Cliente:  {}".format(self.__titular))
        print("Saldo: R$ {}".format(self.__saldo))

    def depositar(self, valor):
        self.__saldo += valor

    def __disponivel_pra_saque(self, valor_a_sacar):
        return (self.__limite + self.__saldo) < valor_a_sacar

    def sacar(self, valor):
        if self.__disponivel_pra_saque(valor):
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

    @property
    def titular(self):
        return self.__titular

    @property
    def saldo(self):
        return self.__saldo

    @property
    def limite(self):
        return self.__limite

    @limite.setter
    def limite(self, limite):
        self.__limite = limite

    @staticmethod  # método estático, são métodos da classe
    def banco():
        return "001"

    @staticmethod  # método estático, são métodos da classe
    def lista_bancos():
        return {'BB': '001', 'Caixa': '104', 'Bradesco': '237'}
