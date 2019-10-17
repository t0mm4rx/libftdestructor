# Libftdestructor

The purpose of tis script is to force the project libft2019 of school 42 to segfault or sigabort.

**Warning !**

This script does NOT test the output of the function, it only tries to make it segfault.

Tests aren't logical, it just tries to crash your lib. For exemple, it sends NULL pointer as function parameter.

Don't use this script in correction, most of projects that passes Moulinette segfaults with this script.

The purpose of this script is only to be 100% sure your libft won't segfault, make your own tests. Please view this tool only as an helper.

Made by tmarx

## Usage
The script will generate a main.c file. It will make your library and link it.
```sh
git clone https://github.com/t0mm4rx/libftdestructor
cd libftdestructor
python3.7 test.py path-of-libft [bonus: yes|no]
```

## ToDo
- [ ] Part 1 functions
- [x] Bonus functions

## Known bugs
- "Cannot find libft.h"
  If so, copy paste the libft.h file at the root of libftdestructor
- Cannot compile bonuses, "undefined symbol ft_function", maybe your bonuses function are not in the same header file. This script isn't compatible with this file structure. Also, check you have a bonus rule in your Makefile.
