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

finalList = [] #create an empty list to store the element of final list

def main(): 
    global finalList

    solve([])

    print(len(finalList)) #print the length of final list
    print("The elements are :") 
    for name in finalList: #search for the name in the final list then print them
        print(name)

def solve(newList): #newList is an empty list

    global finalList
    flag = 0 #hints to track if the conditions are met for the game
    for name in pokeList:   #loop through the names  in the pokemon list
        if((len(newList) == 0) or (name not in newList and (name[0] == newList[-1][-1]))): #check if the newList is empty or if the name is not one of its elments(to avoid repeats) and the first element is = to the last 
            flag =1 #set to 1 if the above conditions are met
            newList.append(name) #add the name to the newlist
            solve(newList)
            newList.pop() #pops the name for backtracking
    

    if(flag == 0): #means that none of the element met the condition 
        if (len(newList) > len(finalList)): #check to compare the size of new and final list. IF yes, then the newlist becomes the final list
            finalList = list(newList)


main();