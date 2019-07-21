def braces(b):
    a={')':'(','>':'<','}':'{',']':'['}
    st=[]
    flag=0
#    print(b)
    for i in b:
        if i in a.values():
            st.append(i)
#            print(i)
        elif len(st)==0 and i in a.keys():
            flag=1
#            print(flag)
        elif i in a.keys() and st[-1]==a[i]:
            st.pop()
#            print(key)
        else:
            flag=0
        if(flag==1):
            break
        else:
            continue
    if(flag==1 or len(st)>0):
        print("NOT-MATCHED")
    else:
        print("MATCHED") 
    
b=input("Enter an expression to check whether the PARANTHESIS are equal or not:")
d=[]
c=['(',')','[',']','<','>','{','}']
for i in c:
    for j in b:
        if(i==j):
            d.append(j)
braces(d)
