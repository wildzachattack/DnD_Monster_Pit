import random
import array
import sys
import tkinter

#initialzing public variables
#list
doorone = ['Bullfango (x3)', 'Vespoid Queen', 'Konchu (x2)', 'Girros', 'Hermitaur (x2)'] #very easy can change w/ doorfiv
doortwo = ['Quetzalcoatlus', 'Great Maccao', 'Bulldrome', 'Cephalos'] #easy can change w/ doorfor
doorthr = ['Yian Kut-Ku', 'Selstas', 'Ludroth (x2)'] #normal
doorfor = ['Hypnocatrice', 'Great Jagras', 'Royal Ludroth (easier)', 'Tetsucabra'] #hard can change w/ doortwo
doorfiv = ['Tzitzi-Ya-Ku', 'Royal Ludroth', 'Great Girros', 'Great Boar (x2) pg395', 'Zamtrios'] #very hard can change w/ doorone
#dictionary
monsterencounterlist = {}
#integers
doordifficulty = random.randrange(2)
roundcount = 1
mnstcntr1 = 0
mnstcntr2 = 0
mnstcntr3 = 0
mnstcntr4 = 0
mnstcntr5 = 0
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
    if doordifficulty != 0:
        tempdoor = doorone
        doorone = doorfiv
        doorfiv = tempdoor
        tempdoor = doortwo
        doortwo = doorfor
        doorfor = tempdoor
        del tempdoor
#Prompts user for door 1, 2, 3, 4, or 5. Removes first monster from the respective list based on user prompt
def select_Door(userinput):
    global monsterencounterlist
    if userinput == 1 and len(doorone) > 1:
        temp = doorone.pop(1)
        monsterencounterlist[temp] = 0.8
        print (temp)
        del temp
    elif userinput == 2 and len(doortwo) > 1:
        temp = doortwo.pop(1)
        monsterencounterlist[temp] = 1.2
        print (temp)
        del temp
    elif userinput == 3 and len(doorthr) > 1:
        temp = doorthr.pop(1)
        monsterencounterlist[temp] = 1.4
        print (temp)
        del temp
    elif userinput == 4 and len(doorfor) > 1:
        temp = doorfor.pop(1)
        monsterencounterlist[temp] = 1.5
        print (temp)
        del temp
    elif userinput == 5 and len(doorfiv) > 1:
        temp = doorfive.pop(1)
        monsterencounterlist[temp] = 1.8
        print (temp)
        del temp
    elif userinput == 10:
        sys.exit('End')
    else:
        print ("Next Round")
#Round 1 Reads Monsters Submitted and moves them from list to encounter
def monsters_Entered(d1, d2, d3, d4, d5):
    door1 = 1
    door2 = 2
    door3 = 3
    door4 = 4
    door5 = 5
    while d1 > 0:
        select_Door(door1)
        d1 -= 1
    while d2 > 0:
        select_Door(door2)
        d2 -= 1
    while d3 > 0:
        select_Door(door3)
        d3 -= 1
    while d4 > 0: 
        select_Door(door4)
        d4 -= 1
    while d5 > 0: 
        select_Door(door5)
        d5 -= 1
#Keeps track of round. If not round 1, can only select one monster
def round_Counter(counter):
    if counter == 1:
        round_One()
    elif counter == 50:
        print ("Final Round")
    else:
        next_Round()
#Round one. Keeps track of arrows, monsters etc
def round_One():
    def up_Arrow1():
        global mnstcntr1
        if mnstcntr1 < 5:
            mnstcntr1 += 1
            mnstcntrlbl1.configure(text = mnstcntr1)
    def up_Arrow2():
        global mnstcntr2
        if mnstcntr2 < 4:
            mnstcntr2 += 1
            mnstcntrlbl2.configure(text = mnstcntr2)
    def up_Arrow3():
        global mnstcntr3
        if mnstcntr3 < 3:
            mnstcntr3 += 1
            mnstcntrlbl3.configure(text = mnstcntr3)
    def up_Arrow4():
        global mnstcntr4
        if mnstcntr4 < 4:
            mnstcntr4 += 1
            mnstcntrlbl4.configure(text = mnstcntr4)
    def up_Arrow5():
        global mnstcntr5
        if mnstcntr5 < 5:
            mnstcntr5 += 1
            mnstcntrlbl5.configure(text = mnstcntr5)
    def down_Arrow1():
        global mnstcntr1
        if mnstcntr1 > 0:
            mnstcntr1 -= 1
            mnstcntrlbl1.configure(text = mnstcntr1)
    def down_Arrow2():
        global mnstcntr2
        if mnstcntr2 > 0:
            mnstcntr2 -= 1
            mnstcntrlbl2.configure(text = mnstcntr2)
    def down_Arrow3():
        global mnstcntr3
        if mnstcntr3 > 0:
            mnstcntr3 -= 1
            mnstcntrlbl3.configure(text = mnstcntr3)
    def down_Arrow4():
        global mnstcntr4
        if mnstcntr4 > 0:
            mnstcntr4 -= 1
            mnstcntrlbl4.configure(text = mnstcntr4)
    def down_Arrow5():
        global mnstcntr5
        if mnstcntr5 > 0:
            mnstcntr5 -= 1
            mnstcntrlbl5.configure(text = mnstcntr5)
    def submit():
        monsters_Entered(mnstcntr1, mnstcntr2, mnstcntr3, mnstcntr4, mnstcntr5)
        sbmtbtn.configure(command = window.destroy)
    def exit():
        exitbtn.configure(command = window.destroy)
        sys.exit('End')
    #GUI
    window = tkinter.Tk()
    window.title("GUI")
    header = tkinter.Label(window, text = "Round 1, Release Monsters")
    header.grid(column = 3, row = 0)
    #Row 1 Door Titles
    drhdr1 = tkinter.Label(window, text = "Door 1")
    drhdr1.grid(column = 1, row = 1)
    drhdr2 = tkinter.Label(window, text = "Door 2")
    drhdr2.grid(column = 2, row = 1)
    drhdr3 = tkinter.Label(window, text = "Door 3")
    drhdr3.grid(column = 3, row = 1)
    drhdr4 = tkinter.Label(window, text = "Door 4")
    drhdr4.grid(column = 4, row = 1)
    drhdr5 = tkinter.Label(window, text = "Door 5")
    drhdr5.grid(column = 5, row = 1)
    #Pull Images
    up = tkinter.PhotoImage(file = "Arrow_Up.png")
    down = tkinter.PhotoImage(file = "Arrow_Down.png")
    #Row 2 Up Buttons. Increase the count for respective door
    bt1Up = tkinter.Button(window, height=50, width=50, image = up, command = up_Arrow1)
    bt1Up.grid (column = 1, row = 2)
    bt2Up = tkinter.Button(window, height=50, width=50, image = up, command = up_Arrow2)
    bt2Up.grid (column = 2, row = 2)
    bt3Up = tkinter.Button(window, height=50, width=50, image = up, command = up_Arrow3)
    bt3Up.grid (column = 3, row = 2)
    bt4Up = tkinter.Button(window, height=50, width=50, image = up, command = up_Arrow4)
    bt4Up.grid (column = 4, row = 2)
    bt5Up = tkinter.Button(window, height=50, width=50, image = up, command = up_Arrow5)
    bt5Up.grid (column = 5, row = 2)
    #Row 3 Counter. As buttons are clicked counter goes up and down
    mnstcntrlbl1 = tkinter.Label(window, text = mnstcntr1)
    mnstcntrlbl1.grid(column = 1, row = 3)
    mnstcntrlbl2 = tkinter.Label(window, text = mnstcntr2)
    mnstcntrlbl2.grid(column = 2, row = 3)
    mnstcntrlbl3 = tkinter.Label(window, text = mnstcntr3)
    mnstcntrlbl3.grid(column = 3, row = 3)
    mnstcntrlbl4 = tkinter.Label(window, text = mnstcntr4)
    mnstcntrlbl4.grid(column = 4, row = 3)
    mnstcntrlbl5 = tkinter.Label(window, text = mnstcntr5)
    mnstcntrlbl5.grid(column = 5, row = 3)
    #Row 4 Down Buttons. Decrease the count for respective door
    bt1Dwn = tkinter.Button(window, height=50, width=50, image = down, command = down_Arrow1)
    bt1Dwn.grid (column = 1, row = 4)
    bt2Dwn = tkinter.Button(window, height=50, width=50, image = down, command = down_Arrow2)
    bt2Dwn.grid (column = 2, row = 4)
    bt3Dwn = tkinter.Button(window, height=50, width=50, image = down, command = down_Arrow3)
    bt3Dwn.grid (column = 3, row = 4)
    bt4Dwn = tkinter.Button(window, height=50, width=50, image = down, command = down_Arrow4)
    bt4Dwn.grid (column = 4, row = 4)
    bt5Dwn = tkinter.Button(window, height=50, width=50, image = down, command = down_Arrow5)
    bt5Dwn.grid (column = 5, row = 4)
    #Row 5 Exit/Submit. Exits the system or submits counters
    sbmtbtn = tkinter.Button(window, text = "Submit", command = submit)
    sbmtbtn.grid (column = 1, row = 5)
    exitbtn = tkinter.Button(window, text = "Exit", command = exit)
    exitbtn.grid (column = 5, row = 5)

    window.mainloop() #Calls Main GUI
def next_Round():
    def submit():
        #if no radio button selected, next round
        #while loop < 7 CHECKS each radio button 1-6
        input = 0
        select_Door(input)
        sbmtbtn.configure(command = window.destroy)
    #GUI
    window = tkinter.Tk()
    window.title("GUI")
    header = tkinter.Label(window, text = "New round, release a monster from a door?")
    header.grid(column = 3, row = 0)
    #Row 1 Door Titles
    drhdr1 = tkinter.Label(window, text = "Door 1")
    drhdr1.grid(column = 1, row = 1)
    drhdr2 = tkinter.Label(window, text = "Door 2")
    drhdr2.grid(column = 2, row = 1)
    drhdr3 = tkinter.Label(window, text = "Door 3")
    drhdr3.grid(column = 3, row = 1)
    drhdr4 = tkinter.Label(window, text = "Door 4")
    drhdr4.grid(column = 4, row = 1)
    drhdr5 = tkinter.Label(window, text = "Door 5")
    drhdr5.grid(column = 5, row = 1)
    drhdr5 = tkinter.Label(window, text = "End")
    drhdr5.grid(column = 6, row = 1)
    #Row 2 Monster Left Behind Each Door
    #Row 3 Radio Buttons
    #Row 4 Monster in Encounter List w/ Submit
    encntr = tkinter.Label(window, text = monsterencounterlist)
    print (monsterencounterlist)
    sbmtbtn = tkinter.Button(window, text = "Submit", command = submit)
    sbmtbtn.grid (column = 5, row = 5)
    
    window.mainloop() #Calls Main GUI

door_Difficulty()
while roundcount < 51:
    round_Counter(roundcount)
    roundcount += 1
