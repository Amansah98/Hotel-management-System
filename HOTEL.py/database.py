import mysql.connector

HOST="localhost"
USER="root"
PASSWORD="amansah"
DATABASE="hotel"

def get_database():
    try:
        database = mysql.connector.connect(host=HOST,user=USER,password=PASSWORD,database="DATABASE")
        cursor=database.cursor(dictionary=True)
        return database,cursor

    except mysql.connector.Error:
        return None,None
