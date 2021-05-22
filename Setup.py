import os
import shutil
import sys 

# Notes : 
# Run with Sudo as it makes PermissionErrors otherwise 
# Syntax `sudo python3 setup.py` 

VPNFiles = sys.argv
VPNFiles.pop(0)

FilesInOpt = os.listdir("/opt/")
if "VPNs"  in FilesInOpt:
	print("Error : there is already a /opt/VPNs/ Directory")
else:
	try:
		os.mkdir("/opt/VPNs")
		print("/opt/VPNs/ Directory Successfully Created")
		if VPNFiles:
			print("Moving VPN Files Now")
			for file in VPNFiles: # Will also need sudo privs but due to the catch before shouldn't cause an issue
				src = file
				destination = "/opt/VPNs/"
				shutil.copy(file,destination)
			print("Successfully Copied VPN Files")

	except Exception as Exc:
		Content = ""
		if type(Exc) == PermissionError:
			Content += "\nDid you forget to add `sudo`?"
		print(f"CRITICAL : Following Error was Found '{Exc}'{Content}")
		exit()
