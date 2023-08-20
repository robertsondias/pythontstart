import sqlite3

conexao = sqlite3.connect("aula.db")

conexao.execute(''' CREATE TABLE IF NOT EXISTS aluno
                (id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL,
                idade INT NOT NULL);''')

def create_aluno(conexao, nome, idade):
    novo_aluno = conexao.execute('INSERT INTO aluno (nome, idade) VALUES (? , ?);', (nome, idade))
    conexao.commit() 
    print(" Aluno cadastrado com sucesso")
    return novo_aluno
    
def list_aluno(conexao):
    alunos = conexao.execute('SELECT * FROM aluno;')
    alunos_list = []
    for aluno in alunos:
        alunos_list.append(aluno)
    return alunos_list

        
def update_aluno(conexao, id, new_name, new_age):
    aluno_atualizado = conexao.execute('UPDATE aluno SET nome = ?, idade = ? WHERE id = ?;', (new_name, new_age, id))
    conexao.commit()
    print(" Dados atualizados com sucesso")
    return aluno_atualizado
    
def delete_aluno(conexao, id):
    conexao.execute('DELETE FROM aluno WHERE id = ?;', (id,))
    conexao.commit()
    print("Aluno deletado com sucesso")
    
# create_aluno(conexao, "Robertson", "40")
# # update_aluno(5, "Elza", "79")
# # delete_aluno(1)
# list_aluno(conexao)