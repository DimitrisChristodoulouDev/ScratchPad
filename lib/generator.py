from random import *
import numpy as np
import scipy.stats
from array import array

COMMANDS_PATH = 'assets/conf.txt'  # Commands file path
output_file = open('assets/output.txt', 'w')


def generate_input_file():
    get_preferences()  # 1.Get user input
    get_commands() #6 Read commands filr
    run_generation() #9. The main generator


def push_to_file(row):
    print(str(row), file=output_file)


def prettify_row(row):
    pass
    #return str(row['name'] + '\t' + str(row['cycles']) + '\t' + str(row['pc']))


def get_commands():
    try:
        global commands_set #7. Make it global to access it from everywhere
        commands_set = open(COMMANDS_PATH).read().splitlines() #8. Read the file into the array
    except FileNotFoundError:
        print('Not found : ' + COMMANDS_PATH)


def loop_flag():  # Selini
    var = uniform(0, 1)
    return False # if var > 0.50 else False


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


def print_header():
    print(str("instruction_type" + '\t' + "cycles" + '\t' + "power consumption"), file = output_file)


def run_generation():
    print_header()

    for count in range(0, 3):
        print('Iteration', count)
        num_of_com_loop = commands_in_loop()
        num_of_serial = commands_in_serial()
        num_of_loop_rep = repeats_loop()

        print('Flag', loop_flag())
        print('Loop', num_of_com_loop)
        print('Repeat', num_of_loop_rep)
        print('Serial', num_of_serial)





        my_arr = []
        if loop_flag():
            #run loop
            for i in range(0, num_of_com_loop):
                my_arr.append(get_command())
                # name = command[0]
                # cycles = command[1]
                # power_consumption = command[2]
            for x in range(0, num_of_loop_rep):
                for y in my_arr:
                   if x==0:
                       y = y+'\t1'+'\t0'
                   else:
                       y=y+'\t1'+'\t1'
                   push_to_file(y)
                   print('Serial')
                   for i in range(0, num_of_serial):
                       push_to_file(get_command())
        else:
            print('Serial')
            for i in range(0, num_of_serial):
                push_to_file(get_command()+'\t0'+'\tx')
            for i in range(0, num_of_com_loop):
                my_arr.append(get_command())
                # name = command[0]
                # cycles = command[1]
                # power_consumption = command[2]
            for x in range(0, num_of_loop_rep):
                for y in my_arr:
                    if x == 0:
                        y = y + '\t1' + '\t0'
                    else:
                        y = y + '\t1' + '\t1'
                    push_to_file(y)