secret_number = 777

print(
"""
+================================+
| Welcome to my game, muggle!    |
| Enter an integer number        |
| and guess what number I've     |
| picked for you.                |
| So, what is the secret number? |
+================================+
""")
number = int(input("enter the number: "))
while number != secret_number:
    if number == 7:
        print("getting closer")
    print("Ha ha! You're stuck in my loop!")
    number = int(input("enter the number: "))
else:
    print("Well done, muggle! You are free now.")
