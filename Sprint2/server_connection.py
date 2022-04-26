import mysql.connector

mydb = mysql.connector.connect(
  host="localhost:3306",
  user="root",
  password="urubu100",
  database="algas"
)

mycursor = mydb.cursor()

def insert(values):
  sql = "INSERT INTO market (cidade, produto, formaPagamento, dia, quantidade, tempo, tamanho) VALUES (%s, %s, %s, %s, %s, %s, %s)"

  mycursor.execute(sql, values)

  mydb.commit()
  print(mycursor.rowcount, "record inserted.")