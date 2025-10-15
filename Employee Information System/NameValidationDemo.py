from NameExcept import InvalidNameError, SpaceError, ZeroNameLengthError
from NameValidation import validatename
while True:
    try:
        name=input("Enter the name: ")
        validname=validatename(name)
    except InvalidNameError:
        print("\t{} is not a valid name.".format(name))
    except SpaceError:
        print("\tDon't Enter space for name")
    except ZeroNameLengthError:
        print("\tTry to enter the name")
    else:
        print("\tUr Name:{}".format(validname))
        break
