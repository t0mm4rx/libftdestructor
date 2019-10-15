import random
import string
import os

MAIN_BASE1 = f"""#include "libft.h"
#include <stdio.h>

int main()
{{
"""
MAIN_BASE2 = "\n}\n"

def random_string(length):
	letters = string.ascii_letters + string.digits
	return ''.join(random.choice(letters) for i in range(length))

def input_string():
	choice = random.choice([0, 1, 2])
	if (choice == 0):
		return '"{}"'.format(random_string(random.randint(1, 100)))
	if (choice == 1):
		return "NULL"
	if (choice == 2):
		return '""'

def input_uint():
	return random.randint(0, 2147483647)

def tests_substr():
	tests = ""
	for i in range(100):
		tests += "ft_substr({}, {}, {});\n".format(input_string(), input_uint(), input_uint())
	return tests

def tests_strjoin():
	tests = ""
	for i in range(100):
		tests += "ft_strjoin({}, {});\n".format(input_string(), input_string())
	return tests

def tests_strtrim():
	tests = ""
	for i in range(100):
		tests += "ft_strtrim({}, {});\n".format(input_string(), input_string())
	return tests

def create_tests():
	tests = ""
	tests += tests_substr()
	tests += tests_strjoin()
	tests += tests_strtrim()
	return tests

def create_main():
	tests = create_tests()
	with open("main.c", "w+") as file:
		file.write(MAIN_BASE1)
		file.write(tests)
		file.write(MAIN_BASE2)

def compile_main():
	os.system("gcc main.c -L. -lft -g -fsanitize=address && ./a.out")

create_main()
compile_main()
