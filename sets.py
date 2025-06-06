a=int(input("Enter the age of the person"))
#if condition part 1
if(a%2==0):
    print("The number is even")
#if condition part 2
if(a>=18):
    print("you are in the age of the consent")

elif(a<18):
    print("you are not in the age of the consent")

elif(a<=0):
    print("Please enter a valid age")

print("End of the program")