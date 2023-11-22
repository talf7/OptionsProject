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
        options = E.AddChoice(options, winRate)
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
        ans = input("Type:\n'1' To run the progrem.\n'2' To edit the options.\n'3' For win rate and statistics\n'4' For options history\n'5' For reset options.\n'6' For choosing favored option.\n")
        match ans:
            case '1':
                currentChoice, options = PickActivity(options, winRate)
                break
            case '2':
                options = E.EditChoice(options, winRate)
            case '3':
                print(winRate)
                print(winingStatistics)
            case '4':
                print(optionsHistory)
            case '5':
                if os.path.isfile("options.txt"):
                    os.remove("options.txt")
                    winingStatistics = {}
                return None,None
            case '6':
                E.Favored(options)
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
            options[currentActivity] -= size - minusForWinner
            size -= 1
            if size <= 0:
                break

    return currentChoice,options


