
# o nome da classe deve ser sempre maiúsculo
class Cliente:

    # o __init__ é o método construtor
    def __init__(self, nome):
        self.__nome = nome

    @property # O @property transforma o método em propriedade da classe
    def nome(self):
        return self.__nome.title()

    @nome.setter # o @nome.setter serve para criar um setter com o mesmo nome do atributo
    def nome(self, nome):
        self.__nome = nome
