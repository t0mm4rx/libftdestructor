import random
import string
import os

TESTS_N = 30
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

def input_char():
	choice = random.choice([0, 1])
	if (choice == 0):
		return '"' + random.choice(string.ascii_letters + string.digits) + '"'
	if (choice == 1):
		return "'\\0'"

def tests_substr():
	tests = ""
	for i in range(TESTS_N):
		tests += "ft_substr({}, {}, {});\n".format(input_string(), input_uint(), input_uint())
	return tests

def tests_strjoin():
	tests = ""
	for i in range(TESTS_N):
		tests += "ft_strjoin({}, {});\n".format(input_string(), input_string())
	return tests

def tests_strtrim():
	tests = ""
	for i in range(TESTS_N):
		tests += "ft_strtrim({}, {});\n".format(input_string(), input_string())
	return tests

def tests_split():
	tests = ""
	for i in range(TESTS_N):
		tests += "ft_split({}, {});\n".format(input_string(), input_char())
	return tests

def create_tests():
	tests = ""
	tests += tests_substr()
	tests += tests_strjoin()
	tests += tests_strtrim()
	tests += tests_split()
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
