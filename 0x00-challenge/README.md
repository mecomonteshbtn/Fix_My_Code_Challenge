# Fix_My_Code_Challenge

# 0x00. Fix my code

---
## Learning Objectives:bulb:
What you should learn from this project:
Fix my code is a new type of project, where we’ll jump into an existing code base and fix it!

Sometimes you will know the language, sometimes not.

Please download the repository [0x00-Fix_My_Code_Challenge](https://github.com/holbertonschool/0x00-Fix_My_Code_Challenge) and use it as initial files for all solutions.

You should not recode everything, just fix it!
---

### [0. FizzBuzz](./0-fizzbuzz.py)
* Please take a look at my implementation of FizzBuzz in Python:
Something is going wrong….
```
$ ./0-fizzbuzz.py 50
1 2 Fizz 4 Buzz Fizz 7 8 Fizz Buzz 11 Fizz 13 14 Fizz 16 17 Fizz 19 Buzz Fizz 22 23 Fizz Buzz 26 Fizz 28 29 Fizz 31 32 Fizz 34 Buzz Fizz 37 38 Fizz Buzz 41 Fizz 43 44 Fizz 46 47 Fizz 49 Buzz
$
```
15 should print FizzBuzz not Fizz

### [1. Print square](./1-print_square.js)
* Please take a look at my implementation of printing a square in Javascript:
Something is going wrong….
```
$ ./1-print_square.js 4
####
####
####
####
$ ./1-print_square.js 10
################
################
################
################
################
################
################
################
################
################
################
################
################
################
################
################
$
```
./1-print_square.js 10 should print a square of size 10…

### [2. Sort](./2-sort.rb)
* Please find here my implementation of sorting arguments in Ruby:
Something is going wrong….
```
$ ruby 2-sort.rb 12 41 2 C 9 -9 31 fun -1 32
31
32
12
41
2
9
-9
-1
$
```

### [3. User password](./3-user.py )
* Please find here my implementation of a User class in Python:
Something is going wrong….
```
$ ./3-user.py 
Test User
is_valid_password should return True if it's the right password
$
```
My tests should not print any error…

### [4. Double linked list](./4-delete_dnodeint/)
* Please find here my implementation of a Double linked list in C:
Something is going wrong….
```
$ gcc -Wall -pedantic -Werror -Wextra main.c free_dlistint.c print_dlistint.c add_dnodeint_end.c delete_dnodeint_at_index.c -o delete_dnodeint
$ ./delete_dnodeint 
0
1
2
3
4
98
402
1024
-----------------
0
1
2
3
4
0
402
1024
-----------------
1
2
3
4
0
402
1024
-----------------
2
3
4
0
402
1024
-----------------
3
4
0
402
1024
-----------------
4
0
402
1024
-----------------
0
402
1024
-----------------
402
1024
-----------------
-----------------
-----------------
-----------------
-----------------
-----------------
-----------------
-----------------
-----------------
-----------------
$
```
It doesn’t look right… 
---

## Author
* **Robinson Montes** - [mecomonteshbtn](https://github.com/mecomonteshbtn)
