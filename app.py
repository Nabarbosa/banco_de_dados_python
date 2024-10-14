import os
from sqlalchemy import create_engine, Column, String, Integer
from sqlalchemy.orm import sessionmaker, declarative_base

# Criando banco de dados.
MEU_BANCO_ALUNO = create_engine("sqlite:///meubancoaluno.db")

# Criando conexão com banco de dados.
session = sessionmaker(bind=MEU_BANCO_ALUNO)
session = session()

# Criando tabela.

Base = declarative_base()

class Aluno(Base):
    __tablename__ = "Alunos"

    # Definindo campos da tabela.
    ra = Column("R.A.", Integer, primary_key=True, autoincrement=True)
    nome = Column("nome", String)
    sobrenome = Column("Sobrenome", String)
    email = Column("e-mail", String)
    senha = Column("senha", String)

    # Definindo atributos da classe.
    def __init__(self, ra: int, nome: str, sobrenome: str, email: str, senha: str):
        self.ra = ra
        self.nome = nome
        self.sobrenome = sobrenome
        self.email = email
        self.senha = senha

# Criando tabelas no banco de dados.
Base.metadata.create_all(bind=MEU_BANCO_ALUNO)

# CRUD.
# Creat - Insert - Salvar.

os.system("cls || clear")
print("Solicitando dados para o aluno. ")
inserir_ra =  input("Digite seu RA: ")
inserir_nome =  input("Digite seu nome: ")
inserir_sobrenome =  input("Digite seu sobrenome: ")
inserir_email =  input("Digite seu e-mail: ")
inserir_senha =  input("Digite seu senha: ")

aluno = Aluno(ra= inserir_ra, nome=inserir_nome, sobrenome=inserir_sobrenome, email=inserir_email, senha=inserir_senha)
session.add(aluno)
session.commit()

# Read - Select - Consulta
print("\nExibindo dados de todos os Alunos na tabela.")
lista_alunos = session.query(Aluno).all()

for aluno in lista_alunos:
    print(f"{aluno.ra} - {aluno.nome} - {aluno.sobrenome} - {aluno.email} - {aluno.senha}")

# U - Update - UPDATE - Atualizar
print("\nAtualizando dados do aluno.")
ra_aluno = input("Digite o RA do aluno que será atualizado: ")

aluno = session.query(Aluno).filter_by(ra = ra_aluno).first()

if aluno:
    aluno.ra = input("Digite seu RA: ")
    aluno.nome = input("Digite seu nome: ")
    aluno.sobrenome = input("Digite seu sobrenome: ")
    aluno.email = input("Digite seu e-mail: ")
    aluno.senha = input("Digite sua senha: ")

    session.commit
else: 
    print("Aluno não encontrado. ")

# Read - Select - Consulta
print("\nExibindo dados de todos os Alunos na tabela.")
lista_alunos = session.query(Aluno).all()

for aluno in lista_alunos:
    print(f"{aluno.ra} - {aluno.nome} - {aluno.sobrenome} - {aluno.email} - {aluno.senha}")

# D - Delete - DELETE -  Excluir
print("\nExcluindo os dados de um aluno.")
ra_aluno = input("Digite o RA do aluno que será excluido: ")

aluno = session.query(Aluno).filter_by(ra = ra_aluno).first()

if aluno:
    session.delete(aluno)
    session.commit()
    print(f"Aluno {aluno.nome} excluido com sucesso!")
else:
    print("Aluno não encontrado.")

# Read - Select - Consulta
print("\nExibindo dados de todos os Alunos na tabela.")
lista_alunos = session.query(Aluno).all()

for aluno in lista_alunos:
    print(f"{aluno.ra} - {aluno.nome} - {aluno.sobrenome} - {aluno.email} - {aluno.senha}")

# R - Read - SELECT - Consulta
print("Consultando os dados de apenas um aluno.")
ra_aluno = input("Digite o RA do aluno: ")

aluno = session.query(Aluno).filter_by(ra = ra_aluno).first()

if aluno:
    print(f"{aluno.ra} - {aluno.nome} - {aluno.sobrenome} - {aluno.email} - {aluno.senha}")
else:
    print("Aluno não encontrado.")

# Fechando conexão.
session.close()

