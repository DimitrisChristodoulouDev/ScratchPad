from lib.commands import *
from lib.generator import *
import time


start_time = time.time()
generate_commands()
print("--- %s seconds for creating conf file  ---\n" % ( round(float(time.time() - start_time))))


generate_input_file()  # for the parser


