import os
import platform

def get_username():
    print(f"The current logged-in user is: {os.getlogin()}")

def get_devicename():
    print(f"The device name is: {platform.node()}")