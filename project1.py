import random

def func1():
    L=['snake','water','gun']

    computer=random.choice(L)

    print(L)

    your_choice=int(input("Enter your choice in number"))

    Your_choice=L[your_choice-1]


    if(Your_choice==computer):
        print("Its a draw.")
        print(f"computer chose {computer}")


    elif(Your_choice=="snake" and computer=="water"):
        print("You win.")
        print(f"computer chose {computer}")

    elif(Your_choice=="snake" and computer=="gun"):
        print("You lose.")
        print(f"computer chose {computer}")

    elif(Your_choice=="water" and computer=="snake"):
        print("You lose.")
        print(f"computer chose {computer}")

    elif(Your_choice=="water" and computer=="gun"):
        print("You win.")
        print(f"computer chose {computer}")

    elif(Your_choice=="gun" and computer=="snake"):
        print("You win.")
        print(f"computer chose {computer}")

    elif(Your_choice=="gun" and computer=="water"):
        print("You lose.")
        print(f"computer chose {computer}")

choice="y"

while(choice =="y"):
    func1()
    choice=input("DO you want to continue playing y/n").lower() 

print("Thankyou for playing.")