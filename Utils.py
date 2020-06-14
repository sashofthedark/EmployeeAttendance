class Employee():
    def __init__(self,id,name,phone,age):
        self.id = id
        self.name = name
        self.phone = phone
        self.age = age

class EmployeeList():
    def CreateEmployeeList(self):
        self.list = []
             
    def add(self,employee):
        Added = False
        a = [(ind,value) for (ind,value) in enumerate(self.list) if value.id == employee.id]
        if a!=[]:
            raise ValueError('Employee already in database!')
        elif type(employee.id) != int or len(employee.id) != 4:
            raise ValueError('Invalid id, should be 4 digits long')
        elif type(employee.age) != int or (employee.age >=18 and employee.age <= 67):
            raise ValueError('Invalid age, should be between 18 and 67')
        elif type(employee.phone) != int or len(employee.phone) != 10:
            raise ValueError('Invalid phone number, should be 10 digits long')
        else:
            self.list.append(employee)
            Added = True
        return Added
