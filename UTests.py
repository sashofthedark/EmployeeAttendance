from Utils import Employee
from Utils import EmployeeList

a = EmployeeList()
id = 1234
name = 'Alexandra'
phone = 5846536420
age = 25

def tCreateEmployeeList():
    a.CreateEmployeeList()
    try:
        a.list
    except AttributeError:
        print('CreateEmployeeList failed')
    else:
        print('CreateEmployeeList succeeded')

def tAdd():
    print('Starting Add unit test')
    b = a.add(id,name,phone,age)
    if b and id == a.list[-1].id:
        print('Add succeeded')
    else:
        print('Add failed')
        return False
    print('Trying to add an existing ID')
    c = a.add(id,name,phone,age)
    if not c:
        print('Could not add again - SUCCESS')
        return True
    else:
        print('It let us add an existing ID')
        return False

def tDelete():
    d = a.delete(id)
    if d:
        print('Deletion successful')
    else:
        print('Deletion unsuccessful')


#running the unit tests
tCreateEmployeeList()
addResult = tAdd()
if addResult:
    tDelete()
    #there is no point deleting if the add did not succeed

