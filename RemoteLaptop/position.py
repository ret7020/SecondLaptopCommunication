import subprocess

while True:
    x, y = list(map(int, subprocess.check_output(["hyprctl", "cursorpos"]).decode("utf-8").strip().split(", ")))
    print(x, y)

