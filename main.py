# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
import os.path
import Logic as L

if not os.path.isfile("options.txt"):
    options = {}
    formerActivity = ""
    options = L.Initialize(options)
else:
    fileRead = open("options.txt","r")
    options = eval(fileRead.readline())
    formerActivity = fileRead.readline().split("=")[1]
    L.ShowActivities(options)
    options = L.EditChoice(options)

choice, options = L.PickActivity(options,formerActivity)
f = open("options.txt","w")
f.write(str(options) + "\nformerActivity=" + choice)
f.close()

