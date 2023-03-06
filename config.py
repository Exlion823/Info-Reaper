import platform

# get the os type
OS_TYPE = platform.system()
if OS_TYPE == "Darwin":
    OS_TYPE = "Mac"

