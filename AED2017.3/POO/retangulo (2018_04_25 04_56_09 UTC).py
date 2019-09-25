class Retangulo(object):
    def __init__(self, c = 0, l = 0):
        print ('construtor chamado com sucesso')
        self.comprimento = c
        self.largura = l
        
    def imprime (self):
        print ("Quadrado com {} de comprimento e {} de largura".format(self.comprimento, self.largura))
    '''def calarea(self,c = 0 ,a = c*l):
        print ("Area é de {}".format(a))
    def perimetro(self,c =0,l = 0,p = 2*c + 2*l):
        print ("Pereimetro é de {}".format(p))''''
        
		

