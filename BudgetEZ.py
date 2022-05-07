import sqlite3

connection = sqlite3.connect('finances.db')
cursor = connection.cursor()

cursor.execute("CREATE TABLE IF NOT EXISTS income (month TEXT, pay REAL)")
cursor.execute("CREATE TABLE IF NOT EXISTS expenses (month TEXT, rent REAL, gas REAL, "
               "groceries REAL, tithing REAL, car REAL, misc REAL)")


def income():
    print(" ")
    print("Which month would you like to view?")
    print("1. January")
    print("2. February")
    print("3: March")
    print("4: April")
    print("5. May")
    month = input("> ")
    print(" ")
    if month == "1":
        print("JANUARY")
    if month == "2":
        print("FEBRUARY")
    if month == "3":
        print("MARCH")
    if month == "4":
        print("         APRIL")
        print("What would you like to do?")
        print("1. Edit Income")
        print("2. View Income")
        choice = input("> ")
        if choice == "1":
            month = "April"
            pay = float(input("Total income for April: "))
            values = (pay, month)
            cursor.execute("UPDATE income SET pay = ? WHERE month = ?", values)
            connection.commit()
        if choice == "2":
            month = "April"
            values = (month,)
            cursor.execute("SELECT * FROM income WHERE month = ?", values)
            for record in cursor.fetchmany(2):
                print("       Income")
                print(f"    {record[0]}  ${record[1]}")
                print("")
    if month == "5":
        print("         MAY")
        print("What would you like to do?")
        print("1. Edit Income")
        print("2. View Income")
        choice = input("> ")
        if choice == "1":
            month = "May"
            pay = float(input("Total income for May: "))
            values = (pay, month)
            cursor.execute("UPDATE income SET pay = ? WHERE month = ?", values)
            connection.commit()
        if choice == "2":
            month = "May"
            values = (month,)
            cursor.execute("SELECT * FROM income WHERE month = ?", values)
            for record in cursor.fetchmany(2):
                print("")
                print(f"    {record[0]}  ${record[1]}")
                print("")


def expenses():
    print(" ")
    print("Which month would you like to view?")
    print("1. January")
    print("2. February")
    print("3: March")
    print("4: April")
    print("5. May")
    month = input("> ")
    print(" ")
    if month == "1":
        print("JANUARY")
    if month == "2":
        print("FEBRUARY")
    if month == "3":
        print("MARCH")
    if month == "4":
        print("         APRIL")
        print("What would you like to do?")
        print("1. Add Expenses")
        print("2. Delete Expenses")
        print("3. View Expenses")
        choice = input("> ")
        if choice == "1":
            print("What type of expense are you adding?")
            print("         April")
            print("1. Rent \n"
                  "2. Gas \n"
                  "3. Groceries \n"
                  "4. Tithing \n"
                  "5. Car \n"
                  "6. Misc")
            choice = input("> ")
            print("")
            if choice == "1":
                rent = float(input("Amount: "))
                month = "April"
                values = (rent, month)
                cursor.execute("UPDATE expenses SET rent = ? WHERE month = ?", values)
                connection.commit()
    if month == "5":
        print("MAY")


choice = None
while choice != 3:
    print("1. Income")
    print("2. Monthly Expenses")
    print("3. Quit")
    choice = input("> ")
    print(" ")

    if choice == '1':
        income()

    if choice == '2':
        expenses()

    if choice == '3':
        break
