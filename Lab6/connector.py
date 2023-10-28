import mysql.connector

# Підключення до бази даних
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="mypassword"
)

mycursor = mydb.cursor()

# Створення бази даних
mycursor.execute("DROP DATABASE mydatabase")
mycursor.execute("CREATE DATABASE mydatabase")

# Використання бази даних
mycursor.execute("USE mydatabase")

# Створення таблиць
mycursor.execute("CREATE TABLE Tenants ("
                 "ID_rentatol INT AUTO_INCREMENT PRIMARY KEY, "
                 "Name VARCHAR(255), "
                 "Manager VARCHAR(255), "
                 "Phone VARCHAR(255))")

mycursor.execute("CREATE TABLE Room ("
                 "ID_Room INT AUTO_INCREMENT PRIMARY KEY, "
                 "Square INT, "
                 "Cost INT, "
                 "Floor INT, "
                 "IndoorTelephone VARCHAR(255), "
                 "Formalization VARCHAR(255))")

mycursor.execute("CREATE TABLE Rent ("
                 "ID_Rent INT AUTO_INCREMENT PRIMARY KEY, "
                 "StartDate DATE, "
                 "ContractTerm INT, "
                 "Purpose VARCHAR(255), "
                 "ID_rentatol INT, "
                 "ID_Room INT)")

# Додавання первинних ключів та зв'язків
mycursor.execute("ALTER TABLE Rent ADD FOREIGN KEY (ID_rentatol) REFERENCES Tenants(ID_rentatol)")
mycursor.execute("ALTER TABLE Rent ADD FOREIGN KEY (ID_Room) REFERENCES Room(ID_Room)")

# Збереження змін
mydb.commit()

# Закриття підключення
mydb.close()
