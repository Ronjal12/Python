with open("donkey.txt","r") as f:
    word=input("Enter the word")
    line_no=1
    content=f.readlines()

for line in content:
    if word in line:
        print(f"Yes the word in present in line: {line_no}")
        break
    line_no+=1
else:
        print("No the word is not present")