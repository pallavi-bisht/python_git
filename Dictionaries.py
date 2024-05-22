#ry it yourself pg98
Person={
    'first_name' :'Pallavi',
    'last_name' :'Bisht',
    'age' :30,
    'city' :'Pune'
    }
print(Person['first_name'])
print(Person['last_name'])
print(Person['age'])
print(Person['city'])

#looping in Dectionaries
Person={
    'first_name' :'Pallavi',
    'last_name' :'Bisht',
    'age' :30,
    'city' :'Pune'
    }
for k,v in Person.items():#when  want to see both key and value
    print(f"{k} :{v}")
for k in Person.keys(): #when only want to see keys
    print(f"{k}")