#Aliquot sum
#Perfect Number

def Aliquot(a):
    s=0
    for i in range(1,a):
        if(a%i==0):
            s=s+i
    if(a==s):
        print("It's the PERFECT NUMBER:"+(str)(s))
    else:
        print("Not a PERFECT NUMBER:"+(str)(a))
        
a=(int)(input("Enter the number to ckeck whether it is PERFECT or NOT: "))
Aliquot(a)