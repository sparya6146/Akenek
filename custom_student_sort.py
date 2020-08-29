from operator import itemgetter as i
from functools import cmp_to_key    

class Student:
    def __init__(self,name,age,marks,rollNumber):
        self.name=name
        self.age=age
        self.marks=marks
        self.rollNumber=rollNumber
    
    def getitems(self):
        return self.name,self.age,self.marks,self.rollNumber
        
    

def makeDictList(students):
    List=[]
    for student in students:
        name,age,marks,rollNumber = student.getitems()
        Student={
            'name':name,
            'age':age,
            'marks':marks,
            'rollNumber':rollNumber
        }
        List.append(Student)
    return List 

def cmp(x,y):
    return (x > y) - (x < y)

def multikeysort(items, columns):
    comparers = [
        ((i(col[1:].strip()), -1) if col.startswith('-') else (i(col.strip()), 1))
        for col in columns
    ]
    def comparer(left, right):
        comparer_iter = (
            cmp(fn(left), fn(right)) * mult
            for fn, mult in comparers
        )
        return next((result for result in comparer_iter if result), 0)
    return sorted(items, key=cmp_to_key(comparer))

def customsort(students,criteria):
    StudentList = makeDictList(students)
    return multikeysort(StudentList,criteria) 

if __name__=='__main__':
    students=[]
    s1=Student('asuraj1',23,34,2)
    s2=Student('asuraj1',24,12,1)
    s3=Student('rsuraj2',15,31,3)
    s4=Student('aasuraj3',34,24,4)
    s5=Student('csuraj5',20,39,5)
    students.extend([s1,s2,s3,s4,s5])
    print(customsort(students,['name','rollNumber']))
