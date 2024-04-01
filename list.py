"""

thislist = ["Python","Java","C++"]      # order, duplicate ,changable
print(thislist)
print(len(thislist))
print(type(thislist))

"""

"""
laptops = ["dell", "hp", "sony", "lenovo", "mac"]
laptops.append("microsoft")
laptops.insert(2,"microsoft")
laptops.remove("dell")
remove_element = laptops.pop(3)
print(remove_element)
print(laptops)



a = [1,2,3,4,5]

laptops.extend(a)
print(laptops)

a.extend(laptops)
print(a)


laptops.append("microsoft")
count = laptops.count("microsoft")
count = laptops.count("hp")
print(count)
print(laptops)

copy_list = laptops.copy()
print("This is orginal list :",laptops)
print("This is copy list :",copy_list)


laptops.clear() 
print("copy list after clearing:", copy_list)




"""
number = (1, 2, 6)                 # Tuple : It can not be changed but we use indexing.
count = number.count(1)
print(len(number))
print(count)
print(number)