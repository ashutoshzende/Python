text=input("Enter the text: \n")
if("make alot of money" in text):
    spam=True
elif("Subscribe this" in text):
    spam=True
elif("click this" in text):
    spam=True
elif("buy now" in text):
    spam=True
else:
    spam=False
if(spam):
    print("This is a spam, so aware it......")
else:
    print("This not a spam,You are safe.........")
