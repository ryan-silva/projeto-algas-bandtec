import mysql.connector

mydb = mysql.connector.connect(
  host="52.90.170.7",
  user="root",
  password="urubu100",
  database="algas"
)

mycursor = mydb.cursor()

def insert(values):
  sql = "INSERT INTO market (cidade, produto, formaPagamento, dia, quantidade, tempo, tamanho, data) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"

  mycursor.execute(sql, values)

  mydb.commit()
  print(mycursor.rowcount, "record inserted.")

def get_values():
  sql = "SELECT * FROM market"

  mycursor.execute(sql)
  resultado = mycursor.fetchall()

  for item in resultado:
    print(item)