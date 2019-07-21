import random

a=random.randint(1,20)
i=0
c=(int)(input("Enter the number of guesses you want:"))
while(i<c):
    b=input("Guess a number:")
    b=(int)(b)
    if(b<a):
        print("The guess is too low")
    elif(b>a):
        print("The guess is too high")
    else:
        break
    i=i+1
    
if i==c:
    print("You Failed! The number was "+(str)(a))
    print("Come back soon.")
else:
    print("\nThe guess is correct")
    print("\nCongratulations!!!!!\n")
        