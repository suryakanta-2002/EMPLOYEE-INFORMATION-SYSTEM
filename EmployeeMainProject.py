#EmployeeMainProject.py<-----Main Project
from Empmenu import menu
from EmployeeAdd import addemployee
from EmployeeDelete import deleteemployee
from EmployeeUpdate import updateemployee
from EmployeeView import viewallemployee, viewemployee
from EmployeeSearch import searchemployee
while(True):
    try:
        menu()
        ch=int(input("Enter your choice:"))
        match(ch):
            case 1:
                addemployee()
            case 2:
                deleteemployee()
            case 3:
                updateemployee()
            case 4:
                viewemployee()
            case 5:
                viewallemployee()
            case 6:
                searchemployee()
            case 7:
                print("\tThanks for using this program")
                break
            case _:
                print("\tYour selection of operation is wrong-try again")
    except ValueError:
        print("\tDont Enter alnums,strs and Symbols for choice-try again")