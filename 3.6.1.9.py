my_list = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]
#
# Write your code here.
#
my_list_2 = []

for i in my_list:
    if i not in my_list_2:
        my_list_2.append(i)

print(my_list_2)
