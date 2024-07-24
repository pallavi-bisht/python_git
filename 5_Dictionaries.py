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

#TIY  104
glossary ={
    "ganga":"India",
    "Nile":"Egypt",
        "godavari":"India",
    "yamuna":"India"
}  

for k,v in glossary.items():
    print(f" The {k.title()} runs through {v}.\n")
for k in glossary.keys():
    print(k)
for v in set(glossary.values()): #to get unique values
    print(v)

favorite_languages = {
      'jen': 'python',
      'sarah': 'c',
      'edward': 'rust',
      'phil': 'python',
      }
new_user=['pallavi','jen','karan']

for i in new_user:
    if i in favorite_languages.keys():
     print(f"{i} Thanks you for participating in poll!")
    else:
     print(f"{i} Please participate in poll !")    

 #TIY 111
Person1={
    'first_name' :'Pallavi',
    'last_name' :'Bisht',
    'age' :30,
    'city' :'Pune'
    } 
Person2={
    'first_name' :'Varun',
    'last_name' :'Bisht',
    'age' :20,
    'city' :'Nagpur'
    } 
Person3={
    'first_name' :'Shweta',
    'last_name' :'Bisht',
    'age' :29,
    'city' :'Delhi'
    }  

people=[Person1,Person2,Person3]
for i in people:
   print(i)


places={
   'karan':['India','Switzerland'],
   'pallavi':['Vietnam','Switzerland']
}

for i,j in places.items():
   print(f"{i} favourite places are:")
   for l in j:
      print(l)

cities={
   "Pune":
   {   "Country" :'India',
      "Population": 20000,
      "fact": "Very beautiful"
   },
   "Delhi":
   {   
      "Country" :'India',
      "Population": 300000,
      "fact": "Very poluted"
   },
   "Mumbai":
   {
      "Country" :'India',
      "Population": 25000,
      "fact": "Very fast"
   }
}      

for i,j in cities.items():
    print(f"City :{i} have ")    
    for k,l in  j.items():
     print(f"{k} :{l}")