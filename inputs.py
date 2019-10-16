import random
import string

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

def input_int():
	choice = random.choice([0, 1, 2, 3])
	if (choice == 0):
		return random.randint(-2147483648, 2147483647)
	if (choice == 1):
		return 2147483647
	if (choice == 2):
		return -2147483648
	if (choice == 3):
		return 0

def input_char():
	choice = random.choice([0, 1])
	if (choice == 0):
		return "'" + random.choice(string.ascii_letters + string.digits) + "'"
	if (choice == 1):
		return "'\\0'"

def input_map_func():
	choice = random.choice([0, 1])
	if (choice == 0):
		return "&map"
	if (choice == 1):
		return "NULL"

def input_del_func():
	choice = random.choice([0, 1])
	if (choice == 0):
		return "&del"
	if (choice == 1):
		return "NULL"

def input_lstmap_func():
	choice = random.choice([0, 1])
	if (choice == 0):
		return "&lstmap"
	if (choice == 1):
		return "NULL"

def input_elem():
	choice = random.choice([0, 1])
	if (choice == 0):
		return "ft_lstnew({})".format(input_string())
	if (choice == 1):
		return "NULL"

def create_list(n):
	res = ""
	res += "t_list *list{} = {};\n".format(n, input_elem())
	for i in range(random.randint(0, 3)):
		res += "ft_lstadd_back(&list{}, {});\n".format(n, input_elem())
	return res
