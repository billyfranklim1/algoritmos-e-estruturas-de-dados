from tkinter import *
   

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
          self.decimoContainer = Frame(master)
          self.decimoContainer["padx"] = 20
          self.decimoContainer.pack()

          
           #botão
          self.decimopriContainer = Frame(master)
          self.decimopriContainer["pady"] = 20
          self.decimopriContainer.pack()
######################################################################################################
   
          self.titulo = Label(self.primeiroContainer, text="Lista de compras")
          self.titulo["font"] = ("Arial", "10", "bold")
          self.titulo.pack()

          self.exibir = Label(self.segundoContainer, text="1.Exbir Lista de Compras")
          self.exibir["font"] = ("Arial", "10", "bold")
          self.exibir.pack()
          
          self.contar = Label(self.terceiroContainer, text="2.Contar o numero de Nos")
          self.contar["font"] = ("Arial", "10", "bold")
          self.contar.pack()
          
          self.procurar = Label(self.quartoContainer, text="3.Procurar um produto")
          self.procurar["font"] = ("Arial", "10", "bold")
          self.procurar.pack()

          self.inserir = Label(self.quintoContainer, text="4. Inserir no inicio da lista")
          self.inserir["font"] = ("Arial", "10", "bold")
          self.inserir.pack()

          self.salvar = Label(self.sextoContainer, text="5. Salvar em arquivo")
          self.salvar["font"] = ("Arial", "10", "bold")
          self.salvar.pack()

            
          self.remover = Label(self.setimoContainer, text="6. Remover um produto especificado")
          self.remover["font"] = ("Arial", "10", "bold")
          self.remover.pack()      

          self.remover = Label(self.oitavoContainer, text="10. Sair")
          self.remover["font"] = ("Arial", "10", "bold")
          self.remover.pack()

          self.escolha = Label(self.oitavoContainer, text="escolha uma opcao:")
          self.escolha["font"] = ("Arial", "10", "bold")
          self.escolha.pack()
         
          
               #nome ao lado da caixa de entrada
          '''self.nomeLabel = Label(self.segundoContainer,text="Nome", font=self.fontePadrao)
          self.nomeLabel.pack(side=LEFT)'''
   
          self.nome = Entry(self.oitavoContainer)
          self.nome["width"] = 30
          self.nome["font"] = self.fontePadrao
          self.nome.pack(side=LEFT)
          
          ''''     #nome ao lado da caixa de entrada
          self.senhaLabel = Label(self.terceiroContainer, text="Senha", font=self.fontePadrao)
          self.senhaLabel.pack(side=LEFT)
   
          self.senha = Entry(self.terceiroContainer)
          self.senha["width"] = 30
          self.senha["font"] = self.fontePadrao
          self.senha["show"] = "*"
          self.senha.pack(side=LEFT)'''
               #butão
          self.autenticar = Button(self.oitavoContainer)
          self.autenticar["text"] = "Autenticar"
          self.autenticar["font"] = ("Calibri", "8")
          self.autenticar["width"] = 12
          self.autenticar["command"] = self.verificaSenha
          self.autenticar.pack()
   
          self.mensagem = Label(self.quartoContainer, text="", font=self.fontePadrao)
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
  
