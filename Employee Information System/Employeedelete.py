import pickle
def deleteemployee():
    with  open("emp1.data", "rb") as fp:
        records=[]
        while(True):
            try:
                record=pickle.load(fp)
                records.append(record)
            except EOFError:
                break
    #display records
    found=False
    empno=int(input("Enter Employee Number for Delete the Record:"))
    for index in range(len(records)):
        if(records[index][0]==empno):
            found=True
            recindex=index
            break
    if(found):
        records.pop(recindex)
        # Place the records from main memory into the file of secondary memory
        with open("emp1.data", "wb") as fp:
            for record in records:
                pickle.dump(record, fp)
        print("Employee Record deleted--verify")
    else:
        print("Employee Deatils does not Exist")