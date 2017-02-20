from random import *
import numpy as np
import scipy.stats

COMMANDS_PATH = 'assets/conf.txt'  # Commands file path


def generate_input_file():
    get_preferences()  # 1.Get user input
    get_commands() #6 Read commands filr
    run_generation() #9. The main generator



def get_commands():
    try:
        global commands_set #7. Make it global to access it from everywhere
        commands_set = open(COMMANDS_PATH).read().splitlines() #8. Read the file into the array
    except FileNotFoundError:
        print('Not found : ' + COMMANDS_PATH)


def loop_flag():  # Selini
    var = round(uniform(0, 1), 2)
    print(var)
    return True if var > 0.49 else False


def commands_in_loop(): #11
    return int(gauss(mean_branch, deviation_branch))


def repeats_loop():#13
    return int(gauss(mean_rep_branch, deviation_rep_branch))


def commands_in_serial(): #15
    return int(gauss(mean_serial, deviation_serial))


def get_preferences():
    global mean_branch  # Mean number of commands in loop block
    global deviation_branch  # Standard deviation of commands in loop block
    global mean_rep_branch  # Mean number of repeates of loop
    global deviation_rep_branch  # Standart deviation of repeates of loop
    global mean_serial  # Mean number of serial commands
    global deviation_serial  # Standard deviation of serial commands
    try:
        mean_branch = int(input("Enter the mean for branch commands: ")) #2
        deviation_branch = int(input("Enter the standard deviation for branch commands: ")) #3
        mean_rep_branch = int(input("Enter the mean for repeat times for branch blocks: ")) #4
        deviation_rep_branch = int(input("Enter the standard deviation for repeat times for branch blocks: ")) #5
        mean_serial = int(input("Enter the mean for serial commands: ")) #5
        deviation_serial = int(input("Enter the deviation_serial: ")) #6
    except ValueError: # Throw exception if input is not a number
        print('Please give a number')


def get_command():
    return choice(commands_set)


def run_generation():
    while True:
        print('Commands in loop', commands_in_loop())
        print('Repeats of loop', repeats_loop())
        print('Commands in serial', commands_in_serial())
        print('Loop flag - selini ', loop_flag())

        commandsInLoop = commands_in_loop() #10
        repeatsLoop = repeats_loop() #12
        commandsInSerial = commands_in_serial() #14

        if(loop_flag()): #15. True => Loop (megalitero tu 0.5)
            #Make a block of commands with size = commandsInLoop
            #Repeat that for times = repeatsLoop
        else # Serial
            # Make a block of commands with size = commandsInSerial




