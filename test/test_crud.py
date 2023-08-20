import unittest
import sqlite3
from aula_db import create_aluno, list_aluno, update_aluno, delete_aluno


class TestCrus(unittest.TestCase):
     def setUp(self):
         self.conexao = sqlite3.connect(":memory:")
         self.conexao.execute('''CREATE TABLE IF NOT EXISTS aluno
                (id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL,
                idade INT NOT NULL);''')
         
     def tearDown(self):
         self.conexao.close()
         
     def test_create_aluno(self):
         create_aluno(self.conexao, "Robertson", 41)
         create_aluno(self.conexao, "Jaqueline", 59)
         alunos = self.conexao.execute ("SELECT * FROM aluno").fetchall()
         self.assertEqual(len(alunos), 2)
         self.assertEqual(alunos[0][1], "Robertson")
         
     def test_list_aluno(self):
         create_aluno(self.conexao, "Robertson", 41)
         create_aluno(self.conexao, "Jaqueline", 59)
         alunos = list(list_aluno(self.conexao))
         self.assertEqual(len(alunos), 2)

                  
     def test_update_aluno(self):
         create_aluno(self.conexao, "Robertson", 41)
         create_aluno(self.conexao, "Jaqueline", 59)
         update_aluno(self.conexao,1, "Robertson Dias", "42")
         aluno = self.conexao.execute("SELECT * FROM aluno WHERE id = ?", (1,)).fetchall()
         self.assertEqual(aluno[0][1], "Robertson Dias")
         
     def test_delete_aluno(self):
         create_aluno(self.conexao, "Robertson", 41)
         create_aluno(self.conexao, "Jaqueline", 59)
         delete_aluno(self.conexao,1)
         alunos = self.conexao.execute("SELECT * FROM aluno").fetchall
         self.assertEqual(len(alunos), 1)
         self.assertEqual(alunos[0][1], "Jaqueline")
        
    
     
     
          