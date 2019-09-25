class Moradia(object):
    def __init__(self,largura,comprimento,altura,casa =0):
        self.largura = largura
        self.comprimento = comprimento
        self.altura = altura
        self.casa = casa
        
    def move(self):
        self.casa.abrirPorta()
        self.casa.abrirJanela()

class casa(object):
    def __init__(self, porta, janela, teto):
        self.porta = porta
        self.janela = janela
        self.teto = teto

    def abrirPorta(self):
        print("{} portas foram abertas".format(self.porta))

    def abrirJanela(self):
        print("{} janela foram abertas".format(self.janela))

    def destruitTeto(self):
        if self.teto == 1 :
            print ("{} teto foi destruido".format(self.teto))
        else:
            print(" {} tetos foram de destruidos".format(self.teto))
