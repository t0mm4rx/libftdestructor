import os
import part2_tests
import bonus_tests

MAIN_BASE1 = f"""#include "libft.h"
#include <stdio.h>

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

def create_tests():
	tests = ""
	tests += part2_tests.tests_part2()
	tests += bonus_tests.tests_bonus()
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
