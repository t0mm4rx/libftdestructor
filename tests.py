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
    print('')

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
    print('')

def partB(PATH):
    print_tests_header("Part Bonus")
    functions.make_test("ft_lstnew", PATH, "free(ft_lstnew(<string>));", N)
    functions.make_test("ft_delone", PATH, "ft_lstdelone(<elem>, <del_func>);", N)
    functions.make_test("ft_lstclear", PATH, "ft_lstclear(&<list>, <del_func>);", int(N / 5), create_list=True)
    functions.make_test("ft_lstadd_front", PATH, "ft_lstadd_front(&<list>, <elem>);", int(N / 5), create_list=True)
    functions.make_test("ft_lstadd_back", PATH, "ft_lstadd_back(&<list>, <elem>);", int(N / 5), create_list=True)
    functions.make_test("ft_lstsize", PATH, "ft_lstsize(<list>);", int(N / 5), create_list=True)
    functions.make_test("ft_lstlast", PATH, "ft_lstlast(<list>);", int(N / 5), create_list=True)
    functions.make_test("ft_lstiter", PATH, "ft_lstiter(<list>, <del_func>);", int(N / 5), create_list=True)
    functions.make_test("ft_lstmap", PATH, "ft_lstmap(<list>, <lstmap_func>, <del_func>);", int(N / 5), create_list=True)
    print('')
