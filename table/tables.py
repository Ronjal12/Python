def generate(n):
    table=""
    for i in range(1,11):
        table += f"{n} X {i} = {n*i}\n"

        with open("table/table_{n}","w") as f:
            f.write(table)

for i in range(2,21):
    generate(i)