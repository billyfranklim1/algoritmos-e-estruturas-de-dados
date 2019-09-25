from tkinter import *
#from lista_telefonica import ListaTel

class Application:
    def __init__(self, master = None):
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
   
          self.titulo = Label(self.primeiroContainer, text="Lista De Compras")
          self.titulo["font"] = ("Arial", "30", "bold")
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

          self.escolherOpcao = Label(self.oitavoContainer, text="Escolha Uma Opcao:")
          self.escolherOpcao["font"] = ("Arial", "10", "bold")
          self.escolherOpcao.pack()
              
            
          self.escolherOpcao = Entry(self.oitavoContainer)
          self.escolherOpcao["width"] = 40
          self.escolherOpcao["font"] = self.fontePadrao
          self.escolherOpcao.pack(side=LEFT)
                 #butão
          self.ir = Button(self.nonoContainer)
          self.ir["text"] = "IR"
          self.ir["font"] = ("Calibri", "15", "bold")
          self.ir["width"] = 12
          self.ir["command"] = self.escolha
          self.ir.pack()

          self.mensagem = Label(self.decimopriContainer, text="", font=self.fontePadrao)
          self.mensagem.pack()
   
      #Método verificar senha
    def escolha(self):
        usuario = self.escolherOpcao.get()
        if usuario == '1':
            self.mensagem["text"] = "Autenticado"
        #else:
            #self.mensagem["text"] = "Erro na autenticação"

          
   
   
root = Tk()
Application(root)
root.mainloop()

