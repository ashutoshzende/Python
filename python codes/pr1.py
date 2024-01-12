mydict={
    "Apna":"Aapla",
    "Bahar":"Get Out",
    "Sorry": "Maph Kra",
    "Khatm TaTa Bye Bye":"chala jya "
}

print("Options Are",mydict.keys())
a=input("Enter the Hindi Words:")
#print("The Meaning Of this words is:",mydict[a])# when we type unknown word it shows error
print("The Meaning Of this words is:",mydict.get(a))