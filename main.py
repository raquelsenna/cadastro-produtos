from dotenv import load_dotenv
import mysql.connector
import os


def carregar_dotenv():
  load_dotenv(dotenv_path='C:/Users/raque/OneDrive/Área de Trabalho/Documentos/projetos-python/cadastro-produtos/keys.env')


def conexao_bd():
  #dados para conexão com bando de dados
  mydb = mysql.connector.connect(  
    host=os.getenv("DB_HOST"),
    user=os.getenv("DB_USER"),
    password=os.getenv("DB_PASSWORD"),
    database=os.getenv("DB_NAME")
    )
  
  #canal de envio de comandos sql para o mysql e receber resultados
  cursor = mydb.cursor()
  return mydb, cursor


def produto(mydb, cursor):
  print("\n---Inserir Produtos---")

  while True:
    nome = input("\nNome do produto: ")
    valor = float(input("Valor do produto: R$"))
    quantidade = int(input("Quantidades vendida: "))

    cadastro_produtos(cursor, nome, valor, quantidade)
    mydb.commit()

    print("Produto inserido com sucesso!\n")

    resp = input("\nDeseja cadastrar outro produto? [S/N] ")
    
    if resp in "Nn":
      print("\nFim do cadastro de produtos!\n")
      break

  return nome, valor, quantidade


def cadastro_produtos(cursor, nome, valor, quantidade):
  #querry responsável por inserir os dados na tabela
  inserir_dados = "INSERT INTO vendas (nome, valor, quantidade) VALUES (%s, %s, %s)"

  cursor.execute(inserir_dados, (nome, valor, quantidade))
  

def main():
  carregar_dotenv()
  mydb, cursor = conexao_bd()
  produto(mydb, cursor)
  cursor.close()
  mydb.close()

main()
