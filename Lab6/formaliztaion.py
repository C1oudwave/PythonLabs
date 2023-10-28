import mysql.connector

# Підключення до бази даних
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="mypassword",
  database="mydatabase"  # Вибір бази даних
)

mycursor = mydb.cursor()

# Вибірка всіх орендарів, які орендують приміщення під склад. Відсортовано по назві фірми.
mycursor.execute("SELECT * FROM Tenants "
                 "INNER JOIN Rent ON Tenants.ID_rentatol = Rent.ID_rentatol "
                 "INNER JOIN Room ON Rent.ID_Room = Room.ID_Room "
                 "WHERE Rent.Purpose = 'Склад' "
                 "ORDER BY Tenants.Name")

print("Запит 1:")
for result in mycursor:
    print(result)

# Порахунок загальної орендної плати за кожне приміщення (запит з обчислювальним полем)
mycursor.execute("SELECT Room.ID_Room, SUM(Rent.ContractTerm * Room.Cost) AS Total_Rent_Price FROM Rent "
                 "INNER JOIN Room ON Rent.ID_Room = Room.ID_Room "
                 "GROUP BY Room.ID_Room")

print("Запит 2:")
for result in mycursor:
    print(result)

# Порахунок загальної площі приміщень з звичайним, поліпшеним та євро оздобленням (підсумковий запит)
mycursor.execute("SELECT Room.Formalization, SUM(Room.Square) AS Total_Square FROM Room "
                 "GROUP BY Room.Formalization")

print("Запит 3:")
for result in mycursor:
    print(result)

# Порахунок кінцевої дати дії кожного договору оренди (запит з обчислювальним полем)
mycursor.execute("SELECT Rent.ID_Rent, DATE_ADD(Rent.StartDate, INTERVAL Rent.ContractTerm DAY) AS End_Date FROM Rent")

print("Запит 4:")
for result in mycursor:
    print(result)

# Порахунок кількості приміщень, які здаються під офіс, кіоск, склад для кожного типу оздоблення (перехресний запит)
mycursor.execute("SELECT Room.Formalization, Rent.Purpose, COUNT(*) AS Room_Count FROM Room "
                 "INNER JOIN Rent ON Room.ID_Room = Rent.ID_Room "
                 "GROUP BY Room.Formalization, Rent.Purpose")

print("Запит 5:")
for result in mycursor:
    print(result)

# Відображення всіх приміщень за обраним типом оздоблення (запит з параметром)
formalization_type = 'євро'  # замініть це значення на власне
mycursor.execute("SELECT * FROM Room WHERE Room.Formalization = %s", (formalization_type,))

print("Запит 6:")
for result in mycursor:
    print(result)

# Закриття підключення
mydb.close()
