import pickle
def searchemployee():
    with open("emp1.data", "rb") as fp:
        records=[] #empty list created for Holding records of file
        while(True):
            try:
                record=pickle.load(fp)
                records.append(record)
            except EOFError:
                break
    #Get emp number from user
    found=False
    empno=int(input("Enter employee number to search: "))
    for record in records:
        if(record[0]==empno):
            found=True
            break
    print("-"*50)
    if(found):
        print("\t EMPLOYEE FOUND AND VALID")
    else:
        print("\t EMPLOYEE NOT FOUND AND IN-VALID")
    print("-" * 50)

