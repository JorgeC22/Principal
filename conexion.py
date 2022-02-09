import mysql.connector

def conect():
    return mysql.connector.connect(
            host="localhost",
            port= 3306,
            user="root",
            passwd="281200",
            database="usuarios"
    )