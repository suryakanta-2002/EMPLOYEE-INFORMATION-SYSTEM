#EmployeeSearch.py<---Module Name
import pickle
def searchemployee():
    with open("employee.txt","rb") as fp:
        records=[]   #empty list created for Holding records of file
        while (True):
            try:
                record=pickle.load(fp)
                records.append(record)
            except EOFError:
                break
    # Get emp number from user
    found=False
    empno=int(input("Enter Employee Number to search:"))
    for record in records:
        if(record[0]==empno):
            found=True
            break
    print("-"*50)
    if(found):
        print("Employee Found and valid")
    else:
        print("Employee Not Found and invalid")
    print("-"*50)


