def generate(n):
    table=""
    for i in range(1,11):
        table += f"{n} X {i} = {n*i}\n"

        with open(f"table/table_{n}","w") as f:
            f.write(table)

for i in range(2,21):
    generate(i)

    #table/table_{n} tells the table to be followed for other number from 2 to 21 as well.