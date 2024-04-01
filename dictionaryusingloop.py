dictionary ={}

dictionary['name']="Ram"
dictionary['age']=18
dictionary['subject']=['Math','Science','Neplai']
dictionary['education']={'School':{
    'name':'Xavier School',
    'address':'Kalopul,Kathandu'
},
'High school':{'name':'Dev collage',
               'address':'Jawlakhel,Lalitpur'},
'Bacholer level':{
    'name':'Xavier Collage',
    'address':'Boudha,Kathmandu'
    }
}
print(dictionary)

for i in dictionary.keys():
    print(i) 

for i in dictionary['subject'][0]:
    print(i, end="")

for i in dictionary['education']:
    print(i)

#accessing elements of nested dictionary from for loop
for i,j in dictionary['education']['School'].items():
    print(i, "=", j)

#dictionary  = {keys:{nestedkey:{subnestedkey:values}}}
    
print(dictionary ['education']['School']['name'])
