from EmpMenu import menu
from EmployeeAdd import addemployee
from EmployeeSearch import searchemployee
from EmployeeUpdate import updateemployee
from EmployeeView import viewemployee,viewallemployee
from Employeedelete import deleteemployee

while(True):
    try:
        menu()
        ch=int(input("Enter your choice: "))
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
                print("--------------Thanks for using------------")
            case _:
                print("Invalid choice-------Try again")
    except ValueError:
        print("\tDont Enter Alnum,str and symbols for choice")

