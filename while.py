my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
index = 0

while my_list[index] > 0:
    if index >= len(my_list):
        break
    print(my_list[index])
    index += 1
