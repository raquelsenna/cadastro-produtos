from dotenv import load_dotenv
import mysql.connector
import os


load_dotenv(dotenv_path='C:/Users/raque/OneDrive/Área de Trabalho/Documentos/projetos-python/cadastro-produtos/keys.env')

#dados para conexão com bando de dados
mydb = mysql.connector.connect(
  host=os.getenv("DB_HOST"),
  user=os.getenv("DB_USER"),
  password=os.getenv("DB_PASSWORD"),
  database=os.getenv("DB_NAME")
  )

#canal de envio de comandos sql para o mysql e receber resultados
cursor = mydb.cursor()

print("\n---Inserir Produtos---\n")
nome = input("Nome do produto: ")
valor = float(input("Valor do produto: R$"))
quantidade = int(input("Quantidades vendida: "))

#querry responsável por inserir os dados na tabela
inserir_dados = "INSERT INTO vendas (nome, valor, quantidade) VALUES (%s, %s, %s)"

cursor.execute(inserir_dados, (nome, valor, quantidade))

mydb.commit()

print("\nProduto inserido com sucesso!\n")
#libera o cursor e db
cursor.close()
mydb.close()