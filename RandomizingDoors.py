import random
import array
import sys
#initialzing public variables
doorone = ['veM1', 'veM2', 'veM3', 'veM4', 'veM5']
doortwo = ['eM1', 'eM2', 'eM3', 'eM4']
doorthr = ['nM1', 'nM2', 'nM3']
doorfor = ['hM1', 'hM2', 'hM3', 'hM4']
doorfiv = ['vhM1', 'vhM2', 'vhM3', 'vhM4', 'vhM5']
doordifficulty = random.randrange(2)
roundcount = 1

#Randomizes door order coming out
def randomize_Monsters():
    random.shuffle(doorone)
    random.shuffle(doortwo)
    random.shuffle(doorthr)
    random.shuffle(doorfor)
    random.shuffle(doorfiv)
#Checks if doordifficulty is equal to 0 then door order is 1-5. Else door order is 5-1
def door_Difficulty():
    global doorone, doortwo, doorthr, doorfor, doorfiv
    randomize_Monsters()
    if doordifficulty == 0:
        print ("If", doorone) #Remove
    else:
        tempdoor = doorone
        doorone = doorfiv
        doorfiv = tempdoor
        tempdoor = doortwo
        doortwo = doorfor
        doorfor = tempdoor
        del tempdoor
        print ("Else", doorone) #Remove
#Prompts user for door 1, 2, 3, 4, or 5. Removes first monster from the respective list based on user prompt
def select_Door():
    userinput = 10
    if userinput == 1 and len(doorone) > 1:
        print (doorone.pop(1))
    elif userinput == 2 and len(doortwo) > 1:
        print (doortwo.pop(1))
    elif userinput == 3 and len(doorthr) > 1:
        print (doorthr.pop(1))
    elif userinput == 4 and len(doorfor) > 1:
        print (doorfor.pop(1))
    elif userinput == 5 and len(doorfiv) > 1:
        print (doorfiv.pop(1))
    elif userinput == 10:
        sys.exit('End')
    else:
        print ("Next Round")
#Keeps track of round. If not round 1, can only select one monster
def round_Counter(counter):
    if counter == 1:
        print ("User Select Doors and Number")
    elif counter == 100:
        print ("Final Round")
    else:
        select_Door()



door_Difficulty()
while roundcount < 101:
    round_Counter(roundcount)
    print("Rounds Remaining:", 100-roundcount)
    roundcount += 1
