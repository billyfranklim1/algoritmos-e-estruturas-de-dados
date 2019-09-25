class Moradia(object):
    def __init__(self,nome,largura,comprimento,altura):
        self.nome = str(nome)
        self.largura = int (largura)
        self.comprimento =int (comprimento)
        self.altura = int(altura)
        
    def area( largura,comprimento):
        a = largura * comprimento
        print(a)
        

class Casa(Moradia):
    def __init__(self, porta, janela, teto,compartimento,aberta = True or False):
        self.porta = int (porta)
        self.janela = int (janela)
        self.teto = int (teto)
        self.compartimento = int (compartimento)
        self.aberta = aberta
        
               
    def abrirPorta(self):
        if self.porta == 1:
            print("{} porta foi aberta".format(self.porta))
        else:
            print("{} portas foram abertas".format(self.porta))

    def abrirJanela(self):
        if self.janela == 1 :
            print("{} janela foi aberta".format(self.janela))
        else:
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

    def area(self, largura,comprimento):
        a = largura * comprimento
        print(a)

    def stts (self):
        if self.aberta == False:
            print ("A casa está fechada")
            if self.aberta == True :
                print("A casa está aberta")
        

        
class Barraco(Moradia):
    
    def __init__(self, porta, janela, teto,compartimento):
        self.porta = int (porta)
        self.janela = int (janela)
        self.teto = int (teto)
        self.compartimento = int (compartimento)
        
    def abrirPorta(self):
        if self.porta == 1:
            print("{} porta foi aberta".format(self.porta))
        else:
            print("{} portas foram abertas".format(self.porta))

    def abrirJanela(self):
        if self.janela == 1 :
            print("{} janela foi aberta".format(self.janela))
        else:
            print("{} janela foram abertas".format(self.janela))
            
    def destruitTeto(self):
        if self.teto == 1 :
            print ("{} teto foi destruido".format(self.teto))
        else:
            print(" {} tetos foram de destruidos".format(self.teto))
            
    def numcompartimento(self):
        if self.compartimento == 1:
            print("O Barraco tem {} compartimento".format(self.compartimento))
        else:
            print ("O Barraco tem {} compartimentos".format(self.compartimento))


            
    def area(self, largura,comprimento):
        a = largura * comprimento
        print(a)

        
class Mansao (Moradia):
    
    def __init__(self, porta, janela, teto,compartimento):
        self.porta = int (porta)
        self.janela = int (janela)
        self.teto = int (teto)
        self.compartimento = int (compartimento)
        
    def abrirPorta(self):
        if self.porta == 1:
            print("{} porta foi aberta".format(self.porta))
        else:
            print("{} portas foram abertas".format(self.porta))

    def abrirJanela(self):
        if self.janela == 1 :
            print("{} janela foi aberta".format(self.janela))
        else:
            print("{} janela foram abertas".format(self.janela))
            
    def destruitTeto(self):
        if self.teto == 1 :
            print ("{} teto foi destruido".format(self.teto))
        else:
            print(" {} tetos foram de destruidos".format(self.teto))
            
    def numcompartimento(self):
        if self.compartimento == 1:
            print("A Mansao tem {} compartimento".format(self.compartimento))
        else:
            print ("A Mansao tem {} compartimentos".format(self.compartimento))
            
    def area(self, largura,comprimento):
        a = largura * comprimento
        print(a)


