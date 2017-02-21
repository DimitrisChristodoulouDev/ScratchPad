from random import *
import os

COMMANDS_PATH = 'assets/conf.txt'  # Commands file path
output_file = open('assets/output.txt', 'w')


def generate_input_file():
    get_preferences()  # 1.Get user input
    get_commands()  # 6 Read commands filr
    run_generation()  # 9. The main generator


def push_to_file(row):
    print(prettify_row(row), file=output_file)


def prettify_row(row):
    return str(row['name'] + '\t' + str(row['cycles']) + '\t' + str(row['pc']) + '\t' + str(row['branch']) + '\t' + str(
        row['loop']))


def get_commands():
    try:
        global commands_set  # 7. Make it global to access it from everywhere
        commands_set = open(COMMANDS_PATH).read().splitlines()  # 8. Read the file into the array
    except FileNotFoundError:
        print('Not found : ' + COMMANDS_PATH)


def loop_flag():  # Selini
    var = uniform(0, 1)
    return True  if var > 0.50 else False


def commands_in_loop():  # 11
    return int(gauss(mean_branch, deviation_branch))


def repeats_loop():  # 13
    return int(gauss(mean_rep_branch, deviation_rep_branch))


def commands_in_serial():  # 15
    return int(gauss(mean_serial, deviation_serial))


def get_preferences():
    global mean_branch  # Mean number of commands in loop block
    global deviation_branch  # Standard deviation of commands in loop block
    global mean_rep_branch  # Mean number of repeates of loop
    global deviation_rep_branch  # Standart deviation of repeates of loop
    global mean_serial  # Mean number of serial commands
    global deviation_serial  # Standard deviation of serial commands
    try:
        mean_branch = int(input("Enter the mean for branch commands: "))  # 2
        deviation_branch = int(input("Enter the standard deviation for branch commands(smaller than "+str(mean_branch)+"): "))  # 3
        if deviation_branch >= mean_branch or deviation_branch <= 0 or mean_branch <= 0 :
            os.system('cls')
            print('Invalid input...')
            get_preferences()

        mean_rep_branch = int(input("Enter the mean for repeat times for branch blocks: "))  # 4
        deviation_rep_branch = int(input("Enter the standard deviation for repeat times for branch blocks (smaller than "+str(mean_rep_branch)+"): "))  # 5
        if deviation_branch >= mean_branch or deviation_branch <= 0 or mean_branch <= 0 :
            os.system('cls')
            print('Invalid input...')
            get_preferences()

        mean_serial = int(input("Enter the mean for serial commands: "))  # 5
        deviation_serial = int(input("Enter the deviation_serial(smaller than "+str(mean_serial)+"):: "))  # 6
        if deviation_branch >= mean_branch or deviation_branch <= 0 or mean_branch <= 0 :
            os.system('cls')
            print('Invalid input...')
            get_preferences()

    except ValueError:  # Throw exception if input is not a number
        print('Please give valid numbers')
        os.system('cls')
        print('Invalid input...')
        get_preferences()


def get_command():
    return choice(commands_set)


def print_header():
    print(str("instruction_type" + '\t' + "cycles" + '\t' + "power consumption"), file=output_file)


def run_times():
    try:
        return int(input('How many blocks of code: '))
    except ValueError:
        print('Please give a number')


def run_generation():
    print_header()

    for count in range(0, run_times()):
        print('Iteration : ', count)
        num_of_com_loop = commands_in_loop()
        num_of_serial = commands_in_serial()
        num_of_loop_rep = repeats_loop()
        flag = loop_flag()
        print('Flag', flag)
        print('Loop', num_of_com_loop)
        print('Repeat', num_of_loop_rep)
        print('Serial', num_of_serial)
        if flag:  # Run loop
            run_loop(num_of_com_loop, num_of_loop_rep)
        else:
            pass
            run_serial(num_of_serial)
    output_file.close()
    print('Opening file...')
    osCommandString = "notepad.exe assets/output.txt"
    os.system(osCommandString)


def run_loop(num_of_com_loop, num_of_loop_rep):
    print('Loop')
    for j in range(0, num_of_loop_rep):
        for i in range(0, num_of_com_loop):
            command = get_command().split('\t')
            obj = {
                'name': command[0],
                'cycles': command[1],
                'pc': command[2],
                'branch': '1' if j == 0 else 1,
                'loop': '0' if j == 0 else 1
            }
            push_to_file(obj)


def run_serial(num_of_serial):
    print('Serial')
    for i in range(0, num_of_serial):
        command = get_command().split('\t')
        obj = {
            'name': command[0],
            'cycles': command[1],
            'pc': command[2],
            'branch': '0',
            'loop': 'x'
        }
        push_to_file(obj)
