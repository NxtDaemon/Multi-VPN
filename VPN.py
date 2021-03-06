import os
import subprocess 
import time 

# Written By NxtDaemon Any Issues or Additions you would like please contact me here https://nxtdaemon.xyz/contact
#  __    __            __     _______                                                   
# |  \  |  \          |  \   |       \                                                  
# | ▓▓\ | ▓▓__    __ _| ▓▓_  | ▓▓▓▓▓▓▓\ ______   ______  ______ ____   ______  _______  
# | ▓▓▓\| ▓▓  \  /  \   ▓▓ \ | ▓▓  | ▓▓|      \ /      \|      \    \ /      \|       \ 
# | ▓▓▓▓\ ▓▓\▓▓\/  ▓▓\▓▓▓▓▓▓ | ▓▓  | ▓▓ \▓▓▓▓▓▓\  ▓▓▓▓▓▓\ ▓▓▓▓▓▓\▓▓▓▓\  ▓▓▓▓▓▓\ ▓▓▓▓▓▓▓\
# | ▓▓\▓▓ ▓▓ >▓▓  ▓▓  | ▓▓ __| ▓▓  | ▓▓/      ▓▓ ▓▓    ▓▓ ▓▓ | ▓▓ | ▓▓ ▓▓  | ▓▓ ▓▓  | ▓▓
# | ▓▓ \▓▓▓▓/  ▓▓▓▓\  | ▓▓|  \ ▓▓__/ ▓▓  ▓▓▓▓▓▓▓ ▓▓▓▓▓▓▓▓ ▓▓ | ▓▓ | ▓▓ ▓▓__/ ▓▓ ▓▓  | ▓▓
# | ▓▓  \▓▓▓  ▓▓ \▓▓\  \▓▓  ▓▓ ▓▓    ▓▓\▓▓    ▓▓\▓▓     \ ▓▓ | ▓▓ | ▓▓\▓▓    ▓▓ ▓▓  | ▓▓ 
#  \▓▓   \▓▓\▓▓   \▓▓   \▓▓▓▓ \▓▓▓▓▓▓▓  \▓▓▓▓▓▓▓ \▓▓▓▓▓▓▓\▓▓  \▓▓  \▓▓ \▓▓▓▓▓▓ \▓▓   \▓▓

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

    NumColor = DARKCYAN
    QuestionColor = BOLD+YELLOW
    ErrorColor = RED+BOLD
    InfoColor = CYAN 
    SuccessColor = GREEN
    InputColor = GREEN+BOLD

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
		return(input(f"{Color.QuestionColor}[?] - {Message}{Color.RESET}\n{Color.InputColor}>{Color.RESET}"))

	def OutputVPNs(Value):
		'Specific to this code; uses format to print numbers then names'
		print(f"{Color.NumColor}{Value[0]}{Color.RESET} : {Color.InfoColor}{Value[1]}{Color.RESET}")


def ChooseVPN():
	'return the value of the chosen .ovpn file' 
	VPNs = os.listdir("/opt/VPNs")
	for value in enumerate(VPNs,1):
		if not value[1].endswith(".ovpn"):
			pass
		else:
			Notify.OutputVPNs(value)
	while 1:
		try:
			Selected = Notify.Question("Input the VPN Number you wish to use")
			if Selected.lower() == "exit":
				exit()
			else: 
				Selected = int(Selected)-1
				return(VPNs[Selected]) 
		except IndexError:
			Notify.Error("Sorry, The Number you Entered is not in the VPNs List")
		except ValueError:
			Notify.Error("Input Must be Numeric; Enter a Number")
		except EOFError:
			Notify.Error("Found `Ctrl+D` use Ctrl+C or type 'Exit'")
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
	

