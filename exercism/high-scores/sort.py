our_list = [10, 30, 90, 30, 100, 20, 10, 0, 30, 40, 40, 70, 70]
print(our_list)
for num in range(len(our_list) - 1):
    for num in range(len(our_list) - 1):
        if our_list[num] > our_list[num + 1]:
            our_list[num], our_list[num + 1] = our_list[num +1], our_list[num]

print(our_list)
