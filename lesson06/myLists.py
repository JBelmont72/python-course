'''
lists and tuples  with lesson 8
'''
users = []
users.append('Dave')
users.append('John')
print(users)
print(len(users))
users +=['Jason']
users.extend(['Robert','James'])
print(users)
data = ['Sara', 42, 1.44]
# users.extend(data)
# print(users)
users.insert(0,'Bob')
print(users)
# to insert , not replace a value

users[2:2]= ['Eddie','Alex']
print(users)
# to replace values
users[2:4]= ['Alex','Sam']
print(users)
# to remove 
users.remove('Bob')
# to remove last
print(users.pop())
print(users)
# to remove selectively
del users[0]
print(users)
# del data
data.clear()
print(data) #erases contents

# users[1:2]  = 'dave' #'Alex', 'd', 'a', 'v', 'e', 'John', 'Jason', 'Robert']
users[1:2 ] =['dave']       # ['Alex', 'dave', 'John', 'Jason', 'Robert']

# to sort 
users.sort()
users.sort(key =str.lower)
print('lower: ',users)
users.sort(key=str.upper)
print('upper: ',users)

nums =[4,43,78,1,55,00]
nums.reverse() # this just flips every thong around, does not sort
print(nums)     #[0, 55, 1, 78, 43, 4]
# this 'sort' function changes the list forever, not llike the 'sorted' function below
#nums.sort(reverse = True) # this sorts high to low
# print(nums)
# nums.sort(reverse = False) # this sorts low ot high
# print(nums)
# the below global sorted function only changes the list for one time.not forever.
print(sorted(nums, reverse=True))   #   [78, 55, 43, 4, 1, 0]
print(nums)         #   [0, 55, 1, 78, 43, 4] the global sorted function but original is not altered
# to make copies of list so as not to distub the orignal
numscopy = nums.copy()
myNums = list(nums)
myCopy = nums[:]
print(nums)
print(numscopy)
print(myNums)
print(myCopy)
myCopy.sort()
print(myCopy)

mylist =list([1,'Neil',True]) # this uses a 'list constructor'
print(mylist)
#TUPLES
mytuple = tuple(('Dave',42,True)) # using a 'tuple CONSTRUCTOR'
anotherTuple = (1,2,3,4,4,4,4)
print(mytuple)
print(type(mytuple))
print(anotherTuple)
# tuples cannot be changed but can be copied
# this changes a tuple by converting it to a list then then back to a tuple

newList = list(mytuple)
newList.append('Neil')
newTuple =tuple(newList)
print(newTuple)
print(type(newTuple))
#  when assign values to a tuple it is called packing a tuple
#    the reverse below is 'unpacking ' a tuplen,  notice  that they are unpaced into a list 
(one,two,*hey)= anotherTuple
print(anotherTuple)
print(one)
print(two)
print(hey)
(one,*two,hey)= anotherTuple
print(anotherTuple)
print(one)
print(two)
print(hey)
print(type(one))
print(type(two))
print(type(hey))
# if type the data type and then a period  all the methods available show up,
#    for tuple only two methods.  count(4) will count how mny fours are in the tuple
x=4
print(anotherTuple.count(x))  # could just use the number 4 etc
n=3
print(anotherTuple.index(n)) # this gives the index where the n = whatever  occurs.( can just use a number)








