import os
import psutil
import platform
from cpuinfo import get_cpu_info

def get_username():
    print(f"The current logged-in user is: {os.getlogin()}")

def get_devicename():
    print(f"The device name is: {platform.node()}")

def get_cpu_info():
    pass

def get_ram():
    print(f"Total RAM installed: {round(psutil.virtual_memory().total/1000000000, 2)} GB")