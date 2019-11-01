import inputs
import subprocess
import random

def create_main(name, path, tests):
    main_template = ""
    with open("main_template.c", "r") as file:
        main_template = file.read()
    main_template = main_template.replace("$$1", path)
    main_template = main_template.replace("$$2", tests)
    subprocess.run("mkdir -p tests", shell=True)
    with open("./tests/{}.c".format(name), "w+") as file:
        file.write(main_template)

def compile_main(name, path):
    return subprocess.run("gcc ./tests/{}.c -L{} -lft -Wall -Werror -Wextra -g3 -fsanitize=address && ./a.out".format(name, path), shell=True, stderr=subprocess.PIPE).stderr

def fill_prototype(s, list=None, pointer=None, pointer_size=0):
    while ("<string>" in s):
        s = s.replace("<string>", inputs.input_string(), 1)
    while ("<uint>" in s):
        s = s.replace("<uint>", inputs.input_uint(), 1)
    while ("<int>" in s):
        s = s.replace("<int>", inputs.input_int(), 1)
    while ("<char>" in s):
        s = s.replace("<char>", inputs.input_char(), 1)
    while ("<map_func>" in s):
        s = s.replace("<map_func>", inputs.input_map_func(), 1)
    while ("<del_func>" in s):
        s = s.replace("<del_func>", inputs.input_del_func(), 1)
    while ("<lstmap_func>" in s):
        s = s.replace("<lstmap_func>", inputs.input_lstmap_func(), 1)
    while ("<elem>" in s):
        s = s.replace("<elem>", inputs.input_elem(), 1)
    while ("<list>" in s):
        s = s.replace("<list>", "list{}".format(list), 1)
    while ("<pointer>" in s):
        s = s.replace("<pointer>", "ptr{}".format(pointer), 1)
    while ("<pointer_size>" in s):
        s = s.replace("<pointer_size>", str(pointer_size), 1)
    while ("<suint>" in s):
        s = s.replace("<suint>", inputs.input_short_uint(), 1)
    return s

def make_test(name, PATH, prototype, n, create_list=False, create_pointer=False):
    tests = ""
    for i in range(n):
        nb_list = None
        if (create_list):
            nb_list = random.randint(0, 10000000000)
            tests += inputs.create_list(nb_list)
        nb_pointer = None
        size_pointer = 0
        if (create_pointer):
            nb_pointer = random.randint(0, 10000000000)
            size_pointer = random.randint(0, 10)
            tests += inputs.create_pointer(nb_pointer, size_pointer)
        tests += "\t"
        tests += fill_prototype(prototype, list=nb_list, pointer=nb_pointer, pointer_size=size_pointer)
        tests += "\n"
    create_main(name, PATH, tests)
    result = compile_main(name, PATH)
    #print(result)
    if (len(result) > 0):
        print("\u001b[31m", end="")
    else:
        print("\u001b[32m", end="")
    print("{:23s} ".format(name), end="")
    if (len(result) == 0):
        print("{:>6s}".format("Ok"))
    elif ("Abort trap" in str(result)):
        print("{:>6s}".format("Abort"))
    elif ("segfault" in str(result)):
        print("{:>6s}".format("Segfault"))
    else:
        print("{:>6s}".format("Error"))
    print("\u001b[0m", end="")
