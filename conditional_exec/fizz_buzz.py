#The famous FizzBuzz
#1. Print the numbers 0 to 100.
#2. For numbers that are evenly divisible by 3, print "Fizz" instead of printing the number
#3. For numbers that are evenly divisible by 5, print "Buzz" instead of printing the number
#4. For numbers that are evenly divisible by both 3 and 5, print "FizzBuzz" instead of printing the number

counter = 0

while counter <= 100:
    if counter % 15 == 0:
        print("FizzBuzz")
    elif counter % 3 == 0:
        print("Fizz")
    elif counter % 5 == 0:
        print("Buzz")
    else:
        print(counter)

    counter += 1


