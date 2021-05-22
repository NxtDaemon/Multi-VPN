import os
import subprocess 

def ChooseVPN():
	VPNs = os.listdir("/opt/VPNs")
	for value in enumerate(VPNs,1):
		print(f"[{value[0]}] : {value[1]}")
	print("[?] : Input the VPN Number you wish to use \n ")
	while 1:
		Selected = int(input("> "))-1
		if VPNs[Selected]:
			return(VPNs[Selected]) 
		else:
			print("Sorry, The Number you Entered is not in the VPNs List")

def SetVPN(VPN):
	Process = subprocess.call(["sudo","openvpn",f"/opt/VPNs/{VPN}"])

if __name__ == "__main__":
	VPN = ChooseVPN()
	# Note : the /usr/sbin/openvpn MUST be added to the /etc/sudoers file with a NOPASSWD otherwise the script must be run as root and that wouldnt be good Security wise
	# Add Something like this to /etc/sudoers 
	# '$(Username) ALL=(all) NOPASSWD: $(which openvpn)'
	# But ofc replace username and the value from 'which openvpn'
	# Also imo its a nice idea to add an alias for this so add something like `alias vpn="python3 $(location of VPN.py)"
	print("Starting VPN Now \n")
	SetVPN(VPN)

