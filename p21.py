f=open("21.txt")
print(f.read())
f.close()


with open("21.txt") as f:
    print(f.read())