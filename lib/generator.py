def get_commands(path):
    try:
        return open(path).read().splitlines()
    except FileNotFoundError:
        print('Not found : ' + path)


def preferences():
    try:
        return int(input("Enter the percentage of loop statements 100: "))
    except ValueError:
        print('Please give a positive number')


def generate_input_file():
    commands = get_commands('assets/conf.txt')  # Read commands
    for row in commands:
        print(row.split('\t'))
