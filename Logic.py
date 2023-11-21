import math
import random
import time
import os
from colorama import Fore, Back, Style

favoredChoice = None
winingStatistics = {}
chosenActivityLog = []
optionsHistory = []
def UpdateFile():
    global optionsHistory, winingStatistics, chosenActivityLog
    if not os.path.isfile("options.txt"):
        options = {}
        winRate = {}
        formerActivity = ""
        options = Initialize(options, winRate)
    else:
        fileRead = open("options.txt", "r")
        content = fileRead.readlines()
        options = eval((content[0]).split("= ")[1])
        winRate = eval((content[2]).split("= ")[1])
        if content[3] != [] and content[4] != []:

            optionsHistory = content[3].split("= ")[1]
            optionsHistory = optionsHistory[1:-2].replace("'","").split(", ")
            chosenActivityLog = content[4].split("= ")[1][1:-2].replace("'","").split(", ")
            print("the chosenActivityLog before all: ", chosenActivityLog)
        winingStatistics = eval(content[5].split("= ")[1])
        fileRead.close()
    choice, options = MainMenu(options, winRate)
    if choice == None:
        optionsHistory = []
        chosenActivityLog = []
        UpdateFile()
        return
    f = open("options.txt", "w")

    winRate.keys
    list = ["The options are = " + str(options) ,'\n' ,"Former activity = " + choice ,'\n', "choice's score = " + str(winRate) ,'\n',"History of changes in options = "  + str(optionsHistory),'\n',"Chosen activity log = " + str(chosenActivityLog),'\n',"Wining statistics = " + str(winingStatistics)]
    f.writelines(list)
    f.close()

def Favored(options):
    global favoredChoice
    while True:
        Show(options)
        ans = input("here you can add a favored option for the next run of the program, there can be only 1 favored choice at a time!\njust write your favored option and we will make it more likly to win\n")
        if ans not in options:
            print("the option is not in the pool, please enter one that is.\n")
        else:
            favoredChoice = ans
            break

def MainMenu(options, winRate):
    while True:
        ans = input("Type:\n'1' to run the progrem.\n'2' to edit the options.\n'3' for statistics\n'4' for options history\n'5' for reset options.\n'6' for choosing favored option.\n")
        match ans:
            case '1':
                currentChoice, options = PickActivity(options, winRate)
                break
            case '2':
                options = EditChoice(options, winRate)
            case '3':
                print(winRate)
            case '4':
                print(optionsHistory)
            case '5':
                if os.path.isfile("options.txt"):
                    os.remove("options.txt")
                return None,None
            case '6':
                Favored(options)
    return currentChoice, options

def Initialize(options, winRate=None):
    firstOption = input("Enter your first option to add\n")
    options[firstOption] = 0
    winRate[firstOption] = 0
    winingStatistics[firstOption] = 0
    optionsHistory.append("add:" + firstOption)
    return options
def PickActivity(options, winRate=None):
    global favoredChoice
    if favoredChoice is not None:
        options[favoredChoice] += 1
    print("starting score is: ",options)
    counter = 1
    while True:
        currentChoice = random.choice(list(options.keys()))
        print(f"roll number: {counter}")
        print("chosen: " + Fore.BLUE + currentChoice)
        print(Style.RESET_ALL)
        counter += 1
        options[currentChoice] += 1
        if options[currentChoice] == 5:
            print("The choice that has been made is:" + Fore.GREEN + currentChoice)
            print(Style.RESET_ALL)
            favoredChoice = None
            chosenActivityLog.append(currentChoice)
            winRate[currentChoice] += 1
            for keys in winRate:
                winingStatistics[keys] = "{:.1f}".format((winRate[keys] / len(chosenActivityLog)) * 100) + "%"
            break
        print("Current score is: ",options)
        time.sleep(5)
    for x in options:
        options[x] = 0
    counter = int(math.log2(len(options)))
    for activity in reversed(chosenActivityLog):
        if counter <= 0:
            break
        if activity in options:
            if options[activity] == 0:
                options[activity] = -counter
                counter -= 1

    return currentChoice,options
def EditChoice(options, winRate=None):
    while True:
        ans = input("edit options, type:\n'1' to add an option\n'2' to remove an option\n'3' to replace an option\n'4' back to main menu\n")
        match ans:
            case '1':
                options = AddChoice(options, winRate)
            case '2':
                options = RemoveChoice(options)
            case '3':
                options = replaceChoice(options, winRate)
            case '4':
                break
    return options
def replaceChoice(options, winRate=None):
    Show(options)
    unwantedChoice = input("enter the option you would like to replace:\n")
    if unwantedChoice not in options:
        print("the option is not in the list so it cant be replaced")
    else:
        wantedChoice = input("Enter the desired option:\n")
        if wantedChoice in options:
            print("the option is already in the list")
        else:
            options[wantedChoice] = 0
            winRate[wantedChoice] = 0
            if wantedChoice not in winingStatistics:
                winingStatistics[wantedChoice] = 0
            optionsHistory.append(unwantedChoice + "->replaced-by:" + wantedChoice)
            del options[unwantedChoice]
    return options
def AddChoice(options, winRate={}):
    option = input("Enter option:\n")
    print("the option is: " + option)
    if option not in options:
        options[option] = 0
        winRate[option] = 0
        if option not in winingStatistics:
            winingStatistics[option] = 0
        optionsHistory.append("add:" + option)
    else:
        print("The option is already in the pool\n")
    return options
def RemoveChoice(options):
        Show(options)
        option = input("Enter option to remove:\n")
        if option in options:
            print("the removed activity is: " + option)
            optionsHistory.append("remove:" + option)
            del options[option]
        else:
            print("the activity does not exist, please chose one from the list.")
            optionsHistory.append(option)
            RemoveChoice(options)
        return options
def Show(dict):
    outputList = []
    for key in dict.keys():
        outputList.append(key)
    print(outputList)


