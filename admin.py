import json
import os
'''
question = input("Enter Question")
input_file = input("Enter Input File, every new input needs to be seperated by space")
input_file = input_file.split(" ")
output_type = input("Enter output type")
d1 = {}
d2 = {}
d2["input file"] = input_file
d2["output type"] = output_type

'''

x = ["0 1", "0 1 1", "0 1 1 2", "0 1 1 2 3", "0 1 1 2 3 5", "0 1 1 2 3 5 8", "0 1 1 2 3 5 8 13", "0 1 1 2 3 5 8 13 21", "0 1 1 2 3 5 8 13 21 34","0 1 1 2 3 5 8 13 21 34 55"]

y = ["2", "3", "4", "5", "6", "7", "8", "9", "10"]
for i in range(len(y)):
    os.popen("gcc fib.c")
    op = os.popen("./a.out" + f" {y[i]}").read()
    ls = op.split()
    x[i] = x[i].split()
    print(ls)
    if len(x[i]) == len(ls):
        for j in range(len(x[i])):
            if ls[i] != x[i][j]:
                print("Not Equal")
                break
        print("Equal")
    else:
        print("Not Equal")
    
    





'''
file = open("admin.json", mode='w')

json.dump()'''


