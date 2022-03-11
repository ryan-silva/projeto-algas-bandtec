import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="python",
  password="Conectar",
  database="python"
)
print(mydb)

mycursor = mydb.cursor()

def insert(values):
  sql = "INSERT INTO algas (agTempo, agEspaco) VALUES (%s, %s)"

  mycursor.execute(sql, values)

  mydb.commit()
  print(mycursor.rowcount, "record inserted.")