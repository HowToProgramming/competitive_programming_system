a = int(input())
with open("output.txt", "w+") as out:
    out.write(str(a + 1))