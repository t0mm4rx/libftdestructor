import inputs

TESTS_N = 30

def tests_substr():
	tests = ""
	tests += 'puts("* ft_substr");';
	for i in range(TESTS_N):
		tests += "free(ft_substr({}, {}, {}));\n".format(inputs.input_string(), inputs.input_uint(), inputs.input_uint())
	return tests

def tests_strjoin():
	tests = ""
	tests += 'puts("* ft_srjoin");';
	for i in range(TESTS_N):
		tests += "free(ft_strjoin({}, {}));\n".format(inputs.input_string(), inputs.input_string())
	return tests

def tests_strtrim():
	tests = ""
	tests += 'puts("* ft_strtrim");';
	for i in range(TESTS_N):
		tests += "free(ft_strtrim({}, {}));\n".format(inputs.input_string(), inputs.input_string())
	return tests

def tests_split():
	tests = ""
	tests += 'puts("* ft_split");';
	for i in range(TESTS_N):
		tests += "ft_split({}, {});\n".format(inputs.input_string(), inputs.input_char())
	return tests

def tests_itoa():
	tests = ""
	tests += 'puts("* ft_itoa");';
	for i in range(TESTS_N):
		tests += "free(ft_itoa({}));\n".format(inputs.input_int())
	return tests

def tests_putchar():
	tests = ""
	tests += 'puts("* ft_putchar");';
	for i in range(TESTS_N):
		tests += "ft_putchar_fd({}, -1);\n".format(inputs.input_char())
	return tests

def tests_putstr():
	tests = ""
	tests += 'puts("* ft_putstr");';
	for i in range(TESTS_N):
		tests += "ft_putstr_fd({}, -1);\n".format(inputs.input_string())
	return tests

def tests_putendl():
	tests = ""
	tests += 'puts("* ft_putendl");';
	for i in range(TESTS_N):
		tests += "ft_putendl_fd({}, -1);\n".format(inputs.input_string())
	return tests

def tests_putnbr():
	tests = ""
	tests += 'puts("* ft_putnbr");';
	for i in range(TESTS_N):
		tests += "ft_putnbr_fd({}, -1);\n".format(inputs.input_int())
	return tests

def tests_mapi():
	tests = ""
	tests += 'puts("* ft_strmapi");';
	for i in range(TESTS_N):
		tests += "free(ft_strmapi({}, {}));\n".format(inputs.input_string(), inputs.input_map_func())
	return tests

def tests_part2():
	tests = ""
	tests += "puts(\"** Part 2\");"
	tests += tests_substr()
	tests += tests_strjoin()
	tests += tests_strtrim()
	tests += tests_split()
	tests += tests_itoa()
	tests += tests_putchar()
	tests += tests_putstr()
	tests += tests_putendl()
	tests += tests_putnbr()
	tests += tests_mapi()
	return tests
