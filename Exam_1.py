# Jacob Auman
# First exam Due 1/20/23

#def marvelNumber(num):
# '''
#     A marvel number is a positive integer that is equal to the
#     sum of its proper divisors. The smallest marvel number is 6,
#     which is the sum of 1, 2, and 3. In other words, a marvel number is a
#     number where all of the numbers it is divisible by *OTHER THAN ITSELF*
#     added up equal the number – this does include 1.
#
#
#     If the number is a marvel number the function should return True, if it is not
#     the function should return False.
#
#     Parameters
#     ----------
#     num : int
#
#     Returns
#     -------
#     boolean
#         True if num is a marvel number
#         False if num is not a marvel number
#
#     Tip: You may want to use some sort of loop to find all
#     of the possible divisors and do your adding as you find
#     divisors, not at the very end.
#
#     '''



def agesAndStages(yearOld):
     yearOld= float(yearOld)

     if yearOld < 1:
         stage = "baby"
     elif 1 <= yearOld < 3:
         stage = "toddler"
     elif 3 <= yearOld < 5:
         stage = "preschool"
     elif 5 <= yearOld < 13:
         stage = "gradeschooler"
     elif 13 <= yearOld < 18:
         stage = "teenager"
     elif 18 <= yearOld:
         stage = "adult"

     return stage





   # '''
   #  Returns the appropriated message considering the
   #  age of a person based in the following rules:
   #      < 1 years old --> "baby"
   #      1-2 years old --> "toddler"
   #      3-4 years old --> "preschool"
   #      5-12 years old --> "gradeschooler"
   #      13-18 years old --> "teenager"
   #      > 18 --> adult
   #
   #  Parameters
   #  ----------
   #  yearOld : float
   #
   #
   #  Returns
   #  -------
   #  String with the appropriated message considering the
   #  rules above described.
   #
   #  '''

# Output Validation

if agesAndStages(0) == "baby":
    print("True")
else:
    print("False")
if agesAndStages(1) == "toddler":
     print("True")
else:
     print("False")
if agesAndStages(2) == "toddler":
     print("True")
else:
    print ("False")
if agesAndStages(3) == "preschool":
    print("True")
else:
    print ("False")
if agesAndStages(5) == "gradeschooler":
    print("True")
else:
    print ("False")
if agesAndStages(21) == "adult":
    print("True")
else:
    print ("False")