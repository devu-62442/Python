# Guessing Game
# Your program chooses a random number between 1 and 100 (say r). 
# Then the player is prompted to guess a number between 1 and 100 (say g). 
# If g is less than r, then the program prints “The guess is too low”. 
# if g is greater than r, then it prints “The guess is too high”. 
# Otherwise, the program prints “The guess is correct” and exits.
# --------------------------------------------------------------------------------------------------------------------------
import random

a=random.randint(1,100)
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
        
