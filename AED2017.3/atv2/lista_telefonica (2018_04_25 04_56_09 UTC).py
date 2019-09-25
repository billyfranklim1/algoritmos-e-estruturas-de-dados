from no import No

class ListaTel(object):
	def __init__(self):
		self.inicio = None
		
	def exibirLista(self):
		if self.inicio is None:
			print('lista vazia')
			return
			print('lista')
	
		p = self.inicio
	
		while(p is not None):
			print(" Produto: ",p.info[0], "Quantidade: ", p.info[1] )
			p=p.proximo
		print()
	
	def gravarArquivo(self, nome_arquivo):
		if self.inicio is None:
			print('lista vazia, não é possível salvar')
			return
	
		p = self.inicio
		arquivo = open(nome_arquivo, "w", encoding = "utf-8")
	
		while(p is not None):
			arquivo.write("Produto: %s\n Qantidade: %s\n" % (p.info[0], p.info[1]))
			p=p.proximo
		print("Arquivo %s salvo com sucesso" %(nome_arquivo))

	def lerArquivo(self):
		nome_arquivo='dados.txt'
		arquivo=open(nome_arquivo,'r')
		temp=[]
		for linha in arquivo:
			temp.append(linha[0:-1])
		i=0
		while i< (len(temp)):
			info=['','']
			info[0]=temp[i]
			i+=1
			info[1]=temp[i]
			self.inserirInicio(info)
			i+=1
		
	def contarNumeroNos(self):
		n=0
		p=self.inicio
		while(p is not None):
			p=p.proximo
			n+=1
		print(n)
	
	
	
	def procurarContato(self, info):
		posicao = 1
		p = self.inicio

		while (p is not None):
			if (p.info[0] == info):
				break
			posicao += 1
			p = p.proximo
		
		if p is None:
			print('%s nao encontrado na lista' % info)
			
			return False
		else:
			print(info)
			
			return True
	
	
	def inserirInicio(self, info):
		temp = No(info)
		temp.proximo = self.inicio
		self.inicio = temp

	
	def remover(self, info):
		if (self.inicio is None):
			print('lista vazia')
			
			return

		# remocao do primeiro no
		if (self.inicio.info[0] == info):
			self.inicio = self.inicio.proximo
			
			return
		
		# remocao no interior ou no final da lista
		p = self.inicio

		while (p.proximo is not None):
			if (p.proximo.info[0] == info):
				break

			p = p.proximo
		
		if (p.proximo is None):
			print('elemento ' + str(info) + ' nao localizado na lista')
		else:
			p.proximo = p.proximo.proximo


	def sair(self,info):
	
	
