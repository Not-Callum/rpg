import json

def CreateNew(profile):
    newDict = [{"name": profile, "XP": 0, "level": 1, "Coins": 0},{"work": [12, 1, 0]}, {}]
    newProfile = (profile, ".json")
    newProfile = ("".join(newProfile))
    print(newProfile)
    created = open(newProfile, "x")
    with open(newProfile , "w") as pl:
        json.dump(newDict, pl)

    
def viewLevel(pfl):
    
    with open(pfl , "r") as pl:
        pflLVL = json.load(pl)
        level = pflLVL[0]["level"]
        XP = pflLVL[0]["XP"]
        xpNeeds = round((level/0.07)**2.0)
        print("Your character level is", level, "and your XP amount is:", XP, "/", xpNeeds)
        print("You have", pflLVL[0]["Coins"], "dosh. ")
        for key in pflLVL[1]:
            print("Your skill in",key,"is level", pflLVL[1][key][1])

def addXP(x, pfl, act):
    
    #handles the profile level
    with open(pfl , "r") as pl:
        pflLVL = json.load(pl)
        
        pflLVL[0]["XP"] += x
        totalXP = int(pflLVL[0]["XP"])
        
        totalLVL = float(pflLVL[0]["level"])
        xpNeeded = round((totalLVL/0.07)**2.0)
        if totalXP >= xpNeeded:
            pflLVL[0]["level"] +=1
        else:
            remainingXP = xpNeeded - totalXP
            print("you have", remainingXP, "remaining to level up!")

        #handles the stats level
        pflLVL[1][act][2] += x
        stattotalXP = int(pflLVL[1][act][2])
        
        stattotalLVL = float(pflLVL[1][act][1])
        statxpNeeded = round((stattotalLVL/0.07)**2.0)
        if stattotalXP >= statxpNeeded:
            pflLVL[1][act][1] +=1
        else:
            pass
    
    newLVL = pflLVL
    with open(pfl, "w") as nl:
        json.dump(newLVL, nl)

