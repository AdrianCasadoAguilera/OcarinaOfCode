import mysql.connector

connection = mysql.connector.connect(user='OcarinaOfCode',password='1234',host='127.0.0.1',database='zelda')

cur = connection.cursor()

cur.execute("SELECT count(*) FROM game;")
query = cur.fetchall()
