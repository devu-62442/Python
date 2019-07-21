# Addition and Multiplication Persistence
# The multiplicative persistence of a positive integer is the number of steps 
# required to get a one digit number when separating the digits and multiplying them together. 
# The persistence of a one digit number is zero. 
# For example, the persistence of 39 is 3 because 39 → 27 → 14 → 4. Write a function to compute the persistence of an integer.


def add(a):
    d=(int)(a)
    count=0
    while(d>=10):
        s=0
        count+=1
        while(d!=0):
            r=d%10
            s=s+r
            d=(int)(d/10)
        d=s
    return count

def mul(a):
    d=(int)(a)
    count=0
    while(d>=10):
        s=1
        count+=1
        while(d!=0):
            r=d%10
            s=s*r
            d=(int)(d/10)
        d=s
    return count

a=input("Enter a number:")
print("Addition Persistence:"+(str)(add(a)))
print("Multiplication Persistence:"+(str)(mul(a)))
