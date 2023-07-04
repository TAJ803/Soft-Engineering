blocks = int(input("Enter the number of blocks: "))

height = 0
blocks = 0
layer_number = 0

while blocks > 0:

    if blocks - layer_number < 0:
        break
    else:
        layer_number = layer_number + 1
        height = height + 1
        blocks = blocks - layer_number

print("The height of the pyramid:", height)
