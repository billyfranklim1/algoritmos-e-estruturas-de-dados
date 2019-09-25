from casapoo import Moradia, casa
moradia = Moradia()
casa = casa()

    def escolherOpcao(escolha):
	opcoes = {
		1: abrirPorta,
		2: abrirJanela,
		3: destruitTeto,
		4: numcompartimento,
		5: obterTamanho,
	}
	
	opcoes.get(escolha, "")()
	
'''	def __init__(self, porta, janela, teto,compartimento):
        self.porta = porta
        self.janela = janela
        self.teto = teto
        self.compartimento = compartimento'''

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