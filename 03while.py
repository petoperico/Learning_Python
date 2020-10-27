"""Class While."""

count = 0
loop = True
while count <= 100:
    print(count)
    count += 1
    if count == 100:
        loop = False
else:
    print("Else's print")
