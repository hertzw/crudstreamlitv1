import mysql.connector
import os
from dotenv import load_dotenv

load_dotenv()  # Carrega as variáveis do arquivo .env

class repositorio():
    mydb = mysql.connector.connect(
        host=os.getenv("DB_HOST"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        database=os.getenv("DB_NAME"),
    )  # Conexão com dados do banco de dados e MySQL
    mysqlcursor = mydb.cursor()

