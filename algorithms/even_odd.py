#Ask the user for a number. Depending on whether the number is even or odd, print out an appropriate message to the user. Hint: how does an even / odd number react differently when divided by 2?
#
#Extras:
#
#If the number is a multiple of 4, print out a different message.
#Ask the user for two numbers: one number to check (call it num) and one number to divide by (check). If check divides evenly into num, tell that to the user. If not, print a different appropriate message.

#PSEUDOCODE
#ask user for a number ----> Save to variable called num
#divide num by 2, if remainder is 0, print "The number you have entered is even"
#if remainder is NOT 0, print "The number you have entered is odd"

num = int(input("Please provide a number: "))
check = int(input("Please give us a number to check if the first is evenlt divisible by: "))

if num % check == 0:
    print("You already know this went into your number an even amount of time. what a waste of time")
else:
    print("You also already knew this would NOT divide evenly")

