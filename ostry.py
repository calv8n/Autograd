import os

os.popen("gcc fib.c")
x = os.popen("./a.out 4")
print(x.readlines())