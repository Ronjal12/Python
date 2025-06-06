n=int(input("Enter the number: "))
i=1
def funct(n,i):
    if(i==11):
        return ""
    print(f"{n} X {i} = {n*i}")
    return funct(n,(i+1))

funct(n,i)
