class Employee():
    def __init__(self,id,name,phone,age):
        self.id = id
        self.name = name
        self.phone = phone
        self.age = age

class EmployeeList():
    def CreateEmployeeList(self):
        self.list = []
             
    def add(self,id,name,phone,age):
        Added = False

        try:
            self.list
        except NameError:
            self.CreateEmployeeList()

        a = [(ind,value) for (ind,value) in enumerate(self.list) if value.id == id]
        if a!=[]:
            raise ValueError('Employee already in database!')
        elif type(id) != int or len(str(id)) != 4:
            raise ValueError('Invalid id, should be 4 digits long')
        elif type(age) != int or not (int(age) >=18 and int(age) <= 67):
            raise ValueError('Invalid age, should be between 18 and 67')
        elif type(phone) != int or len(str(phone)) != 10:
            raise ValueError('Invalid phone number, should be 10 digits long')
        else:
            self.list.append(Employee(id,name,phone,age))
            Added = True
        return Added

    def addFromFile(self,filepath):
        import csv
        import os

        Added  = False
        try:
            self.list
        except NameError:
            self.CreateEmployeeList()
        filetype = filepath[-4:]
        if filetype!='.csv' and filetype!='.xls':
            raise TypeError('Wrong file type')
        elif filetype == 'csv':
            with open(filepath) as csv_file:
                csv_reader = csv.reader(csv_file,delimiter=',')
                if os.stat(filepath).st_size == 0:
                    print('File is empty, nothing to import')
                else:
                    row_cnt = 1
                    for row in csv_reader:
                        if row[0].type !=int or len(str(row[0]))!= 4:
                            raise ValueError('Wrong ID in row' + str(row_cnt))
                        elif row[1].type !=str:
                            raise ValueError('Name is not a string in row' + str(row_cnt))
                        elif row[2].type != int or len(str(row[2]))!= 10:
                            raise ValueError('Phone invalid in row ' + str(row_cnt))
                        elif row[3].type != int or int(row[3]) < 18 or int(row[3]) > 67:
                            raise ValueError('invalid age in row ' + str(row_cnt))
                        else:
                            CurrentEmployee = Employee(row[0],row[1],row[2],row[3])
                         a = [(ind,value) for (ind,value) in enumerate(self.list) if value.id == CurrentEmployee.id]
                         #check whether the id is already in the database
                         if a!=[]:
                             raise ValueError('Employee already in database!')


            


            

        
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

