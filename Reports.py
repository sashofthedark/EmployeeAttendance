from Errors import NotInDB
import Utils
import csv 
import os

class Attendance():
    def CreateAttList(self):
        path = './Attlist.csv'
        if os.path.isfile(path):
            pass
        else:
            with open(path,'w') as File:
                pass 



