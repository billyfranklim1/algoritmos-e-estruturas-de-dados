from lista_telefonica import ListaTel

ListaTel = ListaTel()

def escolherOpcao(escolha):
	opcoes = {
		1: ListaTel.exibirLista,
		2: ListaTel.contarNumeroNos,
		3: procurarContato,
		4: inserirInicio,
		5: gravar,
		6: remover,
	
	
	}
	
	opcoes.get(escolha, "")()

def procurarContato():
	info = input('entre com a produto que deseja procurar: ')
	ListaTel.procurarContato(info)	

def inserirInicio():
	info=[]
	nome = input('entre com o nome que deseja Comprar: ')
	#ListaTel.inserirInicio(info)
	fone = input('entre com o quantidade que deseja Comprar: ')
	info=[nome,fone]
	ListaTel.inserirInicio(info)

def remover():
	info = input('entre com o produto que deseja remover: ')
	ListaTel.remover(info)
	
def gravar():
     nome_arquivo = "dados.txt"
     ListaTel.gravarArquivo(nome_arquivo)


def main():
	
	ListaTel.lerArquivo()
	
	
	while(True):
		print('1. Exibir lista de compras')
		print('2. Contar o numero de Nos')
		print('3. Procurar um produto')
		print('4. Inserir no inicio da lista')
		print('5. Salvar lista em arquivo')
		print('6. Remover um produto especificado')
		print('10. Sair')
		
		escolha = int(input('escolha uma opcao: '))
		#escolha = 2

		if (escolha == 10):
			break
		
		escolherOpcao(escolha)



if __name__ == "__main__":
	main()
#CONTAR NUMERO DE ITENS