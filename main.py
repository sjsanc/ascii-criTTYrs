import sys
from enum import Enum


class Buddy:
    def __init__(self, name):
        self.name = name

    age = 0
    awake = True

    def sayName(self):
        print(self.name)


    def sleepWake(self, state):
        if state == "WAKE" and self.awake == False:
            self.awake = True
            print(self.name + " wakes up with a start! Hi there!")
        elif state == "SLEEP" and self.awake == True:
            self.awake = False
            print(self.name + " falls asleep soundly...")
        else:
            raise Exception("Can't duplicate states")
            
    def getAwakeStatus(self):
        if self.awake == True:
            print(self.name + " is awake")
        else:
            print(self.name + " is sound asleep..sh!")


def run():
    newBud = Buddy(sys.argv[1]) 

    while True:
        user_input = input("Say something to " + newBud.name + ":\n")
        if user_input == "go away": 
            break
        elif user_input == "go to bed":
            newBud.sleepWake("SLEEP")
        elif user_input == "status":
            newBud.getAwakeStatus()
        else:
            print("I am " + newBud.name + "!...*spits bubbled*")


if __name__ == "__main__":
    run()
