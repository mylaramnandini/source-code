jewels = set(input("enter the stone type:"))
stones = input("enter the stones:")
count = 0
for i in stones:
    for char in jewels:
        if char == i:
            count = count +1
print("the stones which are jewels are:", count)


