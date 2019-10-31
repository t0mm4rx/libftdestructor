# Libftdestructor

The purpose of this script is to force the project libft2019 of school 42 to segfault or sigabort.

**Warning !**

This script does NOT test the output of the functions (KO), it only tries to make it segfault.

Tests aren't logical, it just tries to crash your lib. For exemple, it sends NULL pointer as a function parameter.

Don't use this script during corrections, most of projects that passes the Moulinette can segfault with this script.

The purpose of this script is to be 100% sure your libft won't segfault.
Make your own tests! Please consider this tool only as a helper.

Made by **tmarx** with the help of **vgoldman**

## Usage
```sh
git clone https://github.com/t0mm4rx/libftdestructor
cd libftdestructor
sh run.sh <path-of-libft> [12B]

# EXEMPLES
# Part 1 and 2
sh run.sh ../libft 12
# Only bonus
sh run.sh ../libft B
# All parts
sh run.sh ../libft
```

## FAQ
- "Cannot find libft.h"
  The libft.h file should be at the root of your libft project.
- Cannot compile bonuses, "undefined symbol ft_function"
  Maybe your bonuses function are not in the same header file. This script isn't compatible with this file structure. Also, check if you have a bonus rule in your Makefile.
- Other errors
  The subject might change, and tests could not be updated. If so, contact tmarx on the intra or at tom[at]tommarx[dot]fr. You can also try to edit tests yourself and make a pull request.

## ToDo
  - [ ] Part 1 functions
  - [x] Bonus functions
  - [x] New design
