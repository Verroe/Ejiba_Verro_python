# -*- coding: utf-8 -*-
"""
Created on Fri Sep 16 18:34:56 2016

@author: verroejiba
"""
    """
    Given a list of possible names, this function generates the/a sequence with
    the highest possible number of Pokemon names where the subsequent name 
    starts with the final letter of the preceding name. No Pokemon name is to
    be repeated. 
    """
pokeList = ["audino","bagon","baltoy","banette","bidoof", "braviary", "bronzor", 
"carracosta","charmeleon","cresselia", "croagunk", "darmanitan", "deino", "emboar", 
"emolga", "exeggcute", "gabite", "girafarig", "gulpin", "haxorus", "heatmor", 
"heatran", "ivysaur", "jellicent", "jumpluff", "kangaskhan","kricketune", "landorus", 
"ledyba", "loudred", "lumineon", "lunatone", "machamp", "magnezone", "mamoswine",
"nosepass", "petilil", "pidgeotto", "pikachu", "pinsir", "poliwrath", "poochyena", 
"porygon2", "porygonz", "registeel", "relicanth", "remoraid", "rufflet", "sableye", 
"scolipede", "scrafty", "seaking", "sealeo", "silcoon", "simisear", "snivy", 
"snorlax", "spoink", "starly", "tirtouga", "trapinch", "treecko","tyrogue", 
"vigoroth", "vulpix", "wailord", "wartortle","whismur","wingull" ,"yamask"]

finalList = []

def main(): #
    global finalList

    solve([])

    print(len(finalList)) # 
    print("The elements are :") # 
    for name in finalList:
        print(name)

def solve(newList): #

    global finalList
    flag = 0
    for name in pokeList:
        if((len(newList) == 0) or (name not in newList and (name[0] == newList[-1][-1]))): #
            flag =1
            newList.append(name)
            solve(newList)
            newList.pop()
    

    if(flag == 0): #
        if (len(newList) > len(finalList)): #
            finalList = list(newList)


main();