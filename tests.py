import functions

N = 5000

def print_tests_header(title):
    print("*" * 30)
    print("*", end="")
    print("{:^28s}".format(title), end="")
    print("*")
    print("*" * 30)

def part1(PATH):
    print_tests_header("Part 1")

def part2(PATH):
    print_tests_header("Part 2")
    functions.make_test("ft_substr", PATH, "free(ft_substr(<string>, <uint>, <uint>));", N)
    functions.make_test("ft_strjoin", PATH, "free(ft_strjoin(<string>, <string>));", N)
    functions.make_test("ft_strtrim", PATH, "free(ft_strtrim(<string>, <string>));", N)
    functions.make_test("ft_split", PATH, "free(ft_split(<string>, <char>));", N)
    functions.make_test("ft_itoa", PATH, "free(ft_itoa(<int>));", N)
    functions.make_test("ft_strmapi", PATH, "free(ft_strmapi(<string>, <map_func>));", N)
    functions.make_test("ft_putchar_fd", PATH, "ft_putchar_fd(<char>, -1);", N)
    functions.make_test("ft_putstr_fd", PATH, "ft_putstr_fd(<string>, -1);", N)
    functions.make_test("ft_putendl_fd", PATH, "ft_putendl_fd(<string>, -1);", N)
    functions.make_test("ft_putnbr_fd", PATH, "ft_putnbr_fd(<int>, -1);", N)

def partB(PATH):
    print_tests_header("Part Bonus")
