import random
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
defeated = 0
#doubles
bnsscore = 0
mnstscore = 0
rndscore = 0
finalscore = 0
#boolean
common = True
#Randomizes door order coming out
def randomize_Monsters():
    random.shuffle(doorone)
    random.shuffle(doortwo)
    random.shuffle(doorthr)
    random.shuffle(doorfor)
    random.shuffle(doorfiv)
#Checks if doordifficulty is equal to 0 then door order is 1-5. Else door order is 5-1
def door_Difficulty():
    global doorone, doortwo, doorthr, doorfor, doorfiv, common
    randomize_Monsters()
    if doordifficulty != 0:
        common = False
        tempdoor = doorone
        doorone = doorfiv
        doorfiv = tempdoor
        tempdoor = doortwo
        doortwo = doorfor
        doorfor = tempdoor
        del tempdoor
#Prompts user for door 1, 2, 3, 4, or 5. Removes first monster from the respective list based on user prompt
def select_Door(userinput):
    global monsterencounterlist, common
    if userinput == 1 and len(doorone) >= 1:
        temp = doorone.pop(0)
        if common:
            monsterencounterlist[temp] = 0.8
        else:
            monsterencounterlist[temp] = 1.8
        print (temp)
        del temp
    elif userinput == 2 and len(doortwo) >= 1:
        temp = doortwo.pop(0)
        if common:
            monsterencounterlist[temp] = 1.2
        else:
            monsterencounterlist[temp] = 1.5
        print (temp)
        del temp
    elif userinput == 3 and len(doorthr) >= 1:
        temp = doorthr.pop(0)
        monsterencounterlist[temp] = 1.4
        print (temp)
        del temp
    elif userinput == 4 and len(doorfor) >= 1:
        temp = doorfor.pop(0)
        if common:
            monsterencounterlist[temp] = 1.5
        else:
            monsterencounterlist[temp] = 1.2
        print (temp)
        del temp
    elif userinput == 5 and len(doorfiv) >= 1:
        temp = doorfiv.pop(0)
        if common:
            monsterencounterlist[temp] = 1.8
        else:
            monsterencounterlist[temp] = 0.8
        print (temp)
        del temp
    elif userinput == 10:
        sys.exit('End')
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
        end_Encounter(counter)
    else:
        next_Round(counter)
#Round one. Keeps track of arrows, monsters etc
def round_One():
    #GUI
    window = tkinter.Tk()
    window.title("GUI")
    header = tkinter.Label(window, text = "Round 1, Release Monsters").grid(column = 3, row = 0)
    #Row 1 Door Titles
    drhdr1 = tkinter.Label(window, text = "Door 1").grid(column = 1, row = 1)
    drhdr2 = tkinter.Label(window, text = "Door 2").grid(column = 2, row = 1)
    drhdr3 = tkinter.Label(window, text = "Door 3").grid(column = 3, row = 1)
    drhdr4 = tkinter.Label(window, text = "Door 4").grid(column = 4, row = 1)
    drhdr5 = tkinter.Label(window, text = "Door 5").grid(column = 5, row = 1)
    #Pull Images
    up = tkinter.PhotoImage(file = "Arrow_Up.png")
    down = tkinter.PhotoImage(file = "Arrow_Down.png")
    def incrmt_Arrow(idx):
        global mnstcntr1, mnstcntr2, mnstcntr3, mnstcntr4, mnstcntr5
        if idx == 1 and mnstcntr1 < 5:
            mnstcntr1 += 1
            mnstcntrlbl1.configure(text = mnstcntr1)
        elif idx == 2 and mnstcntr2 < 4:
            mnstcntr2 += 1
            mnstcntrlbl2.configure(text = mnstcntr2)
        elif idx == 3 and mnstcntr3 < 3:
            mnstcntr3 += 1
            mnstcntrlbl3.configure(text = mnstcntr3)
        elif idx == 4 and mnstcntr4 < 4:
            mnstcntr4 += 1
            mnstcntrlbl4.configure(text = mnstcntr4)
        elif idx == 5 and mnstcntr5 < 5:
            mnstcntr5 += 1
            mnstcntrlbl5.configure(text = mnstcntr5)
    #Row 2 Up Buttons. Increase the count for respective door
    bt1Up = tkinter.Button(window, height=50, width=50, image = up, command = lambda idx = 1: incrmt_Arrow(idx)).grid (column = 1, row = 2)
    bt2Up = tkinter.Button(window, height=50, width=50, image = up, command = lambda idx = 2: incrmt_Arrow(idx)).grid (column = 2, row = 2)
    bt3Up = tkinter.Button(window, height=50, width=50, image = up, command = lambda idx = 3: incrmt_Arrow(idx)).grid (column = 3, row = 2)
    bt4Up = tkinter.Button(window, height=50, width=50, image = up, command = lambda idx = 4: incrmt_Arrow(idx)).grid (column = 4, row = 2)
    bt5Up = tkinter.Button(window, height=50, width=50, image = up, command = lambda idx = 5: incrmt_Arrow(idx)).grid (column = 5, row = 2)
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
    def dcrmnt_Arrow(idx):
        global mnstcntr1, mnstcntr2, mnstcntr3, mnstcntr4, mnstcntr5
        if idx == 1 and mnstcntr1 > 0:
            mnstcntr1 -= 1
            mnstcntrlbl1.configure(text = mnstcntr1)
        elif idx == 2 and mnstcntr2 > 0:
            mnstcntr2 -= 1
            mnstcntrlbl2.configure(text = mnstcntr2)
        elif idx == 3 and mnstcntr3 > 0:
            mnstcntr3 -= 1
            mnstcntrlbl3.configure(text = mnstcntr3)
        elif idx == 4 and mnstcntr4 > 0:
            mnstcntr4 -= 1
            mnstcntrlbl4.configure(text = mnstcntr4)
        elif idx == 5 and mnstcntr5 > 0:
            mnstcntr5 -= 1
            mnstcntrlbl5.configure(text = mnstcntr5)
    #Row 4 Down Buttons. Decrease the count for respective door
    bt1Dwn = tkinter.Button(window, height=50, width=50, image = down, command = lambda idx = 1: dcrmnt_Arrow(idx)).grid (column = 1, row = 4)
    bt2Dwn = tkinter.Button(window, height=50, width=50, image = down, command = lambda idx = 2: dcrmnt_Arrow(idx)).grid (column = 2, row = 4)
    bt3Dwn = tkinter.Button(window, height=50, width=50, image = down, command = lambda idx = 3: dcrmnt_Arrow(idx)).grid (column = 3, row = 4)
    bt4Dwn = tkinter.Button(window, height=50, width=50, image = down, command = lambda idx = 4: dcrmnt_Arrow(idx)).grid (column = 4, row = 4)
    bt5Dwn = tkinter.Button(window, height=50, width=50, image = down, command = lambda idx = 5: dcrmnt_Arrow(idx)).grid (column = 5, row = 4)
    #Row 5 Exit/Submit. Exits the system or submits counters
    def exit():
        sys.exit('End')
        window.destroy()
    exitbtn = tkinter.Button(window, text = "Exit", command = exit)
    exitbtn.grid (column = 1, row = 5)
    def submit():
        global bnsscore
        opendoor1_5 = mnstcntr1 + mnstcntr5
        if (opendoor1_5 == 1 or opendoor1_5 == 9):
            bnsscore = bnsscore + 1.2
        elif (opendoor1_5 == 2 or opendoor1_5 == 8):
            bnsscore = bnsscore + 1.8
        elif (opendoor1_5 == 3):
            bnsscore = bnsscore + 2.4
        elif (opendoor1_5 == 4):
            bnsscore = bnsscore + 3.0
        elif (opendoor1_5 == 5):
            bnsscore = bnsscore + 3.6
        elif (opendoor1_5 == 6):
            bnsscore = bnsscore + 4.4
        elif (opendoor1_5 == 7):
            bnsscore = bnsscore + 2.4
        elif (opendoor1_5 == 10):
            bnsscore = bnsscore + 1.0
        opendoor2_4 = mnstcntr2 + mnstcntr4
        if (opendoor2_4 == 1):
            bnsscore = bnsscore + 1.1
        elif (opendoor2_4 == 2 or opendoor2_4 == 8):
            bnsscore = bnsscore + 1.8
        elif (opendoor2_4 == 3 or opendoor2_4 == 7):
            bnsscore = bnsscore + 2.6
        elif (opendoor2_4 == 4 or opendoor2_4 == 6):
            bnsscore = bnsscore + 3.2
        elif (opendoor2_4 == 5):
            bnsscore = bnsscore + 4.4
        if (mnstcntr3 == 1):
            bnsscore = bnsscore + 1.6
        elif (mnstcntr3 == 2):
            bnsscore = bnsscore + 2.6
        elif (mnstcntr3 == 3):
            bnsscore = bnsscore + 3.2
        monsters_Entered(mnstcntr1, mnstcntr2, mnstcntr3, mnstcntr4, mnstcntr5)
        window.destroy()
    sbmtbtn = tkinter.Button(window, text = "Submit", command = submit)
    sbmtbtn.grid (column = 5, row = 5)
        
    window.mainloop() #Calls Main GUI
def next_Round(rnd):
    zero = 0
    one = 1
    def show_Number(idx):
        if idx == 1 and bt1.cget('text') == zero:
            bt1.configure(text = one)
            bt2.configure(text = zero)
            bt3.configure(text = zero)
            bt4.configure(text = zero)
            bt5.configure(text = zero)
        elif idx == 1:
            bt1.configure(text = zero)
            bt2.configure(text = zero)
            bt3.configure(text = zero)
            bt4.configure(text = zero)
            bt5.configure(text = zero)
        elif idx == 2 and bt2.cget('text') == zero:
            bt1.configure(text = zero)
            bt2.configure(text = one)
            bt3.configure(text = zero)
            bt4.configure(text = zero)
            bt5.configure(text = zero)
        elif idx == 2:
            bt1.configure(text = zero)
            bt2.configure(text = zero)
            bt3.configure(text = zero)
            bt4.configure(text = zero)
            bt5.configure(text = zero)
        elif idx == 3 and bt3.cget('text') == zero:
            bt1.configure(text = zero)
            bt2.configure(text = zero)
            bt3.configure(text = one)
            bt4.configure(text = zero)
            bt5.configure(text = zero)
        elif idx == 3:
            bt1.configure(text = zero)
            bt2.configure(text = zero)
            bt3.configure(text = zero)
            bt4.configure(text = zero)
            bt5.configure(text = zero)
        elif idx == 4 and bt4.cget('text') == zero:
            bt1.configure(text = zero)
            bt2.configure(text = zero)
            bt3.configure(text = zero)
            bt4.configure(text = one)
            bt5.configure(text = zero)
        elif idx == 4:
            bt1.configure(text = zero)
            bt2.configure(text = zero)
            bt3.configure(text = zero)
            bt4.configure(text = zero)
            bt5.configure(text = zero)
        elif idx == 5 and bt5.cget('text') == zero:
            bt1.configure(text = zero)
            bt2.configure(text = zero)
            bt3.configure(text = zero)
            bt4.configure(text = zero)
            bt5.configure(text = one)
        else:
            bt1.configure(text = zero)
            bt2.configure(text = zero)
            bt3.configure(text = zero)
            bt4.configure(text = zero)
            bt5.configure(text = zero)
    def exit():
        end_Encounter(rnd)
        window.destroy()
    def submit():
        if bt1.cget('text') == one:
            select_Door(1)
            encntr.configure(text = monsterencounterlist)
            window.destroy()
        elif bt2.cget('text') == one:
            select_Door(2)
            encntr.configure(text = monsterencounterlist)
            window.destroy()
        elif bt3.cget('text') == one:
            select_Door(3)
            encntr.configure(text = monsterencounterlist)
            window.destroy()
        elif bt4.cget('text') == one:
            select_Door(4)
            encntr.configure(text = monsterencounterlist)
            window.destroy()
        elif bt5.cget('text') == one:
            select_Door(5)
            encntr.configure(text = monsterencounterlist)
            window.destroy()
        else:
            select_Door(6)
            window.destroy()   
    #GUI
    window = tkinter.Tk()
    window.title("GUI")
    header = tkinter.Label(window, text = "New round, release a monster from a door?").grid(column = 3, row = 0)
    #Row 1 Door Titles
    drhdr1 = tkinter.Label(window, text = "Door 1").grid(column = 1, row = 1)
    drhdr2 = tkinter.Label(window, text = "Door 2").grid(column = 2, row = 1)
    drhdr3 = tkinter.Label(window, text = "Door 3").grid(column = 3, row = 1)
    drhdr4 = tkinter.Label(window, text = "Door 4").grid(column = 4, row = 1)
    drhdr5 = tkinter.Label(window, text = "Door 5").grid(column = 5, row = 1)
    #Row 2 Radio Buttons
    bt1 = tkinter.Button(window, command = lambda idx = 1: show_Number(idx), text = zero)
    bt1.grid (column = 1, row = 2)
    bt2 = tkinter.Button(window, command = lambda idx = 2: show_Number(idx), text = zero)
    bt2.grid (column = 2, row = 2)
    bt3 = tkinter.Button(window, command = lambda idx = 3: show_Number(idx), text = zero)
    bt3.grid (column = 3, row = 2)
    bt4 = tkinter.Button(window, command = lambda idx = 4: show_Number(idx), text = zero)
    bt4.grid (column = 4, row = 2)
    bt5 = tkinter.Button(window, command = lambda idx = 5: show_Number(idx), text = zero)
    bt5.grid (column = 5, row = 2)
    #Row 3 Monster Left Behind Each Door
    rmn1 = len(doorone), "left"
    rmn2 = len(doortwo), "left"
    rmn3 = len(doorthr), "left"
    rmn4 = len(doorfor), "left"
    rmn5 = len(doorfiv), "left"
    cnt1 = tkinter.Label(window, text = rmn1).grid(column = 1, row = 3)
    cnt2 = tkinter.Label(window, text = rmn2).grid(column = 2, row = 3)
    cnt3 = tkinter.Label(window, text = rmn3).grid(column = 3, row = 3)
    cnt4 = tkinter.Label(window, text = rmn4).grid(column = 4, row = 3)
    cnt5 = tkinter.Label(window, text = rmn5).grid(column = 5, row = 3)
    #Row 4 Monster in Encounter List w/ Submit
    extbtn = tkinter.Button(window, text = "End", command = exit).grid (column = 1, row = 4)
    encntr = tkinter.Label(window, text = monsterencounterlist)
    encntr.grid (column = 3, row = 4)
    sbmtbtn = tkinter.Button(window, text = "Submit", command = submit)
    sbmtbtn.grid (column = 5, row = 4)
    window.mainloop() #Calls Main GUI
def defeated_Enemies():
    #GUI
    window1 = tkinter.Tk()
    window1.title("GUI")
    header1 = tkinter.Label(window1, text = "How many monsters were defeated?").grid(column = 3, row = 0)
    #Row 1 Monster in Encounter List
    encntr1 = tkinter.Label(window1, text = monsterencounterlist).grid (column = 3, row = 1)
    #Row 2 User Input Box
    entrybox1 = tkinter.Entry(window1)
    entrybox1.grid(column = 3, row = 2)
    #Row 3 End Encount & Submit
    extbtn1 = tkinter.Button(window1, text = "End", command = window1.destroy).grid (column = 1, row = 3)
    def submit1():
        global defeated
        defeated = int(entrybox1.get())
        #GUI
        window2 = tkinter.Tk()
        window2.title("GUI")
        header2 = tkinter.Label(window2, text = "Which monster in the list was defeated?").grid(column = 3, row = 0)
        #Row 1 Monster in Encounter List
        encntr2 = tkinter.Label(window2, text = monsterencounterlist)
        encntr2.grid (column = 3, row = 1)
        #Row 2 User Input Box
        entrybox2 = tkinter.Entry(window2)
        entrybox2.grid(column = 3, row = 2)
        def submit2():
            global defeated, mnstscore, monsterencounterlist
            if defeated > 1:
                tempscore = monsterencounterlist.pop(entrybox2.get())
                if tempscore > 0:
                    mnstscore = mnstscore + tempscore
                    del tempscore
                    defeated -= 1
                    encntr2.configure(text = monsterencounterlist)
            else:
                tempscore = monsterencounterlist.pop(entrybox2.get())
                if tempscore > 0:
                    mnstscore = mnstscore + tempscore
                    del tempscore
                    defeated -= 1
                    encntr2.configure(text = monsterencounterlist)
                window2.destroy()
                window1.destroy()
        #Row 3 End Encount & Submit
        extbtn2 = tkinter.Button(window2, text = "End", command = window2.destroy).grid (column = 1, row = 3)
        sbmtbtn2 = tkinter.Button(window2, text = "Submit", command = submit2)
        sbmtbtn2.grid (column = 5, row = 3)
        window2.mainloop() #Calls Main GUI
    sbmtbtn1 = tkinter.Button(window1, text = "Submit", command = submit1).grid (column = 5, row = 3)
    window1.mainloop() #Calls Main GUI
#When hit round 50 with surviving monsters and players
def encounter_End(rnd):
    global finalscore, bnsscore, mnstscore, rndscore
    rndscore = 3
    finalscore = bnsscore + mnstscore + rndscore
    print ("Team Bonus Score:", bnsscore)
    print ("Team Monster Score:", mnstscore)
    print ("Team Round Score:", rndscore)
    print ("Team Final Score:", finalscore)
#When hit round 1-50 and the battle ends
def end_Encounter(rnd):
    global finalscore, bnsscore, mnstscore, rndscore, roundcount, defeated, monsterencounterlist
    if (rnd == 1 or rnd <= 5):
        rndscore = 10
        while len(monsterencounterlist) > 0:
            tempscore = monsterencounterlist.popitem()
            mnstscore = mnstscore + tempscore[1]
    elif (rnd > 5 and rnd <= 25):
        rndscore = ((25 - rnd) / 10) + 8
        while len(monsterencounterlist) > 0:
            tempscore = monsterencounterlist.popitem()
            mnstscore = mnstscore + tempscore[1]
    elif (rnd > 25 and rnd < 50):
        rndscore = (((50 - rnd) * 2) / 10) + 3
        while len(monsterencounterlist) > 0:
            tempscore = monsterencounterlist.popitem()
            mnstscore = mnstscore + tempscore[1]
    finalscore = mnstscore + rndscore + bnsscore
    print ("Team Bonus Score:", bnsscore)
    print ("Team Monster Score:", mnstscore)
    print ("Team Round Score:", rndscore)
    print ("Team Final Score:", finalscore)
    roundcount = 51
def main():
    global roundcount
    door_Difficulty()
    while roundcount < 51:
        if roundcount%5 == 0:
            defeated_Enemies()
            round_Counter(roundcount)
            roundcount += 1
        else:
            round_Counter(roundcount)
            roundcount += 1
