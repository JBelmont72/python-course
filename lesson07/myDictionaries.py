''' lesson 8, my Dictionaries

look like javscript objects a lot
'''

band = {
    'vocals':'Plant',
    'guitar': 'Page'
}

band2 = dict(vocals= 'Plant',guitar = 'Page')
print(band)
print(band2)
print(type(band))
print(len(band))
# Access items.  Here we  enter the key and get the value

print(band['vocals'])
print(band.get('guitar'))
# list all keys
print(band.keys())
# list all values
print(band.values())
# list of key/value tuples
print(band.items())   #  dict_items([('vocals', 'Plant'), ('guitar', 'Page')])
# verify if a key exists
print('guitar' in band)
print('circle' in band)

# change values
band['guitar']='Coverdale'      #   dict_items([('vocals', 'Plant'), ('guitar', 'Coverdale')])
print(band.items())
band.update({'bass':'JPJ'})     # note need dictionary style {}
# this adds a tuple to the dictionary
print(band)     #   {'vocals': 'Plant', 'guitar': 'Coverdale', 'bass': 'JPJ'}
# Remove items
print(band.pop('bass'))  #  returns JPJ
print(band) #    shows that the key:value pair deleted   {'vocals': 'Plant', 'guitar': 'Coverdale'}

print(band.popitem())  #tuple  removes the last keyvalue pair ('guitar', 'Coverdale')

# delete and clear  
band['drums']= 'Bonham'
band['guitar']= 'Coverdale'
print(band)
del band['drums']
print(band)
band2.clear()
print(band2)
del band2
# print(band2)  # deletes the whole dictionary, returns a traceback

# COPY DICTIONARIES
# HOW not to COPU dictionary
# band2 = band   # createsa reference in memory but not a new band2
# print('bad copy')
# print(band2)
# print(band)

# band2['drums']= ('Dave')
# print('band dictionary is: ',band) # problem is a change in band2 will alter band so is a "no/No'"
#RIGHT way to copu a dictionary

band2 = band.copy()
band2['Drums']=('Dave')
print(band)
print(band2)
# can also use a ' dictionary constructor function'
band3 = dict(band) #good way to copy a dictionary
print(band3)  
# NESTED DICtionaries  

member1 = {
    'name':'Plant',
    'instrument':'vocals',
    'manager':'Rolling Stone'
}
member2 = {
    'name':'Page',
    'instrument':'guitar'
}
member3 = {
    'name':'Coverdale',
    'instrument':'drums'
}
member4 = {}

band = {
    'member1':member1,
    'member2 ':member2,
    'member3':member3,
    'member4':member4
    
}

print(band)
band = {
    'memberUNO':member1,
    'member2 ':member2,
    'member3':member3,
    'member4':member4
    
}
print(band)