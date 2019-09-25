class PessoaS2animal(object):
    def __init__(self, nome, peso, cao):
        self.nome = nome
        self.peso = peso
        self.cao = cao

    def treinar(self):
        self.cao.daApatinha()
        self.cao.latir()

class cachorro(object):
    def __init__(self,nome,cor):
        self.nome = nome
        self.cor = cor
    def daApatinha(self):
        print("{} levandou a patinha".format(self.nome))
    def latir(self):
        print ("AUAUAUAUAUAUAU!!")
