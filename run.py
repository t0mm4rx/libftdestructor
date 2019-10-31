import sys
import tests
import os

HEADER = f"""
\u001b[36;1m
 _ _ _      __ _      _           _                   _
| (_) |    / _| |    | |         | |                 | |
| |_| |__ | |_| |_ __| | ___  ___| |_ _ __ _   _  ___| |_ ___  _ __
| | | '_ \|  _| __/ _` |/ _ \/ __| __| '__| | | |/ __| __/ _ \| '__|
| | | |_) | | | || (_| |  __/\__ \ |_| |  | |_| | (__| || (_) | |
|_|_|_.__/|_|  \__\__,_|\___||___/\__|_|   \__,_|\___|\__\___/|_|\u001b[0m
                                                         by\u001b[1m tmarx\u001b[0m

"""

def compile_lib(path, bonus):
	if (bonus):
		os.system("make bonus -C {}".format(path))
	else:
		os.system("make all -C {}".format(path))

if (len(sys.argv) < 2 or len(sys.argv) > 3):
    print("Error! Usage: python3 run.py <path-of-libft> [12B, default all]")
    exit(0)
else:
    PATH = sys.argv[1]
    if (PATH[-1] != "/"):
        PATH += "/"

PART1 = True
PART2 = True
PARTB = True
if (len(sys.argv) == 3):
    if (not "B" in sys.argv[2]):
        PARTB = False
    if (not "1" in sys.argv[2]):
        PART1 = False
    if (not "2" in sys.argv[2]):
        PART2 = False

print(HEADER)

print("Compiling libft...")
compile_lib(PATH, PARTB)

if (PART1):
    tests.part1(PATH)
if (PART2):
    tests.part2(PATH)
if (PARTB):
    tests.partB(PATH)
