from Utils import Employee
from Utils import EmployeeList

b = EmployeeList()
b.CreateEmployeeList()
id = 1234
name = 'Alexandra'
phone = 5846536420
age = 25
b.add(id,name,phone,age)
a = [(ind,value) for (ind,value) in enumerate(b.list) if value.id == id]
print(f'a[0][0] is {a[0][0]}')
print(f'a[0][1].id is {a[0][1].id}')