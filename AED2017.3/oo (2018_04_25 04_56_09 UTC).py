class Casa (object):
    def __init__(self):
        self.largura = 0
        self.comprimento = 0
        self.altura = 0
        self.numero_de_teto = 0
        self.numero_de_portas = 0
	self.numero_de_janelas = int 0 :
	self.numero_de_quartos = 0
	self.numero_de_banheiros = 0
	self.numero_de_cozinhas = 0
	self.numero_de_salas = 0
	self.numero_de_areaservico = 0
	self.numero_de_compartimento = 0

    
    def abrirPorta(self):
        if numero_de_portas == 1:
            print("{} porta foi aberta".format(numero_de_portas))
        else:
            print("{} portas foram abertas".format(numero_de_portas))

    def abrirJanela(self):
        if numero_de_janelas == 1 :
            print("{} janela foi aberta".format(numero_de_janelas))
        else:
            print("{} janela foram abertas".format(numero_de_janelas))
            

    def area(self):
        return (self.largura * self.comprimento)
    
    def numero_de_compartimento(self):
        return( self.numero_de_quartos +	self.numero_de_banheiros +	self.numero_de_cozinhas + self.numero_de_salas + self.numero_de_areaservico)
        
    def addPorta(self, numero):
	self.numero_de_portas + = numero
	#print("O numero de portas atual é {} ."+str(self.numero_de_portas)+".")
       print("O numero de portas atual é {} .".format(self.numero_de_portas))  
  
    def addJanela(self, numero):
	self.numero_de_janelas += numero
	print("O numero de janelas atual é {} .".format(self.numero_de_janelas))
		#print("O numero de janelas atual é "+str(self.numero_de_janelas)+".")

    def addQuarto(self, numero):
		self.numero_de_quartos += numero
		print("O numero de quartos atual é{} . ".format(self.numero_de_quartos))
		#print("O numero de quartos atual é "+str(self.numero_de_quartos)+".")
  
    def addBanheiro(self, numero):
	self.numero_de_banheiros += numero
	print("O numero de banheiros atual é {}. ".format(self.numero_de_banheiros))
		#print("O numero de banheiros atual é "+str(self.numero_de_banheiros)+".")
    
    def addCozinha(self, numero):
	self.numero_de_cozinhas += numero
	print("O numero de cozinhas atual é {}.".format(self.numero_de_cozinhas))
		#print("O numero de cozinhas atual é "+str(self.numero_de_cozinhas)+".")

    def addSala(self, numero):
	self.numero_de_salas += numero
	print("O numero de salas atual é {} .".format(self.numero_de_salas))
		#print("O numero de salas atual é "+str(self.numero_de_salas)+".")

    def addServico(self, numero):
	self.numero_de_areaservico += numero
	print("O numero de áreas de serviço atual é {} .".format(self.numero_de_areaservico))
	#print("O numero de áreas de serviço atual é "+str(self.numero_de_areaservico)+".")
  
    def verCasa(self):
        print("A largura atual é {}".format(self.largura))
        print("O comprimento atual é {}".format(self.comprimento))
        print("A altura atual é {}".format(self.altura))
        print("A Área atual é {}".format(self.area))
        print("O numero de compartimentos atual é {}".format(self.numero_de_compartimento))
    
        print("O numero de portas atual é {}".format(self.numero_de_portas))
	#print("O numero de portas atual é "+str(self.numero_de_portas)+".")
        print("O numero de janelas atual é {} ".format(self.numero_de_janelas))
		#print("O numero de janelas atual é "+str(self.numero_de_janelas)+".")
        print("O numero de quartos atual é {}. ".format(self.numero_de_quartos))
		#print("O numero de quartos atual é "+str(self.numero_de_quartos)+".")
        print("O numero de banheiros atual é {} ."format(self.numero_de_banheiros))
#print("O numero de banheiros atual é "+str(self.numero_de_banheiros)+".")
        print("O numero de cozinhas atual é {} .".format(self.numero_de_cozinhas))
		#print("O numero de cozinhas atual é "+str(self.numero_de_cozinhas)+".")
        print("O numero de salas atual é {} .".format(self.numero_de_salas))
		#print("O numero de salas atual é "+str(self.numero_de_salas)+".")
        print("O numero de áreas de serviço atual é {}. ".format(self.numero_de_areaservico))
		#print("O numero de áreas de serviço atual é "+str(self.numero_de_areaservico)+".")
		
		
		 '''self.largura = 0
        self.comprimento = 0
        self.altura = 0
        self.numero_de_teto = 0
        self.numero_de_portas = 0
		self.numero_de_janelas = 0
		self.numero_de_quartos = 0
		self.numero_de_banheiros = 0
		self.numero_de_cozinhas = 0
		self.numero_de_salas = 0
		self.numero_de_areaservico = 0
		self.numero_de_compartimento = 0'''


minhacasa = Casa()
minhacasa.altura=3
minhacasa.largura=6
minhacasa.comprimento=8
minhacasa.addSala(2)
minhacasa.addCozinha(1)
minhacasa.addServico(1)
minhacasa.addQuarto(3)
minhacasa.addBanheiro(4)
minhacasa.addJanela(6)
minhacasa.addPorta(10)
minhacasa.abrirPorta()
minhacasa.abrirJanela()
minhacasa.area()
minhacasa.numero_de_compartimento()
minhacasa.verCasa()

#minhacasa=Casa()
#minhacasa.nome="Cafofo"
#minhacasa.altura=3
#minhacasa.largura=6
#minhacasa.comprimento=8
#print("A área da casa ",minhacasa.nome," é",minhacasa.area())
