# # **********Numeric data types*********

# x=100       # Integers
# print(x)
# print(type(x));

# y=19/9      #float numbers
# print(y)
# print(type(y));


# z=10+3j     #complex numbers
# print(z)
# print(type(z));


# s1 = 'Hello siri'   #String type data
# s2 = "hello siri"
# s3 = '''hello
#           siri'''
# print(s1)
# print(s2)
# print(s3)


# x=True        #Boolean
# print(x) 

# # sequence data types: List (to store ordered collection of values of any type)
# # list is mutable:can change values later.
# x = [6,8,'python',True]
# print(type(x))
# x[1] = 50
# print(x)

# #sequence data types: tuple (to store ordered collection of values of any type but it is immutable: tuple elements cannot modifiable)
# x = (6,8,'python',True)
# print(type(x))

# #sequence data types:set (to store unordered collection of values of any type, no duplicates and mutable)
# #  s = {4,7,'siri',"ravi",7.9}
# # print(s)

# set2 = set(['hi', 'mango', 67,90,'apple'])
# print(set2)
# print(type(set2))
# for ele in set2: print(ele )

# #sequence data types: dictionary(to store unordered collection of key:value pairs)
# # Accessing : can get elements by using key / get method.
# d1={'name':"siri",'place':"guntur",'age':30}
# print(type(d1))
# print(d1['name'])
# print(d1.get('age'))

# # sequence data types: range() function returns this type os data.mostly used in loops.
# # syntax:  range(start, stop, step) ==> if step not given then step value take as 1
# # x = range(5)
# # print(x)
# # for ele in x : print(x)
# # for ele in x : print(ele)

# x= range(2,9,2)
# for ele in x : print(ele)

# # sequence data types: bytes (it is immutable) numbers in the range 0-256
# b=[6,67,98,250]
# b=bytes(b)
# print(type(b))

# # sequence data types: bytearray (it is mutable)
# b=[6,67,98,250]
# byt=bytearray(b)
# print(type(byt))
# b[2]=189
# print(byt)


#addition of two numbers
# x = int(input("enter the value of x:"))
# y = int(input("enter the value of y:"))
# print(x+y)

# x=[30,10,40,20,50]
# print(x)
# print(len(x))
# print(sum(x))
# print(max(x))
# print(min(x))
# print(sorted(x))
# print(sorted(x,reverse=True))


# import math
# print(dir(math)) 
# print(math.pi)
# help(math.sqrt)
# print(math.sqrt(16))
# help(math.sinh)
# print(math.pow(10,3))



#showing map in python
# import matplotlib.pyplot as plt
# plt.plot([1,2,3],[4,7,6])   #the line comes default in staright line
# plt.plot([30,35,40,45],[40000,50000,45000,60000],"--",color="red")   #the line comes in dashes line
# plt.plot([30,35,40,45],[40000,50000,45000,60000],"oo")   #the line comes in dot line
# plt.xlabel("AGE")
# plt.ylabel("INCOME")
# plt.title("SAMPLE GRAPH")
# plt.show()

# showing 5 days activity of a person through map
import matplotlib.pyplot as plt
# import matplotlib
plt.use('TkAgg') # or 'Qt5Agg'

days = [1,2,3,4,5]
sleeping = [7,8,6,11,7]
eating =   [2,3,4,3,2]
working =  [7,8,7,2,2]
playing =  [8,5,7,8,13]
plt.stackplot(days,sleeping,eating,working,playing)# colors=['m','c','r','k'])
plt.xlabel("days")
plt.ylabel("hours")
plt.title("Interesting Graph\nCheck it out")
plt.show()

