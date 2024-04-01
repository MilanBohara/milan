"""
# stored key values

student ={
    'name':'Ram',
    'age':20,
    'address': 'Boudha'

}
print(student)

"""

capital ={
    "Nepal":"Kathmandu",
    "India":"New Delhi",
    "China":"Beijing"
}
print(capital)
print(len(capital))
print(type(capital))

print(capital.keys())        #gives list of keys in the dictionary
print(capital.values())      #gives list of values in the dictionary

print(capital["Nepal"])       #gives the values of given keys 
print(capital["India"])
print(capital["China"])

capital["Japan"] = "Tokyo"    #adds the values in the dictionary
print(capital)

capital["Bhutan"] = "Thimpu"
print(capital)

pop_element = capital.pop("Bhutan")
print(pop_element)
print(capital)

a = {1,2,3,4}
b = (1,2,3,4)

#list remaining part

c = ['a','b','c','d','e','f']
print(c.index('a'))           #gives the index number number of given data
c.sort()                      #ascending order
print(c)
c.sort(reverse=True)
marks = {
    "Math" : 80,
    "English" : 80,
    "Science" :80
}
print(marks)

capital.update(marks)   
print(capital)


copy_capital = capital.copy()
print("This is orginal list :",capital)
print("This is copy list :",copy_capital)            #copy same data from capital

capital.clear() 
print("copy list after clearing:", copy_capital)               #clear previous copy data