import random
import array
#initialzing public variables
vesy = ['M0', 'M1', 'M2', 'M3', 'M4']
easy = ['M0', 'M1', 'M2', 'M3']
norm = ['M0', 'M1', 'M2',]
hard = ['M0', 'M1', 'hM2', 'hM3']
vhrd = ['vhM0', 'vhM1', 'vhM2', 'vhM3', 'vhM4']
doordifficulty = random.randrange(2)
#create class that randomizes door order coming out
def randomize_Monsters():
    random.shuffle(vesy)
    random.shuffle(easy)
    random.shuffle(norm)
    random.shuffle(hard)
    random.shuffle(vhrd)
#create class that checks if doordifficulty is equal to 0 then door order is 1-5. Else door order is 5-1
def door_Difficulty():
    if doordifficulty == 0:
        print ("If", doordifficulty) #Remove
        randomize_Monsters()
        door1 = vesy
        door2 = easy
        door3 = norm
        door4 = hard
        door5 = vhrd
    else:
        print ("Else", doordifficulty) #Remove
        randomize_Monsters()
        door1 = vhrd
        door2 = hard
        door3 = norm
        door4 = easy
        door5 = vesy

door_Difficulty()
