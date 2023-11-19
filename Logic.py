import random
import time
import os.path


def UpdateFile():
    if not os.path.isfile("options.txt"):
        options = {}
        statistics = {}
        formerActivity = ""
        options = Initialize(options, statistics)
    else:
        fileRead = open("options.txt", "r")
        content = fileRead.readlines()
        print("the current content is:", content)
        options = eval(content[0])
        formerActivity = content[1].split("=")[1][0:-1]
        statistics = eval(content[2])
        Show(options)
        fileRead.close()

    choice, options = MainMenu(options, statistics, formerActivity)
    f = open("options.txt", "w")
    print(statistics)
    list = [str(options),'\n',"formerActivity=" + choice,'\n', str(statistics)]
    f.writelines(list)
    f.close()

#main menu not working yet
def MainMenu(options,statistics, formerActivity= ""):
    while True:
        ans = input("Type:\n'1' to run the progrem.\n'2' to edit the options.\n'3' for statistics\n")
        match ans:
            case '1':
                currentChoice, options = PickActivity(options, formerActivity, statistics)
                break
            case '2':
                options = EditChoice(options, statistics)
            case '3':
                print(statistics)
    return currentChoice, options

def Initialize(options, statistics=None):
    firstOption = input("Enter your first option to add\n")
    options[firstOption] = 0
    statistics[firstOption] = 0
    return options
def PickActivity(options, formerActivity, statistics=None):
    print("starting score is: ",options)
    counter = 1
    while True:
        currentChoice = random.choice(list(options.keys()))
        print(f"roll number: {counter} \nchosen: {currentChoice}")
        counter += 1
        options[currentChoice] += 1
        if options[currentChoice] == 3:
            print("The choice that has been made is:", currentChoice)
            statistics[currentChoice] += 1
            break
        print("Current score is: ",options)
        time.sleep(5)
    for x in options:
        options[x] = 0
    options[currentChoice] = -4
    if formerActivity != "":
        print("Fromer activity was:",formerActivity)
        options[formerActivity] = -2
    return currentChoice,options
def EditChoice(options, statistics=None):
    while True:
        ans = input("edit options, type:\n'1' to add an option\n'2' to remove an option\n'3' to replace an option\n'4' to continue\n")
        if ans == '1':
            options = AddChoice(options, statistics)
        elif ans == '2':
            options = RemoveChoice(options)
        elif ans == '3':
            options = replaceChoice(options, statistics)
        elif ans == '4':
            break
        else:
            continue
    return options
def replaceChoice(options, statistics=None):
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
            statistics[wantedChoice] = 0
            del options[unwantedChoice]
    return options
def AddChoice(options, statistics={}):
    option = input("Enter option:\n")
    print("the option is: " + option)
    if option not in options:
        options[option] = 0
        statistics[option] = 0
    else:
        print("The option is already in the pool\n")
    return options
def RemoveChoice(options):
        Show(options)
        option = input("Enter option to remove:\n")
        if option in options:
            print("the removed activity is: " + option)
            del options[option]
        else:
            print("the activity does not exist, please chose one from the list.")
            RemoveChoice(options)
        return options
def Show(dict):
    print(dict.keys())




