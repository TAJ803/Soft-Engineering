x = float(input("Enter value for x: "))

# Write your code here.
#y = (1/((x+1/((x+1)/(x+1/x))))

c = (x + (1 / x))
b = (x + (1 / c))
a = (x + (1 / b))

y = (1 / a )

print("y =", y)
