class Autor():
    def __init__(self,nome):
        self.nome = nome
    
class Livro():
    def __init__(self, titulo, autor ):
        self.titulo = titulo
        self.autor = autor
        self.emprestado = False
        
    def emprestar(self):
        if self.emprestado == False:
            self.emprestado = True
        else:
            print ("Livro já foi emprestado")
    
    def devolver(self,):
        if self.emprestado == True:
            self.emprestado = False
        else:
            print("Livro já devolvido")

class Usuario():
    def __init__(self,login):
        self.login = login
        
autor1 = Autor ("McDonalds")
livro1 = Livro ("Fazer hamburguer", autor1)

livro1.emprestar()
print(autor1.nome)
print(livro1.titulo)
print(livro1.emprestado)
livro1.emprestar()