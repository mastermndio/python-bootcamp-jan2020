
def latest(scores):
    return scores[-1]

def personal_best(scores):
    scores = mastermnd_sort(scores)
    return scores[-1]

def personal_top_three(scores):
    scores = mastermnd_sort(scores)
    return scores[:3]

#This function needs to be updated to sort from high to low instead of low to high.
#See if you can modify this to do so, and also update the personal_best() and 
#personal_top_three() functions to work with your changes. 
def mastermnd_sort(lst):
    for num in range(len(lst) - 1):
        for num in range(len(lst) - 1):
            if lst[num] > lst[num + 1]:
                lst[num], lst[num + 1] = lst[num +1], lst[num]
    return lst