#mozart.py
#Alejandro Belgrave

import random
import soundwave

def makeMinuet(mTable):
    try:
        minue = []
        minuet = soundwave.Soundwave()
        measures = 16
        for m in range(measures):
            snippet = random.randint(0,10)
            minue.append(mTable[snippet][m])
            notes = soundwave.Soundwave("../Mfiles/M" +str(mTable[snippet][m]) + ".wav")
            minuet.concat(notes)
        return minuet
    except IOError:
        print("Please check that you are refrencing the correct file in your code")

def makeTrio(tTable):
    try:
        tri = []
        trio = soundwave.Soundwave()
        measures = 16
        for m in range(measures):
            snippet = random.randint(0,5)
            tri.append(tTable[snippet][m])
            notes = soundwave.Soundwave("../Tfiles/T" +str(tTable[snippet][m]) + ".wav")
            trio.concat(notes)
        return trio
    except IOError:
        print("Please check that you are refrencing the correct file in your code")

def combine(minuet, trio):
    soul = soundwave.Soundwave()
    soul.concat(minuet)
    soul.concat(trio)
    soul.concat(minuet)

    return soul

def main():
    try:
        #open and parse the tables
        mInput = open("mTable.txt", "r")
        mTable = []
        for row in mInput:
            mTable.append(row.split())
        
        tInput = open("tTable.txt", "r")
        tTable = []
        for row in tInput:
            tTable.append(row.split())
    
        #create full minuet and trio
        minuet = makeMinuet(mTable)
        #minuet.play()
        trio = makeTrio(tTable)
        #trio.play()
    
        #concat errthang
        music = combine(minuet, trio)
        music.play()
    except IOError:
        print("Please check that you are refrencing the correct file in your code")

main()