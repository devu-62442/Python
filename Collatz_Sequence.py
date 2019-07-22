# Collatz Sequence
# -----------------------------------------------------------------------------------------------------------------------------
# Given N, apply the following rules iteratively to get a sequence that ends with 1.
# N→N/2 (if N is even)
# N→(3∗N)+1 (if N is odd)
# For example:
# 13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
# Write a function to generate a Collatz sequence. 
#-----------------------------------------------------------------------------------------------------------------------------

# Method to generate the COLLATZ SEQUENCE
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

# Getting the input from the user
a=(int)(input("Enter the number to start generating Collatz Sequence:"))
# If you input 1 million you will get the longest Collatz Sequence

# Calling the method
Collatz(a)
