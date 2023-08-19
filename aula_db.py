import sqlite3

conexao = sqlite3.connect("aula.db")

conexao.execute ('''CREATE TABLE IF NOT EXISTS aluno
                 (id INTEGER PRIMARY KEY AUTOINCREMENT,
                 nome TEXT NOT NULL,
                 idade INT NOT NULL);''')

def cria_aluno(nome, idade):
    conexao.execute("INSERT INTO aluno (nome, idade) VALUES (?, ?);", (nome, idade));
    conexao.commit()
    print("Aluno cadastrado")
    
def listar_alunos():
    alunos = conexao.execute("SELECT * FROM aluno;")
    for aluno in alunos:
        print(aluno)
    
def atualizar_aluno(id, novo_nome, nova_idade):
    conexao.execute("UPDATE aluno SET nome = ?, idade = ? WHERE id = ?;", (novo_nome, nova_idade, id))
    conexao.commit()
    print("Dados atualizados corretamente")
    
def deletar_aluno(id):
    conexao.execute("DELETE FROM aluno WHERE id = ?;",(id,))
    conexao.commit()
    print("Arquivo deletado com sucesso")
    
#cria_aluno("Elza", "79")
# atualizar_aluno(4,"Sylvia","30")
deletar_aluno(6)
listar_alunos()