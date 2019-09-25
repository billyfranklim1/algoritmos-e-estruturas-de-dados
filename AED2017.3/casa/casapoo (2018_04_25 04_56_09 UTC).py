class Moradia(object):
    def __init__(self):
        
        
    def dimencoes (largura,comprimento,altura):
        self.largura = largura
        self.comprimento = comprimento
        self.altura = altura
        
    def move(self):
        self.casa.abrirPorta()
        self.casa.abrirJanela()

class casa(object):
    def __init__(self):
        
        
    def c1( porta, janela, teto,compartimento):
        self.porta = porta
        self.janela = janela
        self.teto = teto
        self.compartimento = compartimento

    def abrirPorta(self):
        if self.abrirPorta() == 1:
            print("{} porta foi aberta".format(self.abrirPorta()))
        else:
            print("{} portas foram abertas".format(self.porta))

    def abrirJanela(self):
        print("{} janela foram abertas".format(self.janela))

    def destruitTeto(self):
        if self.teto == 1 :
            print ("{} teto foi destruido".format(self.teto))
        else:
            print(" {} tetos foram de destruidos".format(self.teto))
            
    def numcompartimento(self):
        if self.compartimento == 1:
            print("A casa tem {} compartimento".format(self.compartimento))
        else:
            print ("A casa tem {} compartimentos".format(self.compartimento))