class Casa (object):
	def __init__(self):
		self.tamanho_de_largura = 0
		self.tamanho_de_comprimento = 0
		self.tamanho_de_altura = 0
		self.tamanho_de_frente = 0
		#self.numero_de_cozinhas = 0
		#self.numero_de_salas = 0
		#self.numero_de_areaservico = 0
  
	def tamanhoLargura(self, numero):
		self.tamanho_de_largura += numero
		print("A largura atual é "+str(self.numero_de_portas)+".")
  
	def tamanhoCompri(self, numero):
		self.tamanho_de_comprimento += numero
		print("O comprimento atual é "+str(self.numero_de_janelas)+".")

	def tamanhoAltura(self, numero):
		self.tamanho_de_altura += numero
		print("A altura atual é "+str(self.numero_de_quartos)+".")
  
	'''def addBanheiro(self, numero):
		self.numero_de_banheiros += numero
		print("O numero de banheiros atual é "+str(self.numero_de_banheiros)+".")
    
	def addCozinha(self, numero):
		self.numero_de_cozinhas += numero
		print("O numero de cozinhas atual é "+str(self.numero_de_cozinhas)+".")

	def addSala(self, numero):
		self.numero_de_salas += numero
		print("O numero de salas atual é "+str(self.numero_de_salas)+".")

	def addServico(self, numero):
		self.numero_de_areaservico += numero
		print("O numero de áreas de serviço atual é "+str(self.numero_de_areaservico)+".")
  '''
	def 
	def verCasa(self):
		print("O numero de portas atual é "+str(self.numero_de_portas)+".")
		print("O numero de janelas atual é "+str(self.numero_de_janelas)+".")
		print("O numero de quartos atual é "+str(self.numero_de_quartos)+".")
		print("O numero de banheiros atual é "+str(self.numero_de_banheiros)+".")
		print("O numero de cozinhas atual é "+str(self.numero_de_cozinhas)+".")
		print("O numero de salas atual é "+str(self.numero_de_salas)+".")
		print("O numero de áreas de serviço atual é "+str(self.numero_de_areaservico)+".")
    


casa_verde = Casa()
casa_verde.addSala(2)
casa_verde.addCozinha(1)
casa_verde.addServico(1)
casa_verde.addQuarto(3)
casa_verde.addBanheiro(4)
casa_verde.addJanela(6)
casa_verde.addPorta(10)
#casa_verde.verCasa()

  
  
