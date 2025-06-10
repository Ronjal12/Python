with open("file.txt", "w") as f:
    n=input("Enter the number: ")

    for i in range(1,11):
            s= f"{n} X {i}={n*i}"
            f.write(s)
