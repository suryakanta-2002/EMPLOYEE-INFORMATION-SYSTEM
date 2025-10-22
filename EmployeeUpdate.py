#EmployeeUpdate.py<---Module Name
import pickle
def updateemployee():
    with open("employee.txt","rb") as fp:
        records=[]
        while (True):
            try:
                record=pickle.load(fp)
                records.append(record)
            except EOFError:
                break
    # accept employee number for Updating Other details
    found=False
    empno=int(input("Enter employee number for updating the Details:"))
    for index in range(len(records)):
        if records[index][0]==empno:
            found=True
            recindex=index
            break
    # Update the records if the empno found
    if(found):
        empnewsal=float(input("Enter employee new salary:"))
        empcompname=input("Enter employee new company name:")
        records[recindex][2]=empnewsal
        records[recindex][3]=empcompname
    #Place the records from main memory into the file of secondary memory
        with open ("employee.txt","wb") as fp:
            for record in records:
                pickle.dump(record,fp)
        print("Employee Details updated--verify")
    else:
        print("Employee Details not found")



