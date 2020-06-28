from Utils import Employee
from Utils import EmployeeList

a = EmployeeList()
id = 1234
name = 'Alexandra'
phone = 5846536420
age = 25
filepathCSV = 'Employees.csv'
filepathXLSX = 'Employees.xlsx'

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

def tAddfromcsv(filepath):
    try:
        a.addFromCSV(filepath)
    except TypeError:
        print('addfromCSV failed, wrong file type')
    except ValueError:
        print(f'addfromCSV failed with ValueError')
    except Exception as Exc:
        print(f'addFromCSV failed with exception {Exc}')
    else:
        print('addfromCSV succeeded')

def tAddfromxlsx(filepath):
    try:
        a.addFromXLSX(filepath)
    except TypeError:
        print('addfromXLSX failed, wrong file type')
    except ValueError:
        print(f'addfromXLSX failed with ValueError')
    except Exception as Exc:
        print(f'addFromXLSX failed with exception {Exc}')
    else:
        print('addfromXLSX succeeded')

#running the unit tests
tCreateEmployeeList()
addResult = tAdd()
if addResult:
    tDelete()
    #there is no point deleting if the add did not succeed
tAddfromcsv(filepathCSV)
tAddfromxlsx(filepathXLSX)
# for i1 in range(len(a.list)):
#     print(a.list[i1].id)

