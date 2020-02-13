#Create a program that asks the user to enter their name and their age. Print out a message addressed to them that tells them the year that they will turn 100 years old.
#
#Extras:
#
#Add on to the previous program by asking the user for another number and printing out that many copies of the previous message. (Hint: order of operations exists in Python)
#Print out that many copies of the previous message on separate lines. (Hint: the string "\n is the same as pressing the ENTER button)

#1. Ask user to enter name and age
#    1a. Ask user to enter name
#    1b. Ask user to enter age
#2. Print message addressed to user with year they will turn 100
#    2a. Calculate year user will turn 100
#    2b. Print message addressed to user with the year we calculated
#
#PSEUDOCODE
#ask user input for name ---> assign to name variable
#ask user input for age ---> assign to age variable
#subtract users age from 100 ---> assign to years_left_to_100 variable
#Add years_left_to_100 to the current year(2020)
#Build print statement which has the users name and year they will turn 100
#ask user input for new_number ----> assign to new_num variable
#Print out new_num compies of Print statement from 2 steps above

name = input("Hello Sir or Madame, What is your name?: ")
age = int(input("Also, if you wouldnt mind, what age will you be turning this year?: "))
current_year = 2020

years_left_to_100 = 100 - age

year_of_age_100 = current_year + years_left_to_100

output = f"Your name is {name} and you won't be 100 years old until {year_of_age_100}"
print(output)

new_num = int(input("Please give us a new number...please?: "))

print((output + "\n") * new_num)

