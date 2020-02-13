#Take a list, say for example this one:

#  a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
#and write a program that prints out all the elements of the list that are less than 5.

user_input = int(input("C'mon, give us a number!: "))

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

new_a = []

for i in a:
    if i < user_input:
        new_a.append(i)

print(new_a)
#print(new_a := [i for i in a if i < user_input])

