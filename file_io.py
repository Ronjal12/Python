import random
def game():
    print("You are playing the game.....")
    score=random.randint(1,100)

    with open("Hscore.txt","r") as f:
        Hscore=f.read()
        if(f.read()==""):
            with open("Hscore.txt","w") as f:
             f.write(f"Your highscore is {score}")

        elif(score>Hscore):
            with open("Hscore.txt","r") as f:
             f.write(f"Your new high score is {score}")
game()
print("Thankyou for playing.")