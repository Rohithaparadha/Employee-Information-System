import pickle
from NameValidation import validatename

def updateemployee():
    with open("emp1.data","rb") as fp:
        records=[]
        while True:
            try:
                record=pickle.load(fp)
                records.append(record)
            except EOFError:
                break
    #accept employee number for updating the details
    found=False
    empno=int(input("Enter the Employee Number for updating details: "))
    for index in range(len(record)):
        if records[index][0]==empno:
            recindex =index
            found=True
            break
    #update the details if the employeenumber found
    if found:
        empnewsal=float(input("Enter the Employee New Salary : "))
        companyname=input("Enter the Employee New Company : ")
        empcompname=validatename(companyname)
        records[recindex][2]=empnewsal
        records[recindex][3]=empcompname
    #place the record from main memory into file of secondary memory
        with open("empdata.data","wb") as fp:
            for record in records:
                pickle.dump(record,fp)
        print("Employee details updated successfully-----verify")
    else:
        print("Employee details not found")





