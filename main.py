# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
import random
import time
import os.path


def PickActivity(options,formerActivity):
    while True:
        print(options)
        currentChoice = random.choice(list(options.keys()))
        options[currentChoice] += 1
        if options[currentChoice] == 3:
            print("The choice that has been made is:", currentChoice)
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
def EditChoice(options, y0rn):
    while y0rn == 'y':
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
            options[wantedChoice] = 0
            del options[unwantedChoice]
    return options
def AddChoice(options):
    option = input("Enter option:\n")
    if option not in options:
        options[option] = 0
    else:
        print("The option is already in the pool\n")
    return options
def RemoveChoice(options):
        ShowActivities(options)

        option = input("Enter option to remove:\n")
        if option in options:
            print("the removed activity is: " + option)
        else:
            print("the activity does not exist, please chose one from the list.")
            RemoveChoice(options)

        del options[option]
        return options
def ShowActivities(options):
    print(options.keys())


formerActivity = ""


def Initialize(options):
    firstOption = input("Enter your first option to add\n")
    options[firstOption] = 0
    return EditChoice(options,'y')



if not os.path.isfile("options.txt"):
    options = {}
    options = Initialize(options)
else:
    fileRead = open("options.txt","r")
    options = eval(fileRead.readline())
    formerActivity = fileRead.readline().split("=")[1]
    ShowActivities(options)
    answer = input("would you like to edit your activities? yes = 'y', no = 'n'\n")
    if answer == 'y':
        options = EditChoice(options,'y')
    elif answer == 'n':
        PickActivity(options, formerActivity)

choice , options = PickActivity(options,formerActivity)
f = open("options.txt","w")
f.write(str(options) + "\nformerActivity=" + choice)

f.close()

