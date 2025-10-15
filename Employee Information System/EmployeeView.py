import pickle
def viewemployee():
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
    empno=int(input("Enter employee number to view: "))
    for record in records:
        if(record[0]==empno):
            rec=record
            found=True
            break
    print("-"*50)
    if(found):
        print("\t\tEmployee number={}".format(rec[0]))
        print("\t\tEmployee Name={}".format(rec[1]))
        print("\t\tEmployee Salary={}".format(rec[2]))
        print("\t\tEmployee Comp Name={}".format(rec[3]))
    else:
        print("\t{} Employee number not found".format(empno))
    print("-" * 50)

def viewallemployee():
    with open("emp1.data", "rb") as fp:
        print("-"*50)
        print("\tEMPNO\t\tNAME\t\tSAL\t\t\tCOMP NAME")
        print("-" * 50)
        while (True):
            try:
                record = pickle.load(fp)
                for val in record:
                    print("\t\t{}".format(val), end=" ")
                print()
            except EOFError:
                print("-"*50)
                break
