mydict={
    "Fast":"In Quick Manner",
    "Alone":"One Man Army",
    "Marks":[1,2,3,4,5],
    "anotherdict":{'Ashu':'A name'}
}


print(mydict.keys())
print(mydict.values())
print(mydict.items())
print(mydict)
updatedict={
    "Anay":"A Coder"
}
mydict.update(updatedict)
print(mydict)
print(mydict.get("Ashuu"))#Returs None Bcoz this variable is not preset in code
#print(mydict["Ashuu"]) #showing error bcoz here we not use get function