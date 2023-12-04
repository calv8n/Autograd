import subprocess
import time

def execution(FILE_NAME, exename) -> str:
    cmd = ["gcc", FILE_NAME,]
    run = [f"./exname 2 2 1 2 3 4"]
    process = subprocess.Popen(
        cmd,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        stdin=subprocess.PIPE,
        text=True,
    )
    process.wait(10)
    x = subprocess.run(run, stdout=subprocess.PIPE, stdin=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    x = x.stdout
    return x


#admin_output = execution("sudoku.c", "sudoku")

student_output = execution("a2d.c", "a2d")


# Vanilla compare
def compare(a_o, s_o) -> bool:
    l_a = a_o.split(" ")
    l_s = s_o.split(" ")
    if len(l_s) == len(l_a):
        for i in range(len(l_a)):
            if l_a[i] != l_s[i]:
                return False
    else:
        return False
    return True


#print("Admin Output:\n", admin_output)
print("User Output:\n", student_output)
#print("Does it match: ", compare(admin_output, student_output))
