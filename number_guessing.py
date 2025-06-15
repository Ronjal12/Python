import random

choice="y"
count=0
while(choice=="y"):
    Number=random.randint(1,4)
    Input=int(input("Enter your number: "))

    if(Input==Number):
        print("you have guessed the number right. It was: ",Number)
        count+=1

    else:
     print("The number is not right. It was: ",Number)

    print("Your score is: ",count)
    choice=input("Do you want to play again? y/n")