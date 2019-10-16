import os
import part1_tests

MAIN_BASE1 = f"""#include "libft.h"
#include <stdio.h>

char map(unsigned int i, char c)
{{
	return ((char) (c + 3));
}}

int main()
{{
"""
MAIN_BASE2 = "\n}\n"

def create_tests():
	tests = ""
	tests += part1_tests.tests_part1()
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
