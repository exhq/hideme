def main():
    import mouse
    import subprocess
    import os
    xmouse = mouse.get_position()
    ssubprocess = subprocess.Popen(
        "xrandr --query", shell=True, stdout=subprocess.PIPE)
    shit = ssubprocess.stdout.read().decode("utf-8").split("\n")

    for i in range(len(shit)):
        line = shit[i]
        if " connected" in line:
            info = line[line.find("+")+1:]
            currentmonitor = (info[:info.find(" ")].split("+"))
            mouse.move(int(currentmonitor[0])+1, int(currentmonitor[1])+1)
            os.system(f"i3-msg workspace hidden{i}")
    mouse.move(xmouse[0], xmouse[1])
main()
