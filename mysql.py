import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="urubu100",
  database="banco_algas"
)
print(mydb)

mycursor = mydb.cursor()

def insert(values):
  sql = "INSERT INTO algas (agTempo, agEspaco, agData) VALUES (%s, %s, %s)"

  mycursor.execute(sql, values)

  mydb.commit()
  print(mycursor.rowcount, "record inserted.")