'''
myLoops.py

'''
value = 1
while value <11:
    print(value)
    if value ==5:
        break
    value += 1

value = 1
while value <11:
    value += 1
    if value ==5:
        continue
    else:
        print('value is now equal to: ',value)
    
names = ['Dave','Sara','John'] 

for x in names:
    if x =='Sara':
        break
    print(x)  
for x in names:
    if x =='Sara':
        continue
    print(x)  