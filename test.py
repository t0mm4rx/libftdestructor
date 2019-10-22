import os
import part2_tests
import bonus_tests
import sys

MAIN_BASE1 = f"""#include "libft.h"
#include <stdio.h>
#include <stdlib.h>

char map(unsigned int i, char c)
{{
	return ((char) (c + 3));
}}

void del(void *content)
{{
	(void) content;
}}

void *lstmap(void *content)
{{
	(void) content;
	return ft_calloc(sizeof(char), 1);
}}

int main()
{{
"""
MAIN_BASE2 = "\n}\n"
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

BONUS = True
PATH = "./"

if (len(sys.argv) == 3):
	PATH = sys.argv[1]
	if (sys.argv[2] == "yes"):
		BONUS = True
	else:
		BONUS = False
else:
	print("Error !\nUsage: python3.7 test.py <path-of-libft> <bonus (yes/no)>\nExemple: python3.7 ../libft yes")
	exit(0)

def create_tests():
	tests = ""
	tests += part2_tests.tests_part2()
	if (BONUS):
		tests += bonus_tests.tests_bonus()
	return tests

def create_main():
	tests = create_tests()
	with open("main.c", "w+") as file:
		file.write(MAIN_BASE1)
		file.write(tests)
		file.write(MAIN_BASE2)

def compile_lib():
	os.system("cp {}/libft.h ./".format(PATH))
	if (BONUS):
		os.system("make bonus -C {}".format(PATH))
	else:
		os.system("make all -C {}".format(PATH))

def compile_main():
	os.system("gcc main.c -L{} -lft -g -fsanitize=address && ./a.out".format(PATH))

print(HEADER)
compile_lib()
create_main()
compile_main()
