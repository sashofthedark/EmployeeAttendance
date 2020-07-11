from Errors import NotInDB,InDB
import Utils
import csv 
import os
import datetime

a = Utils.EmployeeList()

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
        if not a.IsInList(id,self.EList.list):
            print('Employee is not in database!')
            raise NotInDB('Employee not in database')
        else:
            with open(list_path,'a',newline='') as OF:
                now = datetime.datetime.now()
                writefile = csv.writer(OF,delimiter=',')
                writefile.writerow([id,now.year,now.month,now.day,now.hour,now.minute])
        
    def RepID(self,id,year,month):
        #generates attendance report per ID
        pathID = './'+str(id)+'_'+str(year)+'_'+str(month)+'_rep.csv'
        list_path = self.CreateAttList()
        if not a.IsInList(id,self.EList.list):
            print('Employee is not in database!')
            raise NotInDB('Employee not in database')
        else:
            with open(pathID,'a',newline='') as IDrep:
                with open(list_path,'r') as List:
                    readfile = csv.DictReader(List,delimiter=',')
                    headers = readfile.fieldnames
                    writefile = csv.DictWriter(IDrep,fieldnames = headers,delimiter=',')
                    writefile.writeheader()
                    for row in readfile:
                        if row['ID'] == str(id) and row['Year'] == str(year) and row['Month'] == str(month):
                            writefile.writerow(row)

    def Rep(self,year,month,OnlyLate):
        pass

    def RepView(self,year,month,OnlyLate):
        pass


    def RepIDView(self,id,year,month):
        from prettytable import PrettyTable
        list_path = self.CreateAttList()
        if not a.IsInList(id,self.EList.list):
            print('Employee is not in database!')
            raise NotInDB('Employee not in database')
        else:
            with open(list_path,'r') as List:
                readfile = csv.DictReader(List,delimiter=',')
                headers = readfile.fieldnames
                t = PrettyTable(list(headers[1:]))
                print(f'This is an attendance report for ID {id}')
                t.add_row(['Year','Month','Day','Hour','Minute'])
                for row in readfile:
                    if row['ID'] == str(id) and row['Year'] == str(year) and row['Month'] == str(month):
                        t.add_row([row['Year'],row['Month'],row['Day'],row['Hour'],row['Minute']])
                print(t)


                    



        



