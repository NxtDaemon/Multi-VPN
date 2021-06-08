import os
import subprocess 
import time 

class Color:
    'Class for Colors to be used in Execution'
    PURPLE = '\033[95m'
    CYAN = '\033[96m'
    DARKCYAN = '\033[36m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    RESET = '\033[0m'

    QuestionColor = BOLD+YELLOW
    ErrorColor = RED+BOLD
    InfoColor = CYAN 
    SuccessColor = GREEN

class Notify():
	'Managed what type of message is sent'

	def Error(Message):
		'Error Messages'
		print(f"{Color.ErrorColor}[!] - {Message}{Color.RESET}")

	def Info(Message):
		'Infomation Messages'
		print(f"{Color.InfoColor}[*] - {Message}{Color.RESET}")

	def Success(Message):
		'Success Messages'
		print(f"{Color.SuccessColor}[$] - {Message}{Color.RESET}")

	def Question(Message):
		'Get infomation from user'
		input(f"{Color.QuestionColor}[?] - {Message}{Color.RESET}")
  
    def OutputVPNs(Value):
        'Specific to this code; uses format to print numbers then names'
        print(f"{NumColor}{Value[0]}{RESET} : {ActiveColor}{Value[1]}{RESET}")


def ChooseVPN():
	'return the value of the chosen .ovpn file' 
	VPNs = os.listdir("/opt/VPNs")
	for value in enumerate(VPNs,1):
		if not value[1].endswith(".ovpn"):
			pass
		else:
			Notify.OutputVPNs(value)
	Selected = Notify.Question("Input the VPN Number you wish to use\n> ")
	while 1:
		try:
			Selected = int(Selected)-1
			return(VPNs[Selected]) 
		except IndexError:
            Notify.Error("Sorry, The Number you Entered is not in the VPNs List")
		except ValueError:
			Notify.Error("Input Must be Numeric; Enter a Number")
		except EOFError:
			Notify.Error("Found `Ctrl+D` use Ctrl+C")
		except Exception as Exc:
			Notify.Error(f"Unexpected Error : {Exc}\nClass : {type(Exc).__name__}")

def SetVPN(VPN):
	'Call the OpenVPN command'
	Process = subprocess.call(["sudo","openvpn",f"/opt/VPNs/{VPN}"])

if __name__ == "__main__":
	VPN = ChooseVPN()
	# Note : the /usr/sbin/openvpn MUST be added to the /etc/sudoers file with a NOPASSWD otherwise the script must be run as root and that wouldnt be good Security wise
	# Add Something like this to /etc/sudoers 
	# '$(Username) ALL=(all) NOPASSWD: $(which openvpn)'
	# But ofc replace username and the value from 'which openvpn'
	# Also imo its a nice idea to add an alias for this so add something like `alias vpn="python3 $(location of VPN.py)"
	Notify.Success("Starting VPN Now")
    time.sleep(1)
    SetVPN(VPN)
	

