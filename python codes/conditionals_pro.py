m1=int(input("Enter your math Subject Mark:"))
m2=int(input("Enter your English Subject Mark:"))
m3=int(input("Enter your Marathi Subject Mark:"))

if(m1<33 or m2<33 or m3<33):
    print("You are fail,Bcoz in each subject you doen not carry 33%")

elif((m1+m2+m3/3)<40):
    print("You are fail,bcoz your marks total is not 40%")
else:
    print("Congratulations,You Are pass........")