#For some reason the source files contains "[x]" in front of ruletext every now and then. Since it only occurs 4 times, it's faster to remove them manually then to write a script for it.

import json
from pprint import pprint
import os
debug = True

try:
    os.remove("sql.txt")
    if debug:
        print("sql.txt removed")
except OSError:
    if debug:
        print("No sql.txt found")
    pass

for i in range(3):

    if i == 0:
        with open('minions.json') as f:
            data = json.load(f)
    elif i == 1:
        with open('spells.json') as f:
            data = json.load(f)
    elif i == 2:
        with open('weapons.json') as f:
            data = json.load(f)
    else:
        print("Error in file opener at index: " + str(i))

    for i in range(len(data)):

        data[i]['name'] = data[i]['name'].replace("'","''")

        if 'text' in data[i].keys():
            if debug:
                print("Before replace():")
                print("data[i]['text'] at Index: " + str(i) + "contains: " + data[i]['text'])
                print(type(data[i]['text']))

            data[i]['text'] = data[i]['text'].replace("'","''")
            data[i]['text'] = data[i]['text'].replace("_"," ")
            data[i]['text'] = data[i]['text'].replace("[x]","")
            data[i]['text'] = data[i]['text'].replace("$", "")
            data[i]['text'] = data[i]['text'].replace("#", "")
            data[i]['text'] = str(data[i]['text'].lstrip())
            if debug:
                print("After replace():")
                print("data[i]['text'] at Index: " + str(i) + "contains: " + data[i]['text'])
        else:
            data[i]['text'] = "NULL"
        if 'health' in data[i].keys():
            print('checked')
        else:
            data[i]['health'] = "NULL"
        if 'attack' in data[i].keys():
            print('checked')
        else:
            data[i]['attack'] = "NULL"
        if 'durability' in data[i].keys():
            print('checked')
        else:
            data[i]['durability'] = "NULL"


        if 'race' in data[i].keys():
            if data[i]['race'] == "All":
                data[i]['race'] = 1
            elif data[i]['race'] == "Beast":
                data[i]['race'] = 2
            elif data[i]['race'] == "Demon":
                data[i]['race'] = 3
            elif data[i]['race'] == "Dragon":
                data[i]['race'] = 4
            elif data[i]['race'] == "Elemental":
                data[i]['race'] = 5
            elif data[i]['race'] == "Mech":
                data[i]['race'] = 6
            elif data[i]['race'] == "Murloc":
                data[i]['race'] = 7
            elif data[i]['race'] == "Pirate":
                data[i]['race'] = 8
            elif data[i]['race'] == "Totem":
                data[i]['race'] = 9
            else:
                print("Error in race parser!")
        else:
            data[i]['race'] = "NULL"


        if data[i]['playerClass'] == "Warrior":
            data[i]['playerClass'] = 1
        elif data[i]['playerClass'] == "Warlock":
            data[i]['playerClass'] = 2
        elif data[i]['playerClass'] == "Neutral":
            data[i]['playerClass'] = 3
        elif data[i]['playerClass'] == "Mage":
            data[i]['playerClass'] = 4
        elif data[i]['playerClass'] == "Priest":
            data[i]['playerClass'] = 5
        elif data[i]['playerClass'] == "Paladin":
            data[i]['playerClass'] = 6
        elif data[i]['playerClass'] == "Hunter":
            data[i]['playerClass'] = 7
        else:
            print("Error in switch case for playerClass!")


        if 'rarity' in data[i].keys():
            print("data[i]['rarity'] = " + data[i]['rarity'] + " At index: " + str(i))
            if data[i]['rarity'] == "Free":
                data[i]['rarity'] = 1
            elif data[i]['rarity'] == "Common":
                data[i]['rarity'] = 2
            elif data[i]['rarity'] == "Rare":
                data[i]['rarity'] = 3
            elif data[i]['rarity'] == "Epic":
                data[i]['rarity'] = 4
            elif data[i]['rarity'] == "Legendary":
                data[i]['rarity'] = 5
            else:
                print("Error in switch case for rarity! At index: " + str(i))
        else:
            data[i]['rarity'] = 1

        if data[i]['type'] == 'Minion':
            data[i]['type'] = 1
        elif data[i]['type'] == "Spell":
            data[i]['type'] = 2
        elif data[i]['type'] == "Weapon":
            data[i]['type'] = 3
        else:
            print("Error in type filtering!")

        if 'collectible' in data[i].keys():
            print("collectible checked")
        else:
            data[i]['collectible'] = "false"

        

        preparedStatement = "INSERT INTO cards (cardName, cost, health, attack, durability, ruleText, baseImg, classId, minionType, rarity, cardType, collectible) VALUES (" + "\'" + str(data[i]['name']) + "\'," + str(data[i]['cost']) +","+ str(data[i]['health'])+","+ str(data[i]['attack'])+","+ str(data[i]['durability'])+",\'"+ str(data[i]['text'])+"\',\'"+ str(data[i]['img'])+"\',"+ str(data[i]['playerClass'])+","+ str(data[i]['race'])+","+ str(data[i]['rarity'])+","+ str(data[i]['type'])+",\'"+ str(data[i]['collectible'])+"\');"

        with open('sql.txt', 'a') as the_file:

            the_file.write(preparedStatement + '\n')

    f.close()




