import random

randNumber = random.randint(1,4)
userguess = None
guesses = 0

while(userguess != randNumber):
    userguess = int(input("enter your No :"))
    guesses +=1
    
    if(userguess==randNumber):
        print(f"your guesses right No is a {userguess}")
    else:
        if(userguess>randNumber):
            print("your choise small No")
            
        else:
            
            print("your choise large No")
            
print(f"your guesses is {guesses}")

with open("h.txt","r") as f:
    hiscor = int(f.read())
    
if(guesses<hiscor):
    with open("h.txt","w") as f:
        f.write(str(guesses))

