import random
file = open('output.txt', 'w')

def return_preferences():
    try:
        mu = int(input("Please give the mean \n --> "))
        sigma = int(input("Please give the standard divation \n --> "))
        return mu, sigma
    except ValueError:
        print("Not a number")

def command_set():
    return [
                'add', 'sub', 'addi', 'addu', 'subu',
                'addiu', 'mfc0', 'mult', 'multu', 'div',
                'divu', 'mfhi', 'mflo', 'and', 'or',
                'andi', 'ori', 'sll', 'srl', 'lw', 'sw', 'lbu'
            ]

def push_to_file(row):
    print(row, file=file)


def prettify_row(row):
    return str(row['name'] + '\t' + str(row['power']) + '\t' + str(row['cycles']))






def process_block(block):
    #loop throuh the block, and format it according to the template
    for row in block:
        formated_row = prettify_row(row)
        push_to_file(formated_row)




def generate_file():
    #creating blocks (serial, branch) and forward to process block
    block = []

    row = {
        'name': random.choice(command_set()),  # get the name
        'cycles': random.randint(0, 9),
        'power': random.randint(0, 9)
    }
    count = 0
    while (count < 1000):
        block.append({
        'name': random.choice(command_set()),  # get the name
        'cycles': random.randint(0, 9),
        'power': random.randint(0, 9)
    })
        process_block(block=block)
        block = []#empty the block
        count += 1







