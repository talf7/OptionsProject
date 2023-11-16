# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
import random
import time
import os.path


def PickActivity(options,formerActivity):
    while True:
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

def EditChoice(options):
    ans = input("would you like to add or remove an option? Enter 'add' or 'remove'\n")
    if ans == 'add':
        options = AddChoice(options)
    elif ans == 'remove':
        RemoveChoice(options,'y')
def AddChoice(options):
    yOrn = 'y'
    while yOrn == "y":
        option = input("Enter option:\n")
        if option not in options:
            options[option] = 0
            yOrn = input("would you like to put another option? yes = 'y', no = 'n'\n")
        else:
            print("The option is already in the pool\n")
    return options

def RemoveChoice(options,ans):
    while ans == 'y':
        options.pop()
        ShowActivities(options)
        ans = input("would you like to remove another option? yes = 'y', no = 'n'\n")

def ShowActivities(options):
    print(options.keys())
formerActivity = ""
if not os.path.isfile("options.txt"):
    options = {}
    options = AddChoice(options)
else:
    fileRead = open("options.txt","r")
    options = eval(fileRead.readline())
    formerActivity = fileRead.readline().split("=")[1]
    ShowActivities(options)
    if input("would you like to edit your activities? yes = 'y', no = 'n'\n") == 'y':
        options = EditChoice(options)


choice , options = PickActivity(options,formerActivity)
f = open("options.txt","w")
f.write(str(options) + "\nformerActivity=" + choice)

f.close()

#{"coding":0,"STS":0,"rubik":0,"otherPS":0,"HellCard":0}



# best of 3:

