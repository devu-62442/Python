#Cows and Bulls game.

#The game is the following:
#Computer generates a random six digit number. Player is prompted to
#guess a 6 digit number. For every correct digit in the correct place, count
#one cow. For every correct digit in the wrong place, count a bull. So every
#time player enters a number, print the number of cows and bulls. If the
#number guessed is correct, congratulate the player and print how many
#guesses were used to get the correct number
print("|-------------------------------------|")
print("|-------------------------------------|")
print("|      C.O.W   A.N.D   B.U.L.L.S      |")
print("|-------------------------------------|")
print("|-------------------------------------|")

import random
d=[]
i=0
while i!=6:
    e=random.randint(1,9)
    if(e in d):
        i=i 
        continue
    else:
        d.append(e)
        i=i+1

ans=True
count3=0
while(ans):
	count=0
	count1=0
	b=(input("\nEnter a 6 digit number:"))

	c=[int(i) for i in b]
	count3=count3+1
	for i in range(0,len(d)):
		for j in range(0,len(c)):
			if(d[i]==c[j] and i==j):
				print("Correct Guess "+str(d[i])+" at "+str(i+1))
				count=count+1
			elif(d[i]==c[j] and i!=j):
				count1=count1+1
	print("COWS (Correct Guesses): "+str(count))
	print("BULLS (Correct Guess Incorrect Position): "+str(count1))
	if(count==6):
		break
	ans=input("\n\nDo you want to continue ( y or Y):")
	if(ans=="y"):
		ans==True
	else:
		ans=False
x=''.join(str(g) for g in d)      
if ans == True:
    print("You GUESSED it CORRECTLY after: "+str(count3)+" guesses")
    print("The Random number is: "+x)
    y=''.join(str(h) for h in c)
    print("Your number you guessed is: "+y) 
    print("|-------------------------------------|")
    print("|    C.O.N.G.R.A.T.U.L.A.T.I.O.N.S    |")
    print("|-------------------------------------|")
else:
    print("Your number of Guesses are: "+str(count3))
    print("The number was: "+x)


