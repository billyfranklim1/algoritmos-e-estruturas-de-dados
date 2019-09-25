from casapoo import Moradia, casa
moradia = Moradia(2,2,2)
casa = casa(20,30,10,30)

    def escolherOpcao(escolha):
    opcoes = {
        1: dimencoes,
        2: c1,
                    #3: exibirInicio,
                    #4: exibir,
                    #5: obterTamanho,
        }
            
        opcoes.get(escolha, "")()


    def dimencoes():
        largura = int(input("insra a largura"))
        comprimento = int(input('insira o comprimento'))
        altura = int(input('insira a altura'))
        
    def c1():
        porta = int(input("insra a porta"))
        janela = int(input("insra a janela"))
        teto = int(input("insra a teto"))
        compartimento = int(input("insra a compartimento"))
        
    def main():

            while(True):
                    print('1. Inserir dimencoes da moradia)')
                    print('2. inserir compartimentos da casa')
                    #print('3. Exibir o Elemento do Inicio')
                    #print('4. Exibir todos os Elementos da Fila')
                    #print('5. Exibir o Tamanho da Fila')
                    print('6. Sair')

                    escolha = int(input('escolha uma opcao: '))

                    if (escolha == 6):
                            break
                    
                    escolherOpcao(escolha)

if __name__ == "__main__":
    main()
