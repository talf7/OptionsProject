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
    print(outputList)

def Favored(options):
    global favoredChoice
    while True:
        E.Show(options)
        ans = input("Here you can add a favored option for the next run of the program, There can be only 1 favored choice at a time!\nJust write your favored option and we will make it more likly to win\n")
        if ans not in options:
            print("The option is not in the pool, Please enter one that is.\n")
        else:
            favoredChoice = ans
            break