import subprocess


def execution(FILE_NAME, exename) -> str:
    cmd = ["gcc", FILE_NAME, "-o", exename]
    run = [f"./{exename}"]
    process = subprocess.Popen(
        cmd,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
    )
    process.wait(10)
    x = subprocess.run(run, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    x = x.stdout
    return x


admin_output = execution("utils/admin/sudoku.c", "sudoku")
student_output = execution("utils/student/sudoku2.c", "sudoku2")


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


print(admin_output)
print(student_output)
print("Does it match: ", compare(admin_output, student_output))
