import mariadb

def conect():
    return mariadb.connect(
            host="localhost",
            port= 3307,
            user="root",
            passwd="1234",
            database="usuarios"
    )