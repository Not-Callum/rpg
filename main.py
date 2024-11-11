
import json
import time
import character
import os
import store
from threading import Timer
gameOn = False

#open personal file
name = input("Who are you? ")
fileName = (name, ".json")
fileName = ("".join(fileName))
#makes sure the file exists and then loads it if found
if os.path.isfile(fileName):
    with open(fileName, "r") as prfl:
        activities = json.load(prfl)
        activities = activities[1]
    print("ah! there you are")
    gameOn = True
#uh oh! the file didnt exist, silly sausage, time to make one for you
else:
    if input("Do you want to make this a new profile?(y/n) ") == "y":
        character.CreateNew(name)
        with open(fileName, "r") as prfl:
            activities = json.load(prfl)
            activities = activities[1]
        gameOn = True
    else:
        quit()

def workActive(workDoing):
    print("You've started work on", workDoing)
    xpPM = int(activities[workDoing][0])
    startTime = time.time()
    user_input = input("Enter something if you wanna stop lol: ")
    endTime = time.time()
    timeWorked = endTime - startTime
    timeWorked = round(timeWorked)
    print(timeWorked)
    #calculates xp given based on how long we worked (per minute)
    if round(timeWorked)/60 >=1:
        xpAdded = round(timeWorked/60)*xpPM
        #adds the xp gained
        character.addXP(xpAdded, fileName, workDoing)
        for i in range(round(timeWorked/60)):
            print(i, "is the name, giving items is the game!")
            
            store.randomGetItem(fileName)
    #L Bozo
    else:
        print("you did not work long enough for xp")

#loops while the game is running
while gameOn == True:
    
    #i wonder what this does it's so hard to tell (it lets you see your level)
    whatDoing = input("Do you wish to: 1: Look at level? 2: Start Work? or 3: visit the store? (anything else to quit) ")
    if  whatDoing == "1":
        character.viewLevel(fileName)
        
    #no one truly wants to start working 
    elif whatDoing == "2":
        workDoing = input("what are you working on?(name activity) ")
        #makes sure the activity exists
        if workDoing in activities:
            workActive(workDoing)

        

        else:
            #that activity didnt exist so we're gonna make a new one and set it up together
            if input("Not found :( do you wish to make this a new activity?(y/n)") == "y":
                #decision for amount of xp it should reward
                difficulty = input("How difficult is this activity to perform?(easy,medium,hard)")
                if difficulty == ("easy" or "Easy"):
                    amountOfXP = 5
                elif difficulty == ("medium" or "Medium"):
                    amountOfXP = 12
                elif difficulty == ("hard" or "Hard"):
                    amountOfXP = 20
                activities[workDoing] = [amountOfXP, 1, 0]
                #I didnt learn how to properly code opening the file and making only one change to a certain part of it, poor baby me but it works
                
                with open(fileName , "r") as fp:
                    wholeDict = json.load(fp)
                    firstDict = wholeDict[0]
                    lastDict = wholeDict[2]
                    reformDict = firstDict, activities, lastDict
                with open(fileName, "w") as fp:
                    json.dump(reformDict, fp)
                workActive(workDoing)
            else:
                print("okay :)")
    #asks if you wanna visit the store
    elif whatDoing == "3":
        store.viewInventory(fileName)
        inStore = True
        #just to loop in case you feel like it
        while inStore == True:
            storeAns = input("Do you want to sell your items?(y/n/sellall) ")
            if storeAns == "y":
                itemToSell = input("Which item do you want to sell? (spelling is important) ")
                amountToSell = input("How much do you want to sell?")
                store.sellItem(fileName, itemToSell, amountToSell)
            elif storeAns == "sellall":
                store.SellAll(fileName)
            
            else:
                inStore = False
    else:
        gameOn = False

while gameOn == False:
    print("Goodbye!")
    quit()

#ideas for expansion
#Inventory in character file as separate dictionary, also coins as part of the first dictionary in character files :done
#Randomised rewards with different ways of getting them such as "found a diamond ring in chest" :doneish
#shop, can sell these rewards for dosh which can be spent on upgrades or irl things, probably best done in a separate file for organisation sake :doneish