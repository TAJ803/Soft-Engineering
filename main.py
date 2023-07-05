blocks = int(input("Enter number of blocks: "))

for i in range(blocks): 
    if i*(i+1)/2 <= blocks: 
        height = i

print("The height of the pyramid is:",height)