from random import *
import os

input_file = 'assets/output.txt'
ReadlinesNo = 10
repeatofLoop = 0
Scratchpad = []
L1Cache = []
previousInstruction = ''


def parseInputFile():
    global previousInstruction, input_file, ReadlinesNo, repeatofLoop, Scratchpad, L1Cache
    print('Number of ', ReadlinesNo)
    with open(input_file, 'r') as infile:
        # Skip first 2 lines
        next(infile)
        next(infile)
        lines = []
        for line in infile:
            # print (line)
            lines.append(line)
            if len(lines) > ReadlinesNo:
                parselines(lines)
                lines = []
        if len(lines) > 0:
            parselines(lines)


def parselines(blockoffile):
    global previousInstruction, input_file, ReadlinesNo, repeatofLoop, Scratchpad, L1Cache
    for line in blockoffile:
        line = line.strip()
        print(line)
        instruction = line.split('\t')

        obj = {
            'number': instruction[0],
            'address': instruction[1],
            'name': instruction[2],
            'cycles': instruction[3],
            'pc': instruction[4]
        }
        print(instruction[5] == '1')
        print(instruction[6] == '0')
        # , type(instruction[6]))

        # love
        if instruction[5] is '0':  # Serial
            L1Cache.append(obj)
            print('Found serial')
        if instruction[5] is '1' and instruction[6] is '0':  # New loop
            print('Found new loop')
            # Save last repeat of loop
            Scratchpad.append('R' + fLoop)
            print('Saved last repeat')
            # Reset repeats of loop
            repeatofLoop = 0
            print('Reset repeats')
            # Append new instruction
            Scratchpad.append(obj)
            print('Added new object')
        else:  # Same loop
            repeatofLoop += 1
            print('Same loop, increase by one')
    print(Scratchpad)
