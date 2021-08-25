# Multi-VPN
Ability to use multiple VPNs from the same command with little config, only uses OpenVPN for now.

## Setup
- clone the repo with `git clone https://github.com/NxtDaemon/Multi-VPN` 
- you should run the setup.py first passing all VPN files to it with relative or absolute paths 
- syntax : `sudo python3 setup.py file1.ovpn file2.ovpn`
- it is advised to add the path to the OpenVPN binary with a NOPASSWD e.g 
- add the following to your /etc/sudoers file [ `$(whoami) ALL=(ALL) NOPASSWD: $(which openvpn)`]
- Once this is done you can run the `VPN.py` file without sudo 

## Using VPN.py 
Simply run the file ensuring you have completed prior steps with the following `python3 VPN.py`.
However if like me you wish to type less add `alias vpn="python3 $(location of VPN.py)` to your ~/.zsh_aliases file or equivalent for other shells 

## Archive 
This project is now done to the standard I want it to be and dont see anything interesting or good I could futher changes within it <br> 
should you think of anything please do contact me and i'll implement it at https://nxtdaemon.xyz/contact
