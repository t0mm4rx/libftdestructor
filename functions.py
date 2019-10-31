import inputs
import subprocess

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

def fill_prototype(str):
    while ("<string>" in str):
        str = str.replace("<string>", inputs.input_string(), 1)
    while ("<uint>" in str):
        str = str.replace("<uint>", inputs.input_uint(), 1)
    while ("<int>" in str):
        str = str.replace("<int>", inputs.input_int(), 1)
    while ("<char>" in str):
        str = str.replace("<char>", inputs.input_char(), 1)
    while ("<map_func>" in str):
        str = str.replace("<map_func>", inputs.input_map_func(), 1)
    while ("<del_func>" in str):
        str = str.replace("<del_func>", inputs.input_del_func(), 1)
    while ("<lstmap_func>" in str):
        str = str.replace("<lstmap_func>", inputs.input_lstmap_func(), 1)
    while ("<input_elem>" in str):
        str = str.replace("<input_elem>", inputs.input_elem(), 1)
    return str

def make_test(name, PATH, prototype, n):
    print("{:19s} ".format(name), end="")
    tests = ""
    for i in range(n):
        tests += "\t"
        tests += fill_prototype(prototype)
        tests += "\n"
    create_main(name, PATH, tests)
    result = compile_main(name, PATH)
    if (len(result) == 0):
        print("{:>10s}".format("Ok"))
        return
    if ("Abort trap" in str(result)):
        print("{:>10s}".format("Abort"))
        return
    if ("segfault" in str(result)):
        return
        print("{:>10s}".format("Segfault"))
    print("{:>10s}".format("Error"))
