# Jacob Auman
# 2/14/2023

# [0, 1, 2, 3, 4, 5, 'got them all!'] and it is in the class list

# [0, 'got them all!', 1, 'got them all!', 2, 'got them all!', 3, 'got them all!', 4, 'got them all!', 5, 'got them all!']
#got em all is added to the list between each element.

# I'm not sure why she uses odd numbers for bread...
# I can't even read her handwriting for this one...
# Oh good, vegetables
# Not sure why there are prices in here.
# Oh good, vegetables
# I'm not sure why she uses odd numbers for bread...
# Not sure why there are prices in here.
# This is also in the class of a list

# myFavoriteThings = [17, 0.2, "Phantom of the Opera"]




# input: num--number of items to get
# output: you figure this out!
def itemFetching(num):
    lst = []
    for i in range(num):
        lst.append(i)
    lst.append("got them all!")  # what would happen if we tabbed this line inside of the for-loop?
    return lst


# input: grocery list of mixed types
# output: you figure this out!
def itemSorting(lst):
    sorted = []
    for item in lst:
        if item == 1 or item == 3 or item == 5 or item == 9:
            print("I'm not sure why she uses odd numbers for bread...")
            sorted.append("bread")
        elif item == "peas" or item == "carrots" or item == "broccoli":
            print("Oh good, vegetables")
            sorted.append(item)
        elif item == 2.25 or item == 5.3:
            print("Not sure why there are prices in here.")
            sorted.append("snacks(??)")
        else:
            print("I can't even read her handwriting for this one...")
    return sorted


# input: timer--number of seconds in time out
# output: countDown-- a list with the timer counting down until 0
def timeOut(timer):
    countDown = []
    # student code
    countDown = list(range(timer,0,-1))
    return countDown


# Verification and Validation
# print(itemFetching(6))
#
# lst = [3, 7, "peas", 2.25, "carrots", 1, 5.3]
# itemSorting(lst)
#
# print(type(itemSorting(lst)))
#
# print("TESTING", timeOut(4))
# print("TESTING", timeOut(2))