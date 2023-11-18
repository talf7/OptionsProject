# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
import random
import time
import os.path


def PickActivity(options,OptionsHistory):
    formerActivity = OptionsHistory[-1]
    while True:
        print(options)
        currentChoice = random.choice(list(options.keys()))
        options[currentChoice] += 1
        if options[currentChoice] == 3:
            print("The choice that has been made is:", currentChoice)
            ChosenActivityHistory.append(currentChoice)
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

def mainMenu(options, OptionsHistory):
    while True:
        ans = input("---------------------------\nmain menu, type:\n'1' for runing the program \n'2' for the history of activities \n'3'for histroy of editing options \n'4'for editing options \n")
        if ans == '1':
            PickActivity(options, OptionsHistory)
            choice, options = PickActivity(options, formerActivity)
            f = open("options.txt", "w")
            f.write(str(options))
            f.write("\nActivity history =" + ",".join(
                str(element) for element in ChosenActivityHistory) + "\nChanges history =" + ",".join(
                str(element) for element in OptionsHistory))
            f.close()

        if ans == '2':
            ShowChosenActivityHistory(ChosenActivityHistory)
        if ans == '3':
            ShowHistoryOptins(OptionsHistory)
        if ans == '4':
            EditChoice(options, y0rn)
        if ans == '5':
            break
def EditChoice(options, y0rn):
    while True:
        ans = input("would you like to add ,remove or replace an option?\nEnter '1' to add an option\nEnter '2' to remove an option\nEnter '3' to replace an option\nEnter 'n' for no\n")
        if ans == '1':
            options = AddChoice(options)
        elif ans == '2':
           RemoveChoice(options)
        elif ans == '3':
            replaceChoice(options,'y')
        else:
            break
    return options
#    yOrn = input("would you like to add ,remove or edit another option? 'y' for yes, 'n' for no \n")
def replaceChoice(options, unwantedChoice):
    ShowActivities(options)
    unwantedChoice = input("enter the option you would like to replace:\n")
    if unwantedChoice not in options:
        print("the option is not in the list so it cant be replaced")
    else:
        wantedChoice = input("Enter the desired option:\n")
        if wantedChoice in options:
            print("the option is already in the list")
        else:
            OptionsHistory.append("replace " + unwantedChoice + "with " + wantedChoice)
            options[wantedChoice] = 0
            del options[unwantedChoice]
    return options
def AddChoice(options):
    option = input("Enter option:\n")
    if option not in options:
        options[option] = 0
        OptionsHistory.append("add " + option)
    else:
        print("The option is already in the pool\n")
    return options
def RemoveChoice(options):
        ShowActivities(options)

        option = input("Enter option to remove:\n")
        if option in options:
            print("the removed activity is: " + option)
            OptionsHistory.append("remove " + option)
        else:
            print("the activity does not exist, please chose one from the list.")
            RemoveChoice(options)

        del options[option]
        return options
def ShowActivities(options):
    print(options.keys())
def ShowHistoryOptins(OptionsHistory):
    print("options history is " + ",".join(str(element) for element in OptionsHistory))
def ShowChosenActivityHistory(ChosenActivityHistory):
    print("History of chosen activities: " + ",".join(str(element) for element in ChosenActivityHistory))
def Initialize(options):
    firstOption = input("Enter your first option to add\n")
    OptionsHistory.append("add " + firstOption)
    options[firstOption] = 0
    return EditChoice(options,'y')



formerActivity = ""
if not os.path.isfile("options.txt"):
    options = {}
    ChosenActivityHistory = []
    OptionsHistory = []
    options = Initialize(options)
else:
    fileRead = open("options.txt","r")
    options = eval(fileRead.readline())
    ChosenActivityHistory = []
    OptionsHistory = fileRead.readline().split("=")[1].split(",")

    ShowActivities(options)
    mainMenu(options)

    #answer = input("would you like to edit your activities? yes = 'y', no = 'n'\n")
    #if answer == 'y':
    #    options = EditChoice(options,'y')
    #elif answer == 'n':
    #    PickActivity(options, formerActivity)




