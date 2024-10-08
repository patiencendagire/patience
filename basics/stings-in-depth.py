#strings in array like structure
#in python, arrays are lists
#example of a list in python and this is also an array
#marks=[90,30,50,40]
#In arrays, the first index must be a zero(0)
name="cathy"
print(name[0])
print(name[4])

#2 Looping through strings
#We loop through strings using a keyword "for"
#example
for character in name:
    print (character)
    
address="kamwokya"
for character in address:
    print(character)

#3 Slicing in strings
#This is the accessing of a range of character in a string
#example 
name="patience"
print(name[1:2])

# positive index slicing
# negative index slice

#-ve indexing (u index from left to right)
message="HELLO"
print(message[-1])#o
print(message[-1:-5])# space
print(message[-1:-4])# space
print(message[-5:-3])#he
print(message[-4:])
print(message[4:])

#3 f strings
# formatted strings
name="patience"
age=21
weight=74.4651
print(f" my name is {name} and am {age} years old and i weigh {weight:.2f} kilograms")

#4 string methods
#a) len()# length
name="patience"
print(len(name))
address="from  kamokya"
print(len(address))

#Escape sequences
name='patience\n Ndagire\n'
print(name)

var1=1
var2='2'
var3="3"
print(var1 + var2 + var3)

p, q, r= 10, 20 ,30
print(p, q, r)




