import math
import random
import time
import os
from colorama import Fore, Back, Style
import EditChoice as E


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
        options = AddChoice(options, winRate)
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



def MainMenu(options, winRate):
    global winingStatistics
    while True:
        ans = input("Type:\n'1' To run the program.\n'2' To edit the options.\n'3' For win rate and statistics\n'4' For options history\n'5' For reset options.\n'6' For choosing favored option.\n")
        match ans:
            case '1':
                currentChoice, options = PickActivity(options, winRate)
                break
            case '2':
                options = EditChoice(options, winRate)
            case '3':
                print(winRate)
                print(winingStatistics)
            case '4':
                print(optionsHistory)
            case '5':
                if os.path.isfile("options.txt"):
                    print("hi")
                    os.remove("options.txt")

                else:
                    options = {}
                winingStatistics = {}
                winRate = None
                MainMenu(options, winRate)
            case '6':
                Favored(options)
    return currentChoice, options

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
        #time.sleep(5)
    for x in options:
        options[x] = 0
    size = int(math.log2(len(options)))
    for i in reversed(range(len(chosenActivityLog))):
        currentActivity = chosenActivityLog[i]
        if currentActivity in options:
            minusForWinner = 0
            while i >= 0:
                if chosenActivityLog[i] == chosenActivityLog[i - 1]:
                    minusForWinner += 1
                    i -= 1
                else:
                    break
            options[currentActivity] = options[currentActivity] - size - minusForWinner
            size -= 1
            if size <= 0:
                break

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

def AddChoice(options, winRate=None):
    option = ""
    while option != "q":
        if options is not {}:
            Show(options)
        option = input("Enter an option to add, type 'q' to go to main menu.\n")
        if option not in options and option != "q":
            options[option] = 0
            winRate[option] = 0
            print(option + " was added successfully.")
            if option not in winingStatistics:
                winingStatistics[option] = 0
            optionsHistory.append("add:" + option)
        else:
            print("The option is already in the pool.")
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
        if outputList is not []:
            print("your options are: " + str(outputList))

def Favored(options):
    global favoredChoice
    while True:
        Show(options)
        ans = input("Here you can add a favored option for the next run of the program, There can be only 1 favored choice at a time!\nJust write your favored option and we will make it more likly to win\n")
        if ans not in options:
            print("The option is not in the pool, Please enter one that is.\n")
        else:
            favoredChoice = ans
            break
