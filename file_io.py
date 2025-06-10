with open("file.txt","r") as f:
    poem=f.read()
    if "twinkle".lower() in poem:
        print("yes there is.")
    else:
        print("no there is not.")