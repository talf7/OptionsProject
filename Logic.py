import random
import time
import os

favoredChoice = None
winingStatistics = {}
chosenActivityLog = []
optionsHistory = []


def UpdateFile():
    if not os.path.isfile("options.txt"):
        options = {}
        winRate = {}
        formerActivity = ""
        options = Initialize(options, winRate)
    else:
        fileRead = open("options.txt", "r")
        content = fileRead.readlines()
        options = eval(content[0].split("=")[1])
        formerActivity = content[1].split("=")[1][0:-1]
        winRate = eval(content[2].split("=")[1])
        global optionsHistory, chosenActivityLog, winingStatistics
        optionsHistory = str(content[3].split("=")[1])[1:-2].replace("'","").replace(" ","").split(",")
        chosenActivityLog = content[4].split("=")[1][1:-2].replace("'","").replace(" ","")
        chosenActivityLog = "".join(chosenActivityLog.split()).split(",")
        winingStatistics = eval(content[5].split("=")[1])
        fileRead.close()
    choice, options = MainMenu(options, winRate, formerActivity)
    if choice == None:
        optionsHistory = []
        chosenActivityLog = []
        UpdateFile()
        return
    f = open("options.txt", "w")
    print("Activity wining score: " + str(winRate))

    winRate.keys
    list = ["The options are = " + str(options) ,'\n',"Former activity = " + choice ,'\n', "Activities score = " + str(winRate) ,'\n', "History of changes in options = " + str(optionsHistory),'\n', "Chosen activities log = " + str(chosenActivityLog),'\n', "Wining statistics = " + str(winingStatistics)]
    f.writelines(list)
    f.close()

def MainMenu(options, winRate, formerActivity= ""):
    while True:
        ans = input("Type:\n'1' to run the progrem.\n'2' to edit the options.\n'3' for win rate and statistics\n'4' for options history\n'5' for reset options.\n")
        match ans:
            case '1':
                currentChoice, options = PickActivity(options, formerActivity, winRate)
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
                    os.remove("options.txt")
                return None,None
    return currentChoice, options

def Initialize(options, winRate=None):
    firstOption = input("Enter your first option to add\n")
    options[firstOption] = 0
    winRate[firstOption] = 0
    winingStatistics[firstOption] = 0
    optionsHistory.append("add:" + firstOption)
    return options
def PickActivity(options, formerActivity, winRate=None):
    print("starting score is: ",options)
    counter = 1
    while True:
        currentChoice = random.choice(list(options.keys()))
        print(f"roll number: {counter} \nchosen: {currentChoice}")
        counter += 1
        options[currentChoice] += 1
        if options[currentChoice] == 3:
            print("The choice that has been made is:", currentChoice)
            chosenActivityLog.append(currentChoice)
            winRate[currentChoice] += 1
            for keys in winRate:
                winingStatistics[keys] = "{:.1f}".format((winRate[keys] / len(chosenActivityLog)) * 100) + "%"
            break
        print("Current score is: ",options)
        #time.sleep(5)
    for x in options:
        options[x] = 0
    options[currentChoice] = -4
    if formerActivity != "":
        print("Fromer activity was:",formerActivity)
        options[formerActivity] = -2
    return currentChoice,options
def EditChoice(options, winRate=None):
    while True:
        ans = input("edit options, type:\n'1' to add an option\n'2' to remove an option\n'3' to replace an option\n'4' to continue\n")
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
            optionsHistory.append(unwantedChoice + "->replaced_by:" + wantedChoice)
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
    print("The options are :" + str(dict.keys()).split("(")[1].split(")")[0])


