#STEP 1
collegeAddress = {
'Building Name': 'Ammons Hall',
'Street': '711 Oval Dr',
'City': 'Fort Collins',
'State': 'Colorado',
'Zip Code': 80523
}

#STEP 2
building2Address = {'Building Name': 'Ammons Hall',
'Street': '711 Oval Dr',
'City': 'Fort Collins',
'State': 'Colorado',
'Zip Code': 80523}

building3Address = {'Building Name': 'Ammons Hall',
'Street': '711 Oval Dr',
'City': 'Fort Collins',
'State': 'Colorado',
'Zip Code': 80528}

dictionaryOfAddresses = {
'College Address': collegeAddress,
'Building 2 Address': building2Address,
'Building 3 Address': building3Address}


# for you to test your dictionary of dictionaries
print(dictionaryOfAddresses)

# should output Fort Collins, feel free to change for testing purposes
print(dictionaryOfAddresses['College Address']['City'])