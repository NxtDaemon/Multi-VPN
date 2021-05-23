import os
import subprocess 

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


def ChooseVPN():
	'return the value of the chosen .ovpn file' 
	VPNs = os.listdir("/opt/VPNs")
	for value in enumerate(VPNs,1):
		if not value[1].endswith(".ovpn"):
			pass
		else:
			print(f"{NumColor}[{value[0]}]{RESET} : {ActiveColor}{value[1]}{RESET}")
	print("\n[?] : Input the VPN Number you wish to use \n ")
	while 1:
		try:
			Selected = int(input(f"{QuestionColor}>{RESET} "))-1
			return(VPNs[Selected]) 
		except IndexError:
			print(f"{ErrorColor}Sorry, The Number you Entered is not in the VPNs List{RESET}")
		except ValueError:
			print(f"{ErrorColor}Input Must be Numeric; Enter a Number{RESET}")
		except EOFError:
			print(f"{ErrorColor}Found `Ctrl+D` use Ctrl+C {RESET}")
		except Exception as Exc:
			print(f"{ErrorColor}Unexpected Error : {Exc} Class : {type(Exc).__name__}{RESET}")

def SetVPN(VPN):
	'Call the openvpn command and handle commands'
	Process = subprocess.call(["sudo","openvpn",f"/opt/VPNs/{VPN}"])

if __name__ == "__main__":
	VPN = ChooseVPN()
	# Note : the /usr/sbin/openvpn MUST be added to the /etc/sudoers file with a NOPASSWD otherwise the script must be run as root and that wouldnt be good Security wise
	# Add Something like this to /etc/sudoers 
	# '$(Username) ALL=(all) NOPASSWD: $(which openvpn)'
	# But ofc replace username and the value from 'which openvpn'
	# Also imo its a nice idea to add an alias for this so add something like `alias vpn="python3 $(location of VPN.py)"
	print(f"{NotificationColor}Starting VPN Now \n{RESET}")
	SetVPN(VPN)
	print(f"{Color.RESET}")

