import subprocess
import time
import os
import json

def execution(FILE_NAME, input_n) -> str:
    cmd = ["gcc", FILE_NAME,]
    run = [f"./exname 2 2 1 2 3 4"]
    os.popen("gcc fib.c")
    x = os.popen("./a.out" + " " + input_n).read().rstrip()
    return x


#admin_output = execution("sudoku.c", "sudoku")

#student_output = execution("a2d.c", "a2d")


# Vanilla compare
def compare(a_o, s_o) -> bool:
    l_a = a_o.split()
    l_s = s_o.split()
    if len(l_s) != len(l_a):
        return False      
    elif len(l_s) == len(l_a):
        for i in range(len(l_a)):
            if l_a[i] != l_s[i]:
                return False
    return True

f = open("admin.json", encoding='utf-8')
v = json.load(f)
print(v['3']["output"])
for i in v['3']:
    print(i)
op_store = []
input_file = v['3']["input file"]
for i in range(len(input_file)):
    os.popen("gcc fib.c")
    op = os.popen("./a.out" + " " + input_file[i]).read().rstrip()
    print(op)
    op_store.append(op)
for i in range(len(input_file)):
    print(compare(op_store[i], v['3']["output"][i]))


#print("Admin Output:\n", admin_output)
#print("User Output:\n", student_output)
#print("Does it match: ", compare(admin_output, student_output))
