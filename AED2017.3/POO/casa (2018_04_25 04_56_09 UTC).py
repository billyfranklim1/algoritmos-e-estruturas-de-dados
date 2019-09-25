class Moradia(object):
    def __init__(self, p, j, t, cor):
        print ('construtor chamado com sucesso')
        self.porta = p
        self.janela = j
        self.telhado = t
        self.cor = cor
        
    def imprime (self):
        print ("Casa com {} portas,{} janelas e {} telhados de cor{}".format(self.porta,self.janela,self.telhado,self.cor))
    def AbrirPorta(self):
        self.porta.abrir ()
    def FecharPorta(self):
        self.porta.fechar ()

class casa (object):
    def __init__(self, l, c, a):
        self.largura = l
        self.comprimento = c
        self.altura = a
        
    def abrir ():
        print ("{} Portas foram abertas".format(self.porta))
    def fechar ():
        print("{} Portas foram fechadas".format(self.porta))
