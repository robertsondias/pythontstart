class Pessoa():
    def __init__(self, nome, idade, sexo):
        self.nome = nome
        self.idade = idade
        self.sexo = sexo
    def saudacao(self):
        print(f"Meu nome é, {self.nome}, minha idade é {self.idade} e sou {self.sexo}")
        
class Professor(Pessoa):
    def __init__ (self, nome, idade, sexo, titulo):
        super().__init__(nome, idade, sexo)
        self.titulo=titulo
    def info(self):
        print(f"Meu titulo é {self.titulo}")
prof_1 = Professor("Manoel", "65", "MAsculino", "Doutor")
print(prof_1.nome)
print(prof_1.saudacao())
        
pessoa1 = Pessoa("Rogério", "40", "masculino")
pessoa2 = Pessoa("Manoel", "57", "masculino")
pessoa3 = Pessoa("Arnaldo", "58", "masculino")

print()
pessoa1.saudacao()
pessoa2.saudacao()
pessoa3.saudacao()
print()

print(pessoa1.nome)
print(pessoa2.idade)
print(pessoa3.sexo)