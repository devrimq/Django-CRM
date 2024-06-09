import mysql.connector

# Veritabanı bağlantısı oluşturma
dataBase = mysql.connector.connect(
    host='localhost',
    user='root',
    passwd='Mirved.123'
)

# cursor obje hazırlama
cursorObject = dataBase.cursor()

# Veritabanı oluşturma
cursorObject.execute("CREATE DATABASE elderco")

print("halloldu")
