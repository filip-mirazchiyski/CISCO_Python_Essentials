hat_list = [1, 2, 3, 4, 5]

user_number = int(input("Write an integer number to replace the middle number of the integer: "))

hat_list[2] = user_number

del hat_list[4]

print(hat_list)
print(len(hat_list))

