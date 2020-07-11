from Utils import Employee
from Utils import EmployeeList
from Errors import NotInDB,InDB
from Reports import Attendance
import datetime 

a = EmployeeList()
lst = Attendance(a)
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
    #print('Starting Add unit test')
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

def tAddfromCSV(filepath):
    try:
        a.addFromCSV(filepath)
    except TypeError:
        print('addfromCSV failed, wrong file type')
    except ValueError as Val:
        print(f'addfromCSV failed with ValueError {Val}')
    except Exception as Exc:
        print(f'addFromCSV failed with exception {Exc}')
    else:
        print('addfromCSV succeeded')

def tAddfromXLSX(filepath):
    try:
        a.addFromXLSX(filepath)
    except TypeError:
        print('addfromXLSX failed, wrong file type')
    except InDB:
        print(f'addFromCSV failed with InDB error')
    except ValueError:
        print(f'addfromXLSX failed with ValueError')
    except Exception as Exc:
        print(f'addFromXLSX failed with exception {Exc}')
    else:
        print('addfromXLSX succeeded')

def tdelFromCSV(filepath):
    try:
        a.delFromCSV(filepath)
    except TypeError:
        print('delFromCSV failed, wrong file type')
    except ValueError:
        print(f'delFromCSV failed with ValueError')
    except Exception as Exc:
        print(f'delFromCSV failed with exception {Exc}')
    else:
        print('delFromCSV succeeded')

def tdelFromXLSX(filepath):
    try:
        a.delFromXLSX(filepath)
    except TypeError:
        print('delFromXLSX failed, wrong file type')
    except ValueError:
        print(f'delFromXLSX failed with ValueError')
    except Exception as Exc:
        print(f'delFromXLSX failed with exception {Exc}')
    else:
        print('delFromXLSX succeeded')

def tCreateAttList():
    try:
        lst.CreateAttList()
    except Exception as Exc:
        print(f'Attendance list creation failed with error {Exc}')
    else:
        print('Created attendance list - Success')

def tWrite(id):
    try:
        a.add(id,name,phone,age)
        a.add(id+1,name,phone,age)
        lst.Write(id)
        lst.Write(id+1)
    except NotInDB:
        print('Write to Attendance failed - ID not in database')
    except Exception as Exc:
        print(f'Write to Attendance failed with Exception: {Exc}')
    else:
        print('Write to Attendance - Success')
    try:
        lst.Write(9999)
    except NotInDB:
        print('Trying to add nonexistent ID failed - Success')

def tRepID():
    id1 = 1050
    id2 = 2050
    a.add(id1,'Natalie',2342342342,20)
    a.add(id2,'Portman',3453453453,23)
    lst.CreateAttList()
    lst.Write(id1)
    lst.Write(id2)
    lst.Write(id1)
    lst.Write(id2)
    # try:
    #     lst.RepID(id1,datetime.datetime.now().year,datetime.datetime.now().month)
    # except Exception as Exc:
    #     print(f'Finished with an exception {Exc}')
    lst.RepID(id1,datetime.datetime.now().year,datetime.datetime.now().month)
    lst.RepIDView(id1,datetime.datetime.now().year,datetime.datetime.now().month)
    #will be continued

#running the unit tests

tCreateEmployeeList()
addResult = tAdd()
for i1 in range(len(a.list)):
    print(a.list[i1].id)
if addResult:
    tDelete()
else:
    print('Delete failed, because Add failed')
    #there is no point deleting if the add did not succeed
tAddfromCSV(filepathCSV)
tdelFromCSV(filepathCSV)
tAddfromXLSX(filepathXLSX)
tdelFromXLSX(filepathXLSX)
tCreateAttList()
tWrite(id)
tRepID()
# for i1 in range(len(a.list)):
#     print(a.list[i1].id)


