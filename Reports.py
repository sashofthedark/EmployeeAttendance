from Errors import NotInDB,InDB
import Utils
import csv 
import os
import datetime

class Attendance():
    def __init__(self,EList):
        self.EList = EList 

    def CreateAttList(self):
        path = './Attlist.csv'
        if os.path.isfile(path):
            pass
        else:
            with open(path,'w',newline='') as writesicle:
                writefile = csv.writer(writesicle,delimiter=',')
                writefile.writerow(['ID','Year','Month','Day','Hour','Minute'])
                
        return path

    def Write(self,id):
        #EmployeeList is an Employee.list object,
        #which is a list of Employee instances
        list_path = self.CreateAttList()
        a = [(ind,value) for (ind,value) in enumerate(self.EList.list) if value.id == id]
        #checking whether the ID is in the Employee list 
        if a==[]:
            raise NotInDB('Employee is not in the database!')
        else:
            with open(list_path,'a',newline='') as OF:
                now = datetime.datetime.now()
                writefile = csv.writer(OF,delimiter=',')
                writefile.writerow([id,now.year,now.month,now.day,now.hour,now.minute])
        
    def RepID(self,id):
        #generates attendance report per ID
        pathID = './'+str(id)+'_rep.csv'
        with open(pathID,'w',newline='') as IDrep:
            #with open()
            #will be continued


        



