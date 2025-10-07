


first = int(input("Enter the first integer: "))
second = int(input("Enter the second integer: "))

gsd = min(first, second)

while not(first % gsd == 0 and second % gsd == 0):
    gsd -= 1

print(gsd)
