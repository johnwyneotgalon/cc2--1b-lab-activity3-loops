n = int(input("Enter the number : "))

i = n
while i > 0:
    j = 1
    while j <= i:
        print(j, end="")
        j += 1
    print()
    i -= 1