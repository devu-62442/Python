# Perfect Number
# Aliquot Sum (another name)

# -----------------------------------------------------------------------------------------------------------------------------
# A number is called perfect if it is the sum of its proper positive divisors. 
# For example, 6 is perfect, because its divisors 1,2,3 add up to 6. 
# Write a function to return True if a given number n is perfect. Otherwise return False.
# -----------------------------------------------------------------------------------------------------------------------------

# Method which determines whether the given number is a PERFECT NUMBER or NOT
def Aliquot(a):
    s=0
    for i in range(1,a):
        if(a%i==0):
            s=s+i
    if(a==s):
        print("It's the PERFECT NUMBER:"+(str)(s))
    else:
        print("Not a PERFECT NUMBER:"+(str)(a))
        
# Getting the input from the user
a=(int)(input("Enter the number to ckeck whether it is PERFECT or NOT: "))
# Calling the Method
Aliquot(a)
