n = int(input("Enter the number: "))
sum = 0
for i in range(1, n + 1):
    sum += i


sum_string = ""
for i in range(1, n + 1):
    sum_string += str(i)
    if i < n:
        sum_string += "+"


print(f"{sum_string} is {sum}")