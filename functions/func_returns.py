def addAndSubract(x, y, z):
    addFirstNums = x + y
    subtractLastTwoNum = y - z 
    return addFirstNums, subtractLastTwoNum

#def subtract(num1, num2):
#    difference = num1 - num2
 #   return difference

ourNumber1 = addAndSubract(7098, 2, 7)
ourNumber2 = addAndSubract(2, 7098, 10)
#ourNumber3 = subtract(10, 5)

print(ourNumber1)
print(ourNumber2)
#print(ourNumber3)

#Pass single parameter into function
#def echo(ourArgument):
#    print(ourArgument)
#
#echo(5.5)
#echo(False)
#echo(["Aaron", "Brooks"])
