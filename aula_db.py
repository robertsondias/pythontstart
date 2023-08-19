import sqlite3

conexao = sqlite3.connect("aula_db")

conexao.execute ('''CREATE TABLE IF NOT EXISTS aluno
                 (id INTEGER PRIMARY KEY AUTOINCREMENT,
                 nome TEXT NOT NULL,
                 idade INT NOT NULL);''')

def create_aluno(nome, idade):
    conexao.execute("INSERT INTO aluno (nome, idade) VALUES (?, ?);", (nome, idade))
    conexao.commit()
    print("Aluno cadastrado com sucesso")
    
def list_aluno():
    alunos = conexao.execute("SELECT * FROM aluno;")
    for aluno in alunos:
        print(aluno)
        
def update_aluno(id, novo_nome, nova_idade):
    conexao.execute("UPDATE aluno SET nome = ?, idade = ? WHERE id = ?;", (novo_nome, nova_idade,id))
    conexao.commit()
    print("Dados atualizados corretamente")
    
def delete_aluno(id):
    conexao.execute("DELETE FROM aluno WHERE id = ?;",(id,))
    conexao.commit()
    print("Aluno deletado com sucesso")
    
#create_aluno("Tokio", "3")
#update_aluno(3, "Sylvia", "30")
delete_aluno(5)
list_aluno()
    