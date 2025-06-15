def see():
    todo=input("Do you want to see your tasks?")

    if(todo=="y"):
        print(listz)

    else:
        print("Thankyou.")
listz=[]

choice="y"
while(choice=="y"):
    tasks=input("Enter your tasks: ")
    listz.append(tasks)

    choice=input("Do you want to continue? y/n")


if(choice=="n"):
    see()