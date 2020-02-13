def firsLast(firstName, lastName):
    return f"Your First name is {firstName} and your Last name is {lastName}"


print(firsLast("Aaron", "Brooks"))




x = lambda firstName, lastName: f"Your First name is {firstName} and your Last name is {lastName}"
print(x("Aaron", "Brooks"))
