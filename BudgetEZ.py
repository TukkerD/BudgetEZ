"""
BudgetEZ income and expenses tracker!

This is a program that utilizes SQLite to track expenses and income.

Author: Tukker De Hart
"""
import sqlite3

# This is the SQLite database we are using
connection = sqlite3.connect('finances.db')
cursor = connection.cursor()

# Created two tables, expenses and income
cursor.execute("CREATE TABLE IF NOT EXISTS income (month TEXT, pay REAL)")
cursor.execute("CREATE TABLE IF NOT EXISTS expenses (month TEXT, rent REAL, gas REAL, "
               "groceries REAL, tithing REAL, car REAL, misc REAL)")


def income():
    """
    This function allows the user to access/edit their income on the income SQLite database table.
    :return:
    """
    print(" ")
    print("Which month would you like to view?")
    print("1. January")
    print("2. February")
    print("3: March")
    print("4: April")
    print("5. May")
    month = input("> ")
    print(" ")
    # The user can view each monthly totals. For now only April and May are functional.
    if month == "1":
        print("JANUARY")
    if month == "2":
        print("FEBRUARY")
    if month == "3":
        print("MARCH")
    if month == "4":
        # If the user selects April they will be asked if they want to edit or view
        print("         APRIL")
        print("What would you like to do?")
        print("1. Edit Income")
        print("2. View Income")
        choice = input("> ")
        if choice == "1":
            # If they edit then we code in SQLite to update the pay portion of the table.
            month = "April"
            pay = float(input("Total income for April: "))
            values = (pay, month)
            cursor.execute("UPDATE income SET pay = ? WHERE month = ?", values)
            connection.commit()
        if choice == "2":
            # If they view we simply select all the data in SQLite for the month of April and print it in python.
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
    """
    The expenses tab allows the user to track spending and to edit spending into 6 categories:
    Rent, Gas, Groceries, Tithing, Car (payments), and Misc.
    :return:
    """
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
        print("2. Edit Expenses")
        print("3. View Expenses")
        choice = input("> ")
        if choice == "1":
            # We ask the user the type so we can change the right section of the table.
            print("What type of expense are you adding?")
            print("         April")
            print("Rent \n"
                  "Gas \n"
                  "Groceries \n"
                  "Tithing \n"
                  "Car \n"
                  "Misc")
            choice = input("> ")
            print("")
            rent = float(input("Amount: "))
            month = "April"
            values = (rent, month)
            # Here we use a little python knowledge to just plug in the users choice into the SQLite code.
            cursor.execute(f"UPDATE expenses SET {choice} = ? WHERE month = ?", values)
            connection.commit()
        if choice == "2":
            # Just like above instead of adding we ask what they want to change from the category.
            print("What expense would you like to edit?")
            month = "April"
            values = (month,)
            cursor.execute("SELECT * FROM expenses WHERE month = ?", values)
            connection.commit()

            for record in cursor.fetchall():
                print("           Rent    Gas   Groceries  Tithing  Car    Misc                           ")
                print(f"    {record[0]}  ${record[1]}  ${record[2]}  ${record[3]}       ${record[4]}"
                      f"     ${record[5]}   ${record[6]}")
                print("")
            category = input("Category?: ")
            amount = float(input("Amount?: "))
            values = (amount, month)
            cursor.execute(f"UPDATE expenses SET {category} = ? WHERE month = ?", values)
            connection.commit()
        if choice == "3":
            month = "April"
            values = (month,)
            cursor.execute("SELECT * FROM expenses WHERE month = ?", values)
            connection.commit()

            for record in cursor.fetchall():
                print("           Rent    Gas   Groceries  Tithing  Car    Misc                           ")
                print(f"    {record[0]}  ${record[1]}  ${record[2]}  ${record[3]}       ${record[4]}"
                      f"     ${record[5]}   ${record[6]}")
                print("")

    if month == "5":
        print("MAY")


choice = None
while choice != 3:
    # If the user doesn't want to quit then keep asking!
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
