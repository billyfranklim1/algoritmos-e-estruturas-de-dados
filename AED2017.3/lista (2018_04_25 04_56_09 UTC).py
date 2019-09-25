from tkinter import *
#from lista_telefonica import ListaTel
#from no import No

class Application:
    def __init__(self, master=None):
            #titulo
          self.fontePadrao = ("Arial", "10")
          self.primeiroContainer = Frame(master)
          self.primeiroContainer["pady"] = 10
          self.primeiroContainer.pack()

          
          self.segundoContainer = Frame(master)
          self.segundoContainer["pady"] = 10
          self.segundoContainer.pack()

          
          self.terceiroContainer = Frame(master)
          self.terceiroContainer["pady"] = 10
          self.terceiroContainer.pack()

          self.quartoContainer = Frame(master)
          self.quartoContainer["pady"] = 10
          self.quartoContainer.pack()

          self.quintoContainer = Frame(master)
          self.quintoContainer["pady"] = 10
          self.quintoContainer.pack()

          self.sextoContainer = Frame(master)
          self.sextoContainer["pady"] = 10
          self.sextoContainer.pack()

          self.setimoContainer = Frame(master)
          self.setimoContainer["pady"] = 10
          self.setimoContainer.pack()

          self.oitavoContainer = Frame(master)
          self.oitavoContainer["pady"] = 10
          self.oitavoContainer.pack()


          
            #entrada
          self.nonoContainer = Frame(master)
          self.nonoContainer["padx"] = 20
          self.nonoContainer.pack()
               #entrada
          #self.decimoContainer = Frame(master)
          #self.decimoContainer["padx"] = 20
          #self.decimoContainer.pack()

          
           #botão
          self.decimopriContainer = Frame(master)
          self.decimopriContainer["pady"] = 20
          self.decimopriContainer.pack()
######################################################################################################
   
          self.titulo = Label(self.primeiroContainer, text="Lista de compras")
          self.titulo["font"] = ("Arial", "10", "bold")
          self.titulo.pack()

          self.exibirLista = Label(self.segundoContainer, text="1.Exbir Lista de Compras")
          self.exibirLista["font"] = ("Arial", "10", "bold")
          self.exibirLista.pack()
          
          self.contarNumeroNos = Label(self.terceiroContainer, text="2.Contar o numero de Nos")
          self.contarNumeroNos["font"] = ("Arial", "10", "bold")
          self.contarNumeroNos.pack()
          
          self.procurarContato = Label(self.quartoContainer, text="3.Procurar um produto")
          self.procurarContato["font"] = ("Arial", "10", "bold")
          self.procurarContato.pack()

          self.inserir = Label(self.quintoContainer, text="4. Inserir no inicio da lista")
          self.inserir["font"] = ("Arial", "10", "bold")
          self.inserir.pack()

          self.gravarArquivo = Label(self.sextoContainer, text="5. Salvar em arquivo")
          self.gravarArquivo["font"] = ("Arial", "10", "bold")
          self.gravarArquivo.pack()

            
          self.remover = Label(self.setimoContainer, text="6. Remover um produto especificado")
          self.remover["font"] = ("Arial", "10", "bold")
          self.remover.pack()      

          self.sair = Label(self.oitavoContainer, text="10. Sair")
          self.sair["font"] = ("Arial", "10", "bold")
          self.sair.pack()

          self.escolha = Label(self.oitavoContainer, text="escolha uma opcao:")
          self.escolha["font"] = ("Arial", "10", "bold")
          self.escolha.pack()
         
          
               #nome ao lado da caixa de entrada
          '''self.nomeLabel = Label(self.segundoContainer,text="Nome", font=self.fontePadrao)
          self.nomeLabel.pack(side=LEFT)'''
   
          self.input = Entry(self.oitavoContainer)
          self.input["width"] = 30
          self.input["font"] = self.fontePadrao
          self.input.pack(side=LEFT)
          
          '''#nome ao lado da caixa de entrada
          self.senhaLabel = Label(self.terceiroContainer, text="Senha", font=self.fontePadrao)
          self.senhaLabel.pack(side=LEFT)
   
          self.input = Entry(self.terceiroContainer)
          self.input["width"] = 30
          self.input["font"] = self.fontePadrao
          self.input["show"] = "*"
          self.input.pack(side=LEFT)'''
               #butão
          self.executar = Button(self.nonoContainer)
          self.executar["text"] = "Executar"
          self.executar["font"] = ("Calibri", "8")
          self.executar["width"] = 12
          self.executar["command"] = self.verificaSenha
          self.executar.pack()
   
          self.mensagem = Label(self.nonoContainer, text="", font=self.fontePadrao)
          self.mensagem.pack()
   
      #Método verificar senha

    def verificaSenha(self):
        usuario = self.nome.get()
        senha = self.senha.get()
        if usuario == "usuariodevmedia" and senha == "dev":
            self.mensagem["text"] = "Autenticado"
        else:
            self.mensagem["text"] = "Erro na autenticação"

   
   
root = Tk()
Application(root)
root.mainloop()
  
