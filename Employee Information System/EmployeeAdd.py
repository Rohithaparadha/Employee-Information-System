#EmployeeAdd.py<---Module Name
import pickle
from NameValidation import validatename
from NameExcept import ZeroNameLengthError, SpaceError,InvalidNameError
def addemployee():
    with open("emp1.data", "ab") as fp:
        while (True):
            try:
                print("-" * 50)
                empno = int(input("\tEnter Employee Number:"))
                name = input("\tEnter Employee Name:")
                empname=validatename(name)
                empsal = float(input("\tEnter Employee Salary:"))
                comp= input("\tEnter Employee Company Name:")
                empcomp=validatename(comp)
                print("-" * 50)
                lst = list()  # Create empty list for adding employee values
                # append emp values to lst object
                lst.append(empno)
                lst.append(empname)
                lst.append(empsal)
                lst.append(empcomp)
                # Save the Iterable object content to the file
                pickle.dump(lst, fp)
                print("\tEmployee Data Saved as Record in File Sucessfully")
                print("-" * 50)
                ch = input("\tDo u want to enter another employee details(yes/no):")
                if (ch.lower() == "no"):
                    break
                print("-" * 50)
            except ValueError:
                print("\tDon't enter alnums,strs and symbols for empno andd salary")
            except SpaceError:
                print("\tDON'T ENTER SPACE FOR UR NAME-Try Again")
            except ZeroNameLengthError:
                print("\tENTER FOR UR NAME-Try Again")
            except InvalidNameError:
                print("\tInvalid Emp Name/ Comp Name-Try again")
