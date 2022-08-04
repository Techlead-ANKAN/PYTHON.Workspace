a = int(input("Enter a: "))
b = int(input("Enter b: "))
if a>b:
    max = a
else:
    max = b
while (True):
    if (max % a == 0  and  max % b == 0):
        lcm = max
        break
    max += 1
print(f"LCM of {a} and {b} = {lcm}")

