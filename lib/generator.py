from random import *
import numpy as np
import scipy.stats


def define_globals():
    global forSerial
    global forLoops


def get_commands(path):
    try:
        return open(path).read().splitlines()
    except FileNotFoundError:
        print('Not found : ' + path)

def loopflag(): # Selini
    var = round(uniform(0, 1), 2)
    print(var)
    return True if var > 0.49 else False


def generate_input_file():
    define_globals()
    get_preferences()
    run_generation()


def commands_in_loop():
    return int(gauss(mean_branch, deviation_branch))


def repeats_loop():
    return int(gauss(mean_rep_branch, deviation_rep_branch))


def commands_in_serial():
    return int(gauss(mean_serial, deviation_serial))


def get_preferences():
    global mean_branch  # Mean number of commands in loop block
    global deviation_branch  # Standard deviation of commands in loop block
    global mean_rep_branch  # Mean number of repeates of loop
    global deviation_rep_branch  # Standart deviation of repeates of loop
    global mean_serial  #
    global deviation_serial  #
    try:
        mean_branch = int(input("Enter the mean for branch commands: "))
        deviation_branch = int(input("Enter the standard deviation for branch commands: "))
        mean_rep_branch = int(input("Enter the mean for repeat times for branch blocks: "))
        deviation_rep_branch = int(input("Enter the standard deviation for repeat times for branch blocks: "))
        mean_serial = int(input("Enter the mean for serial commands: "))
        deviation_serial = int(input("Enter the deviation_serial: "))
    except ValueError:
        print('Please give a number')


def run_generation():
    print('Commands in loop', commands_in_loop())
    print('Repeats of loop', repeats_loop())
    print('Commands in serial', commands_in_serial())
    print('Loop flag - selini ', loopflag())
