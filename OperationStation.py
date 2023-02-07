#Jacob Auman
# Work For Lab 04

# 1. howManyEven() is a function that makes a number positive, then calls another function to see if the number is positive and subtracts one and repeats the cycle.
# howManyEven(9) = returns 3
# 2.isOdd(3) returns true because the remainder of 3/2 = non-zero
# 3. Complete
# 4. n=int(3/4) can be represented by 3 // 4 which is floor division

# input: a number
# output: the number of even numbers between that number and 0 (including 0 and the number)
def howManyEven(num):
    count = 0
    if num < 0:
        num *= -1
    while (num >= 0):
        if isEven(num):
            count += 1
        num -= 1
    return count


# input: a number
# output: true/false depending on whether the number is even or not
def isEven(num):
    return num % 2 == 0


# input: a number
# output: true/false depending on whether the number is odd or not
def isOdd(num):
    return num % 2 != 0


def noChange(cents):
    # student code here
    return


# input: num–an int of some kind
# output: the positive factorial of num
def oldFactorial(num):
    total = 1
    if num < 0:
        num *= (-1)
    while (num == num):
        if num <= 0:
            break
        else:
            total = total * num
            num -= 1
    return total

def noChange(cents):
    cents = cents/100
    dollars = int(cents)
    if dollars == cents:
        print(f'Hoorah!')
    else:
        print('Keep the change!')
    return(dollars)

def main():
    print("TESTING", noChange(100))
    print("TESTING", noChange(225))


if __name__ == "__main__":
    main()