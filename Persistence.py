#Addition and Multiplication Persistence
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