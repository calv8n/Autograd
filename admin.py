import json
import os

q_id = input("Enter question id")
question = input("Enter Question")
input_file = input("Enter Input File, every new input needs to be seperated by space")
input_file = input_file.split(" ")
output_type = input("Enter output type")
d1 = {}
d2 = {}
d2["input file"] = input_file
d2["output type"] = output_type
d2["question"] = question





op_store = []
for i in range(len(input_file)):
    os.popen("gcc fib.c")
    op = os.popen("./a.out" + " " + input_file[i]).read().rstrip()
    
    print(op)
    op_store.append(op)

d2["output"] = op_store

d1[q_id] = d2
'''
    if len(x[i]) == len(ls):
        for j in range(len(x[i])):
            if ls[i] != x[i][j]:
                print("Not Equal")
                break
        print("Equal")
    else:
        print("Not Equal")
    '''
    





'''
file = open("admin.json", mode='w')

json.dump()'''


print(op_store)

with open("admin.json", mode='w', encoding='utf-8') as feedsjson:
    
    
    json.dump(d1, feedsjson)