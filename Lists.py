abc=[1,2,3,"sing"]
print(abc)
print(abc[1])
print(abc[-1])

#add
abc.append('pallavi')
print(abc)

#delete  by position
abc=[1,2,3,"sing"]
pop_abc=abc.pop(0)
print(f"{abc} {pop_abc}")

#delete by value
abc=[1,2,3,"sing"]
abc.remove("sing")
print(abc)

#sort method ,sorted function,reverse method

abc=[2,4,1,7]
abc.sort()
print(abc)
klm=[8,33,45,2]
print(sorted(klm))
abc=[2,4,1,7]
abc.reverse()
print(abc)





