#Step 0
#input: num -- an int
#output: lst -- a list of ints from 0 to num-1
def basicLoop(num):
    lst = []
    for i in range(num):
        lst.append(i)
    return lst


#Step 1
#input: customers -- the number of customers in line for the ride
#output: lst -- a list full of the numbers from 0 to customers-1 and the string "now that's a line!"
def lineManage(customers):
    lst = []
    for i in range(0,customers):
        lst.append(i)
    lst.append('now that’s a line!')
    return lst


#Step 2
#input: customers -- the number of customers in line for the ride
#output: lst -- a list full of the numbers from 0 to customers-1, with the splashed customers replaced by "splashed!"
def lineSplash(customers):
    lst = []
    #student code here
    for i in range(0,customers):
        if (i % 3) == 0:
            lst.append('splashed!')
        else:
            lst.append(i)
    return lst


#Step 3
#input: num -- some starting int number
#output: lst -- a list from num to 1 and the string "Happy New Years!"
def connieCountdown(num):
    lst = []
    #student code here
    for i in range(num,0,-1):
        lst.append(i)
    lst.append('Happy New Years!')
    return lst


#Step 4
#input: rolls -- a list of the player's rolls. success -- a list of Connie's rolls
#output: any time one of player's rolls matches one of Connie's, append to lst "Success for [number]"
def ringToss(rolls, success):
   lst = []
    #student code here
   for i in rolls:
       for j in success:
           if i == j:
               lst.append(f'Success for {i}')

   return lst

#Step 5
#input: start -- random starting number numMoves -- the number of moves that should go into the dance list
#output: dance -- a list full of dance moves based on numMoves and start
def dinerDance(start, numMoves):
    dance = []
    #student code here

    for i in range(numMoves):
        move = int(((start+i) * 2 + 4) / 3)

        if ( move % 3) == 0:
            dance.append('spin')
        elif( move % 4) == 0:
            dance.append('side step')
        elif( move % 5) == 0:
            dance.append('shake hips')
        elif( move % 2) == 0:
            dance.append('freestyle')
        else:
            dance.append('hop')
    return dance


def main():
    print("Basic Loop returns: {}".format(basicLoop(3)))
    print("TESTING", lineManage(5))  # should return [0, 1, 2, 3, 4, “now that’s a line!”]
    print("TESTING", lineSplash(5))  # should return [“splashed”, 1, 2, “splashed!”, 4]
    print("TESTING", connieCountdown(10))  # should return [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, “Happy New Years!”]
    print("TESTING", ringToss([10, 3, 5, 7, 20, 19], [19, 3, 18, 12, 15, 1]))
    print("TESTING", dinerDance(50, 4))  # should return [“freestyle”, “spin”, “hop”, “spin”]


    return

if __name__ == "__main__":
    main()

