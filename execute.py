import subprocess


def execution(FILE_NAME) -> str:
    cmd = ["gcc", FILE_NAME]
    run = ["./a.out"]
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
