import os
import shutil
import sys 

# Notes : 
# Run with Sudo as it makes PermissionErrors otherwise 
# Syntax `sudo python3 setup.py` 

class Color:
	# If you wish to use custom colors add them here and change the varibles below
    PURPLE = '\033[95m'
    CYAN = '\033[96m'
    DARKCYAN = '\033[36m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    BLINKING = '\033[5m'
    RESET = '\033[0m'

ActiveColor = Color.GREEN
QuestionColor = Color.BOLD+Color.YELLOW
ErrorColor = Color.RED
NumColor = Color.PURPLE+Color.BOLD
NotificationColor = Color.CYAN
RESET = Color.RESET

VPNFiles = sys.argv
VPNFiles.pop(0)

FilesInOpt = os.listdir("/opt/")
if "VPNs"  in FilesInOpt:
	print(f"{ErrorColor}Error : there is already a /opt/VPNs/ Directory{RESET}")
else:
	try:
		os.mkdir("/opt/VPNs")
		print(f"{ActiveColor}Directory Successfully Created at `/opt/VPNs/`{RESET}")
		if VPNFiles:
			print(f"{ActiveColor}Moving VPN Files Now{RESET}")
			for file in VPNFiles: # Will also need sudo privs but due to the catch before shouldn't cause an issue
				src = file
				destination = "/opt/VPNs/"
				shutil.copy(file,destination)
			print(f"{ActiveColor}Successfully Copied VPN Files{RESET}")

	except Exception as Exc:
		Content = ""
		if type(Exc) == PermissionError:
			Content += "\nDid you forget to add `sudo`?"
		print(f"{ErrorColor}CRITICAL : Following Error was Found '{Exc}'{Content}{RESET}")
		exit()
