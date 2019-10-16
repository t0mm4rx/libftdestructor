import inputs
import random

TESTS_N = 30

def tests_lstnew():
    tests = ""
    for i in range(TESTS_N):
        tests += "free(ft_lstnew({}));\n".format(inputs.input_string())
    tests += 'puts("* ft_lstnew ok !");';
    return tests

def tests_lstdelone():
    tests = ""
    for i in range(TESTS_N):
        tests += "ft_lstdelone({}, {});\n".format(inputs.input_elem(), inputs.input_del_func())
    tests += 'puts("* ft_lstdelone ok !");';
    return tests

def tests_lstclear():
    tests = ""
    for i in range(TESTS_N):
        nb = random.randint(0, 10000000000)
        tests += inputs.create_list(nb)
        tests += "ft_lstclear(&list{}, {});\n".format(nb, inputs.input_del_func())
    tests += 'puts("* ft_lstclear ok !");';
    return tests

def tests_lstaddfront():
    tests = ""
    for i in range(TESTS_N):
        nb = random.randint(0, 10000000000)
        tests += inputs.create_list(nb)
        tests += "ft_lstadd_front(&list{}, {});\n".format(nb, inputs.input_elem())
    tests += 'puts("* ft_lstadd_front ok !");';
    return tests

def tests_lstaddback():
    tests = ""
    for i in range(TESTS_N):
        nb = random.randint(0, 10000000000)
        tests += inputs.create_list(nb)
        tests += "ft_lstadd_back(&list{}, {});\n".format(nb, inputs.input_elem())
    tests += 'puts("* ft_lstadd_back ok !");';
    return tests

def tests_lstsize():
    tests = ""
    for i in range(TESTS_N):
        nb = random.randint(0, 10000000000)
        tests += inputs.create_list(nb)
        tests += "ft_lstsize(list{});\n".format(nb)
    tests += 'puts("* ft_lstsize ok !");';
    return tests

def tests_lstlast():
    tests = ""
    for i in range(TESTS_N):
        nb = random.randint(0, 10000000000)
        tests += inputs.create_list(nb)
        tests += "free(ft_lstlast(list{}));\n".format(nb)
    tests += 'puts("* ft_lstlast ok !");';
    return tests

def tests_lstiter():
    tests = ""
    for i in range(TESTS_N):
        nb = random.randint(0, 10000000000)
        tests += inputs.create_list(nb)
        tests += "ft_lstiter(list{}, {});\n".format(nb, inputs.input_del_func())
    tests += 'puts("* ft_lstiter ok !");';
    return tests

def tests_lstmap():
    tests = ""
    for i in range(TESTS_N):
        nb = random.randint(0, 10000000000)
        tests += inputs.create_list(nb)
        tests += "ft_lstmap(list{}, {});\n".format(nb, inputs.input_lstmap_func())
    tests += 'puts("* ft_lstmap ok !");';
    return tests

def tests_bonus():
    tests = ""
    tests += 'puts("\\n** Bonus");';
    tests += tests_lstnew()
    tests += tests_lstdelone()
    tests += tests_lstclear()
    tests += tests_lstaddfront()
    tests += tests_lstaddback()
    tests += tests_lstsize()
    tests += tests_lstiter()
    tests += tests_lstlast()
    tests += tests_lstmap()
    return tests
