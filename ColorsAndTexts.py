# Jacob Auman
# Lab 08

#1.green(str) index ends with 4 which is not included
#2.having no bounds on the string funtion will return all elements before or after.
#3.only one condition will be returned, they will not stack
#4.It compares the string that is read in the message file and compares each word to the list of tranclation and if there is a match then it replaces that part of the string.

texts = ["lol", "ttyl", "nvm", "brb", "smh", "idk", "btw"]
textTranslations = ["laughing out loud", "talk to you later", "nevermind", "be right back", "shaking my head", "I don't know", "by the way"]

#reads in files and puts the items into lists--if the files have sentences, it separates the words in the list
def readFile(fileName):
    lst = []
    with open(fileName) as file:
        for lines in file:
            for word in lines.split():
                lst.append(word)
    return lst

#input: a list of words from a text
#output: the text with the abbrieviations from textTranslations elongated
def textToSpeech(txtlst):
    str = ""
    for word in txtlst:
        if word.lower() in texts:
            num = texts.index(word.lower())
            str += " " + textTranslations[num]
        else:
            str += " " + word
    return "Translated: " + str

#input: string of RGB values
#output: the red value
def red(str):
    return int(str[:2], 16)

#input: string of RGB values
#output: the green value
def green(str):
    return int(str[2: 4], 16) #Why 4?

#input: string of RGB values
#output: the blue value
def blue(str):
    return int(str[4:], 16) #what happens when we don't put the second value?

# input: color as RGB code
#output: true or false depending on if a person with protanopia could see it
def protanopiaSee(color):
    return red(color) < 64

# input: color as RGB code
#output: true or false depending on if a person with deuteranopia could see it
def deuteranopiaSee(color):
    return green(color) < 64

# input: color as RGB code
#output: true or false depending on if a person with tritanopia could see it
def tritanopiaSee(color):
    if 0 < blue(color):
        if 230 < red(color):
            if 230 < green(color):
                return True
    return False

def main():
    text = readFile("text.txt")
    print(textToSpeech(text))
    colors = readFile("colors.txt")
    for color in colors:
        str = "Can see: "
        if protanopiaSee(color):
            str += "protanopia "
        if deuteranopiaSee(color): #What might happen if we used an elif here? and the next was an else?
            str += "deuteranopia "
        if tritanopiaSee(color):
            str += "tritanopia"
        if not protanopiaSee(color) and not deuteranopiaSee(color) and not tritanopiaSee(color):
            str += "None"
        print(str)
    print('Testing', tritanopiaSee("E7F002"))
    print('Testing', tritanopiaSee("03F002"))

if __name__ == "__main__":
    main()