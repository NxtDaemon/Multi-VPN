# Multi-VPN
Ability to use multiple VPNs from the same command with little config, only uses OpenVPN for now.

## Setup
you should run the setup.py first passing all VPN files to it with relative or absolute paths 
syntax : `sudo python3 setup.py file1.ovpn file2.ovpn`
it is advised to add the path to the OpenVPN binary with a NOPASSWD e.g 
add the following to your /etc/sudoers file [ $(Username) ALL=(all) NOPASSWD: $(which openvpn) ]
Once this is done you can run the `VPN.py` file without sudo 

## Using VPN.py 
Simply run the file ensuring you have completed prior steps with the following `python3 VPN.py` 
However if like me you wish to type less add `alias vpn="python3 $(location of VPN.py)` to your ~/.zsh_aliases file or equivalent for other shells 
