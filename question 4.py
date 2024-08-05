words = input()
l = words.split(" ")
x = input()
x1 =[]
for i in l:
    for j in i:
        if x == j:
            x1.append(l.index(i))
            break
print(x1)