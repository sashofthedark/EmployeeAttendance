from Errors import NotInDB,InDB
from prettytable import PrettyTable
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
        if not a.IsInList(id,self.EList.list):
            print('Employee is not in database!')
            raise NotInDB('Employee not in database')
        else:
            MatchDict = {}
            MatchDict['Year']=year
            MatchDict['Month']=month
            MatchDict['ID'] = id
            self.WriteToCSV(MatchDict,False)

    def Rep(self,year,month,OnlyLate):
        MatchDict = {}
        MatchDict['Year']=year
        MatchDict['Month']=month
        self.WriteToCSV(MatchDict,OnlyLate)

    
    def WriteToCSV(self,MatchDict,OnlyLate):
        list_path = self.CreateAttList()
        path = './'
        EmptyFlag = False
        LateHour = 17
        LateMinute = 15

        for Headers in MatchDict.values():
            path = path + str(Headers) + '_'
        if OnlyLate:
            path = path + '_late'
        path = path + '_report.csv'
        if os.path.isfile(path):
            os.remove(path)
        with open(path,'a',newline='') as writepath:
            with open(list_path,'r') as readpath:
                readfile = csv.DictReader(readpath,delimiter=',')
                headers = readfile.fieldnames
                writefile = csv.DictWriter(writepath,fieldnames = headers,delimiter=',')
                writefile.writeheader()
                rowsToFilter = readfile
                for (key,value) in MatchDict.items():
                    rowsToFilter = filter(lambda row: (row[str(key)] == str(value)),rowsToFilter)
                if OnlyLate:
                    rowsToFilter = filter(lambda row: (int(row['Hour']) > LateHour or (int(row['Hour']) == LateHour and int(row['Minute']) > LateMinute)),rowsToFilter)
                for row in rowsToFilter:
                    writefile.writerow(row)

    def ViewReport(self,MatchDict,OnlyLate):
        LateHour = 19
        LateMinute = 20
        list_path = self.CreateAttList()
        with open(list_path,'r') as readpath:
            readfile = csv.DictReader(readpath,delimiter=',')
            headers = readfile.fieldnames
            t = PrettyTable(list(headers))
            t.add_row(list(headers))
            rowsToFilter = readfile
            
            for (key,value) in MatchDict.items():
                rowsToFilter = filter(lambda row, key=key, value=value: (str(row[str(key)]) == str(value)), rowsToFilter)
            if OnlyLate:
                rowsToFilter = filter(lambda row: (int(row['Hour']) > LateHour or (int(row['Hour']) == LateHour and int(row['Minute']) > LateMinute)),rowsToFilter)
            
            for row in rowsToFilter:
                rowsToAdd = []
                for header in headers:
                    rowsToAdd.append(str(row[header]))
                t.add_row(rowsToAdd)
            print(t)

    def RepView(self,year,month,OnlyLate):
        print(f'This is an attendance report for year {year} month {month}')
        if OnlyLate:
            print('Only late employees')
        MatchDict = {}
        MatchDict['Year']=year
        MatchDict['Month']=month
        self.ViewReport(MatchDict,OnlyLate)


    def RepIDView(self,id,year,month):
        if not a.IsInList(id,self.EList.list):
            print('Employee is not in database!')
            raise NotInDB('Employee not in database')
        else:
            print(f'This is an attendance report for ID {id}')
            MatchDict = {}
            MatchDict['ID'] = id
            MatchDict['Year'] = year
            MatchDict['Month'] = month
            self.ViewReport(MatchDict,False)



                    



        



