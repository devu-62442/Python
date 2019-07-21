#Collatz Sequence
def Collatz(a):
    b=a
    i=1
    list1=list()
    list1.insert(0,b)
    while(b!=1):
        if(b%2==0):
            b=b/2
        else:
            b=(b*3)+1
        list1.insert(i,(int)(b))
        i=i+1
   # print(list1)
    
    for i in range(0,len(list1)):
        print(list1[i]," -> ",end="")
    
a=(int)(input("Enter the number to start generating Collatz Sequence:"))
if(a<1000000):
    Collatz(a)
else:
    print("The Number Is GREATER Than 999999")