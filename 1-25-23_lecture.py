# Jacob Auman
# Sandbox for lecture

# Practice Problem

def welcome_message(first, last):
    print(f'Welcome to the Class {last}, {first}')


def ask_name():
    first = str(input('What is your First Name? '))
    last = str(input('What is your Last Name? '))
    welcome_message(first , last)

ask_name()


# Compound Intrest Function
def compound_interest(principle,intrest_P,years,compound_intervals):
    intrest_D = intrest_P / 100
    ammount = principle * ( 1 + (intrest_D / compound_intervals )) ** (compound_intervals * years)
    return ammount

principle = int(input('Enter Starting $'))
intrest_P = int(input('Enter Return %'))
years = int(input('Enter Years '))
compound_intervals = int(input('Times Compounded Each Year '))

ammount = compound_interest(principle,intrest_P,years,compound_intervals)

print(f'\nAfter {years} years you will have ${ammount:.2f}')
