class Employee():
    def __init__(self,id,name,phone,age):
        self.id = id
        self.name = name
        self.phone = phone
        self.age = age

class EmployeeList():
    def CreateEmployeeList(self):
        try:
            self.list
        except AttributeError:
            self.list = []
    
    def check(self,id,name,phone,age):
        #does this function "see" the self.list?
        #checks whether the data for the employee is valid and he's not already in the employee list
        self.CreateEmployeeList()
        a = [(ind,value) for (ind,value) in enumerate(self.list) if value.id == id]
        if a!=[]:
            raise ValueError('Employee is already in database!')
        elif type(id) != int or len(str(id)) != 4:
            raise ValueError('Invalid ID')
        elif type(name)!=str:
            raise ValueError('Invalid name')
        elif type(phone)!=int or len(str(phone))!=10:
            raise ValueError('Invalid phone number')
        elif type(age)!=int or int(age)<18 or int(age)>67:
            raise ValueError('Invalid age')
        else:
            return True
       
    def add(self,id,name,phone,age):
        self.CreateEmployeeList()
        try:
            self.check(id,name,phone,age)
        except ValueError as ValErr:
            print(f'Error message was {ValErr}')
            return False
        else:
            self.list.append(Employee(id,name,phone,age))
            return True

    def addFromFile(self,filepath):
        import csv
        import os
        import openpyxl

        Added  = False
        self.CreateEmployeeList()

        if filepath[-4:]!='.csv' and filepath[-5:]!='.xlsx':
            raise TypeError('Wrong file type')
        elif filepath[-4:] == '.csv':
            with open(filepath) as csv_file:
                csv_reader = csv.reader(csv_file,delimiter=',')
                if os.stat(filepath).st_size == 0:
                    print('File is empty, nothing to import')
                else:
                    row_cnt = 1
                    for row in csv_reader:
                        try:
                            self.check(row[0],row[1],row[2],row[3])
                        except NameError as NamErr:
                            print('Error message is {}'.format(NamErr) + ' in row ' + str(row_cnt))
                        else:
                            add(self,row[0],row[1],row[2],row[3])
        elif filepath[-5:] == '.xlsx':
            wb_obj = openpyxl.load_workbook(filepath)
            sheet_obj = wb_obj.active 
            for rows in range(0,sheet_obj.max_row-1):
                idc = sheet_obj.cell(row = rows,column = 0)
                name = str(sheet_obj.cell(row = rows,column = 1))
                phone = sheet_obj.cell(row = rows,column = 2)
                age = sheet_obj.cell(row = rows,column = 3)
                try:
                    self.check(idc,name,phone,age)
                except Exception:
                    pass
                #I will write something here
       
    def delete(self,employeeID):
        Deleted = False
        if type(employeeID)!= int or len(str(employeeID))!=4:
            raise ValueError('Invalid id, should be 4 digits long')
        else:
            a = [(ind,value) for (ind,value) in enumerate(self.list) if value.id == employeeID]

            if len(a) == 0:
                raise ValueError('ID doesn\'t exist')
            else:
                del(self.list[a[0][0]])
                Deleted = True
        return Deleted 
        #we return a binary value telling the user whether the employee was removed from the database

