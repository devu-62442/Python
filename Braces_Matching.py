# ----------------------------------------------------------------------------------------------------------------------------
# Given a string of parenthesis,write a function to return the string“Matched”, 
# if the opening parentheses  match the closing parentheses. Otherwise return “Not matched”. Example: “((((()))((())(()))))”
# ----------------------------------------------------------------------------------------------------------------------------

# A method to check whether the braces match or not
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
        print("\nNOT-MATCHED")
    else:
        print("\nMATCHED") 

# Taking the input from the user
b=input("\n Enter an expression to check whether the PARANTHESIS are equal or not:")
d=[]
c=['(',')','[',']','<','>','{','}']
for i in c:
    for j in b:
        if(i==j):
            d.append(j)

# Caliing the method
braces(d)
