#EmployeeDelete.py <---module name
import pickle
def deleteemployee():
    with open("employee.txt","rb") as fp:
        records=[]
        while(True):
            try:
                record=pickle.load(fp)
                records.append(record)
            except EOFError:
                break
    #display records
    found=False
    empno=int(input("Enter The Employee Number for delete the record:"))
    for index in range(len(records)):
        if(records[index][0]==empno):
            found=True
            recindex=index
            break
    if(found):
        records.pop(recindex)
        # Place the records from main memory into the file of secondary memory
        with open("employee.txt","wb") as fp:
            for record in records:
                pickle.dump(record,fp)
        print("Employee Record deleted--verify")
    else:
        print("Employee Details does not Exist")
