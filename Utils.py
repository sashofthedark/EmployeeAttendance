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
        a = [(ind,value) for (ind,value) in enumerate(self.list) if value.id == id]
        if a!=[]:
            raise ValueError('Employee already in database!')
        elif type(id) != int or len(str(id)) != 4:
            raise ValueError('Invalid id, should be 4 digits long')
        elif type(age) != int or (age >=18 and age <= 67):
            raise ValueError('Invalid age, should be between 18 and 67')
        elif type(phone) != int or len(str(phone)) != 10:
            raise ValueError('Invalid phone number, should be 10 digits long')
        else:
            self.list.append(Employee(id,name,phone,age))
            Added = True
        return Added
        
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
