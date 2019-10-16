# Libftdestructor

The purpose of tis script is to force the project libft2019 of school 42 to segfault or sigabort.
**Warning !**
This script does NOT test the output of the function, it only tries to make it segfault.

## Usage
The script will generate a main.c file that use a static library of libft. So please copy libft.h and libft.a in the same folder as test.py. 
```sh
git clone https://github.com/t0mm4rx/libftdestructor
cd # your libft repo
make bonus
cp libft.* path-of-libftdestructor
cd path-of-libftdestructor
python3.7 test.py
```
## ToDo
- [ ] Part 1 functions
- [ ] Bonus functions
