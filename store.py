import json
import random
#list of items with prices, will add the keys to the inventory but only adding 1 at a time
storeItems = {"Can of Fanta": 5,"Candle": 7,"Clock": 12 ,"Geode": 34 ,
            "Ancient Scroll": 78,"Copper hammer": 20 ,"Meteoric Sword": 120,
             "Artifact": 45, "Spriggansoul":  54,"COD": 60 }

def randomGetItem(charInven):
    print("I wish to give an item says the store code")
    randNum = random.randint(1,4)
    randItem = random.randint(1,100)
    
    #might be worth separating the items into rarity types instead of making them all separate, dont need to be ultra specific, will make it look better
    
    if randNum > 2:
        
        #4/100
        if randItem in range(97,100):
            itemGained = "Meteoric Sword"
            pass
            #5
        elif randItem in range(77,81):
            itemGained = "Ancient Scroll"
            pass
            #6
        elif randItem in range(71,76):
            itemGained = "COD"
            pass
            #7
        elif randItem in range(64,70):
            itemGained = "Spriggansoul"
            pass
            #13
        elif randItem in range(51,63):
            itemGained = "Artifact"
            pass
            #17
        elif randItem in range(13,29):
            itemGained = "Copper hammer"
            pass
            #15
        elif randItem in range(1,12):
            itemGained = "Clock"
            pass
            #12
        elif randItem in range(30,41):
            itemGained = "Candle"
            pass
            #9
        elif randItem in range(42,50):
            itemGained = "Can of Fanta"
            pass
            #12
        else:
            itemGained = "Geode"

        print("You found", itemGained, "on your adventures!")
        with open(charInven, "r") as ci:
            char = json.load(ci)
            inventory = char[2]
            firstdict = char[0]
            seconddict = char[1]

            if itemGained in inventory:
                inventory[itemGained] += 1
            else:
                inventory[itemGained] = 1
            
            fulldict = firstdict, seconddict, inventory
            with open(charInven, "w") as cw:
                json.dump(fulldict, cw)

def viewInventory(fileName):
    
    with open(fileName, "r") as mi:
        myInventory = json.load(mi)
        
        for key in myInventory[2]:
            print("You have", key, "x", myInventory[2][key])

def sellItem(charFile, item, amount):
    with open(charFile, "r") as mi:
        myInven = json.load(mi)
    if item in myInven[2] and myInven[2][item] >= int(amount):
        myInven[2][item] -= int(amount)
        price = storeItems[item]
        price = int(price)
        profit = price * int(amount)
        myInven[0]["Coins"] += int(profit)
        print("You sold:", item, "x", amount, "for", profit, "dosh")
        
        if myInven[2][item] <= 0:
            myInven[2].pop(item)
        else:
            pass
        with open(charFile, "w") as wi:
            json.dump(myInven, wi)
    else:
        print("you do not have that item")

#sellallnext?
#things to buy
                

def SellAll(charfile):
    profit = 0
    with open(charfile, "r") as cf:
        sellinventory = json.load(cf)
        for key in list(sellinventory[2]):
            print(key, sellinventory[2][key])
            price = storeItems[key]
            price = int(price)*int(sellinventory[2][key])
            
            profit = profit+price
            
            sellinventory[2].pop(key)
            sellinventory[0]["Coins"] += int(price)
    with open(charfile, "w") as wi:
        json.dump(sellinventory, wi)
    print("You sold it all for", profit)
