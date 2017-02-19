from random import *
from itertools import *

conf_file = open('assets/conf.txt', 'w')  # output file with commands

LOGICAL = [5, 7]
ARITHMETIC = [7, 10]
BITWISE = [2, 5]
DATA_TRANSFER = [10, 15]
PC = 5  # Multiply with cycles


def create_arrays():
    # Read the four files into arrays
    bitwise_shift = get_file_contents('assets/BitwiseShift.txt')
    arithmetic = get_file_contents('assets/Arithmetic.txt')
    data_transfer = get_file_contents('assets/DataTransfer.txt')
    logical = get_file_contents('assets/Logical.txt')
    return arithmetic, bitwise_shift, data_transfer, logical


def get_file_contents(path):
    try:
        return open(path).read().splitlines()
    except FileNotFoundError:
        print('Not found : ' + path)


def push_to_file(row):
    print(prettify_row(row), file=conf_file)


def prettify_row(row):
    return str(row['name'] + '\t' + str(row['cycles']) + '\t' + str(row['pc']))


def generate_commands():
    arithmetic, bitwise, data_transfer, logical = create_arrays()
    for row in arithmetic:
        cycles = randint(ARITHMETIC[0], ARITHMETIC[1])
        pc = PC * cycles
        push_to_file({
            'name': row, 'cycles': cycles, 'pc': pc
        })

    for row in bitwise:
        cycles = randint(BITWISE[0], BITWISE[1])
        pc = PC * cycles
        push_to_file({
            'name': row, 'cycles': cycles, 'pc': pc
        })

    for row in data_transfer:
        cycles = randint(DATA_TRANSFER[0], DATA_TRANSFER[1])
        pc = PC * cycles
        push_to_file({
            'name': row, 'cycles': cycles, 'pc': pc
        })

    for row in logical:
        cycles = randint(LOGICAL[0], LOGICAL[1])
        pc = PC * cycles
        push_to_file({
            'name': row, 'cycles': cycles, 'pc': pc
        })

    conf_file.close()
