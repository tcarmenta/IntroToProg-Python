# ------------------------------------------------------------------------ #
# Title: Assignment 05
# Description: Working with Dictionaries and Files
#              When the program starts, load each "row" of data
#              in "ToDoList.txt" into a python Dictionary.
#              Add each dictionary "row" to a python list "table"
# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created started script
# TArmenta,4.10.2023,Added code to complete assignment 5
# ------------------------------------------------------------------------ #
import csv

# -- Data -- #
# declare variables and constants
objFile = "ToDoList.txt" # An object that represents a file
strData = ""  # A row of text data from the file
dicRow = {}    # A row of data separated into elements of a dictionary {Task,Priority}
lstTable = [] # A list that acts as a 'table' of rows
strMenu = ""   # A menu of user options
strChoice = "" # A Capture the user option selection


# -- Processing -- #
# Step 1 - When the program starts, load the any data you have
# in a text file called ToDoList.txt into a python list of dictionaries rows (like Lab 5-2)
# TODO: Add Code Here
try:
    objFile = open("ToDoList.txt", "r")
    for row in objFile:
        lstRow = row.split(",") # Returns a list
        dicRow = {"Task": lstRow[0], "Priority": lstRow[1].strip()}
        lstTable.append(dicRow)
    objFile.close()
except IOError:  # If an error occurs during the "try" script, this will run
    print()
    print("List empty, enter 2 to add item:")


# -- Input/Output -- #
# Step 2 - Display a menu of choices to the user
while True:
    print("""
    Menu of Options
    1) Show current data
    2) Add a new item
    3) Remove an existing item
    4) Save Data to File
    5) Exit Program
    """)
    strChoice = str(input("Which option would you like to perform? [1 to 5] - "))
    print()  # adding a new line for looks

    # Step 3 - Show the current items in the table
    if (strChoice.strip() == '1'):
        # TODO: Add Code Here
        try:
            objFile = open("ToDoList.txt", "r")
            for row in objFile:
                lstRow = row.split(",")  # Returns a list
                dicRow = {"Task": lstRow[0], "Priority": lstRow[1].strip()}
            objFile.close()
            print("Current Items:")
            for row in lstTable:
                print(row)
        except IOError:  # If an error occurs during the "try" script, this will run
            print("List empty, enter 2 to add item:")

    # Step 4 - Add a new item to the list/Table
    elif (strChoice.strip() == '2'):
        # TODO: Add Code Here
        objFile = open("TodoList.txt", "w")
        strTask = str(input("Enter Task: "))
        strPriority = str(input("Enter Priority: "))
        strData = (strTask + "," + strPriority + "\n")
        dicRow = {"Task": strTask, "Priority": strPriority.strip()}
        lstTable.append(dicRow)
        objFile.close()
        continue

    # Step 5 - Remove a new item from the list/Table
    elif (strChoice.strip() == '3'):
        # TODO: Add Code Here
        strInput = str(input("Enter Item to Remove: "))
        for item in range(len(lstTable)-1, -1, -1):
            if lstTable[item]['Task'] == strInput:
                lstTable.pop(item)
        print()
        print(strInput + " " + "Removed!")
        continue


    # Step 6 - Save tasks to the ToDoToDoList.txt file
    elif (strChoice.strip() == '4'):
        # TODO: Add Code Here
        objFile = open("ToDoList.txt", "w")
        for dicRow in lstTable:
            lstNew = list(dicRow.values())
            objFile.write(lstNew[0] + "," + lstNew[1] + "\n")
        objFile.close()
        print("File Saved!")
        continue

    # Step 7 - Exit program
    elif (strChoice.strip() == '5'):
        # TODO: Add Code Here
        strExit = str(input("Did you Save, Do you want to Exit? (y/n): ")).lower()
        if strExit == "n":
            continue
        elif strExit == 'y':
            break  # and Exit the program
        else:
            print("\nError, invalid input!")
            continue
    else:
        continue

