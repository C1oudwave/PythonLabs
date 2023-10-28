import mysql.connector
import pandas as pd

# Підключення до бази даних
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="mypassword",
  database="mydatabase"
)

mycursor = mydb.cursor()

# Отримання структури та даних з таблиці Tenants
mycursor.execute("SELECT * FROM Tenants")
myresult = mycursor.fetchall()
tenants_df = pd.DataFrame(myresult, columns=[i[0] for i in mycursor.description])
print("Таблиця Tenants:")
print(tenants_df)

# Отримання структури та даних з таблиці Room
mycursor.execute("SELECT * FROM Room")
myresult = mycursor.fetchall()
room_df = pd.DataFrame(myresult, columns=[i[0] for i in mycursor.description])
print("\nТаблиця Room:")
print(room_df)

# Отримання структури та даних з таблиці Rent
mycursor.execute("SELECT * FROM Rent")
myresult = mycursor.fetchall()
rent_df = pd.DataFrame(myresult, columns=[i[0] for i in mycursor.description])
print("\nТаблиця Rent:")
print(rent_df)

# Закриття підключення
mydb.close()
