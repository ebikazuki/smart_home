import subprocess

path = "python3 rm3_mini_controller/BlackBeanControl.py -c "

def temp_on():
    subprocess.call(path + "power_on",shell=True)

if __name__ == '__main__':
    temp_on()

