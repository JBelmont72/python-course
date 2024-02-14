'''
'CODING NEWS TODAY' channel
https://www.youtube.com/@NewsOnCoding
'''
from enum import Enum, unique, auto

class Color(Enum):
    RED = 1 
    GREEN =2
    BLUE = 3
    PURPLE = 3  # this does not register since the value is takened already
print(Color.RED)
# EXAMPLE of iteration

for c in Color:
    print(c)
for c in Color:
    print('My pants are ',c)
        
# duplicate ENUM MEMBERS  cannot use the same key in the same enum,  no two or more BLUEs

# unique ENUM iterators by using (@unique) decorators

@unique
class Department(Enum):
    Engineering = 1
    Pathology =2
    Speech =3
    
class Grade(Enum):
    A = 1
    B = 2
    C = 3
 # enum automatic values   
class Grades(Enum):
    A = auto()
    B = auto()
    C = auto()
print(list(Grades))

if Grades.A ==Grades.B:
    print('False')
    print(type(Grades.A))
else:
    print('True')
    print(type(Grades.A))
if Grades.A is Grades.B:
    print('False')
    print(type(Grades.A))
else:
    print('True')
    print(type(Grades.A))
    
# hashable and can be use d in dictionaries and sets

applies ={}
applies[Color.RED]='#29443th'
applies[Color.BLUE]= (0,0,255)
print(applies[Color.RED])
print(applies[Color.BLUE])
print(type(applies[Color.BLUE]))
    
        
    