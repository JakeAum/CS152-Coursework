# Jacob Auman
# CS 152 Lab 04
# 2/9/23

def temperatureClassification(temp):
    if temp < 40:
        out = 'COLD'
    elif 40 <= temp < 75:
        out = 'FAIR'
    else:
        out = 'HOT'
    return out

def weatherAnnouncer(temp, clearSkies, windy):
    # try to combine these two statements into one if statement!
    tempClass = temperatureClassification(temp)

    if (tempClass == 'HOT' and clearSkies ):
        return 'Wear summer clothes today.'
    elif (tempClass == 'HOT' and not clearSkies and windy):
        return 'Wear summer clothes today, but bring a rain jacket just in case.'
    elif (tempClass == 'HOT' and not clearSkies and not windy):
        return 'Wear summer clothes today, but bring an umbrella just in case.'
    elif (tempClass == 'FAIR' and windy):
        return 'Wear a jacket today.'
    elif (tempClass == 'FAIR' and clearSkies and not windy):
        return 'Wear whatever you would like today.'
    elif (tempClass == 'FAIR' and not clearSkies and not windy):
        return 'Wear a jacket today.'
    elif (tempClass == 'COLD' and clearSkies):
        return 'Wear winter gear today.'
    elif (tempClass == 'COLD' and not clearSkies and windy):
        return 'Just stay inside today.'
    elif (tempClass == 'COLD' and not clearSkies and not windy):
        return 'Wear winter gear today.'

# Verification and Validation

    # if hot and clear and not windy: 'Wear summer clothes today.
    print('TESTING', weatherAnnouncer(77, True, False))
    # if hot and not clear and windy: 'Wear summer clothes today, but bring a rain jacket just in case.'
    print('TESTING', weatherAnnouncer(95, False, True))
    # if hot and not clear and not windy: 'Wear summer clothes today, but bring an umbrella just in case.'
    print('TESTING', weatherAnnouncer(95, False, False))

    # if fair AND clear AND not windy: 'Wear whatever you would like today.'
    print('TESTING', weatherAnnouncer(56, True, False))
    # if fair AND otherwise: 'Wear a jacket today.'
    print('TESTING', weatherAnnouncer(56, False, False))

    # if cold AND windy AND PC: 'Just stay inside today.'
    print('TESTING', weatherAnnouncer(22, False, True))
    # if cold AND otherwise: 'Wear winter gear today.'
    print('TESTING', weatherAnnouncer(2, True, True))
