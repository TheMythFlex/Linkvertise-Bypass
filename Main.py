import ctypes
import re
import webbrowser
from colorama import Fore, Back, Style
from termcolor import colored
import colorama
import requests
colorama.init()
s = requests.session()

ctypes.windll.kernel32.SetConsoleTitleW("Linkvertise Bypass - Made by Flex#8629")
print(colored("""  

                 
             ██╗░░░░░██╗███╗░░██╗██╗░░██╗░░░░░░██╗░░░██╗███████╗██████╗░░░░░░░████████╗██╗░██████╗███████╗
             ██║░░░░░██║████╗░██║██║░██╔╝░░░░░░██║░░░██║██╔════╝██╔══██╗░░░░░░╚══██╔══╝██║██╔════╝██╔════╝
             ██║░░░░░██║██╔██╗██║█████═╝░█████╗╚██╗░██╔╝█████╗░░██████╔╝█████╗░░░██║░░░██║╚█████╗░█████╗░░
             ██║░░░░░██║██║╚████║██╔═██╗░╚════╝░╚████╔╝░██╔══╝░░██╔══██╗╚════╝░░░██║░░░██║░╚═══██╗██╔══╝░░
             ███████╗██║██║░╚███║██║░╚██╗░░░░░░░░╚██╔╝░░███████╗██║░░██║░░░░░░░░░██║░░░██║██████╔╝███████╗
             ╚══════╝╚═╝╚═╝░░╚══╝╚═╝░░╚═╝░░░░░░░░░╚═╝░░░╚══════╝╚═╝░░╚═╝░░░░░░░░░╚═╝░░░╚═╝╚═════╝░╚══════╝
                                                   
                                                    < Bypass Link Advertisement >
                                                                                                                                       
""", "red", attrs=["bold"]))




user_input = input("Enter linkvertise Link To Bypass: ")
print("\n")

r = s.get("https://bypass.bot.nu/bypass2?url={}".format(user_input))
Link = re.findall('"destination": "(.*?)"', r.text)
Link = str(Link).replace("[", "")
Link = str(Link).replace("'", "")
Link = str(Link).replace("]", "")

print(colored("Here U Go: " + Link, "blue", attrs=["bold"]))
print("\n")
print(colored("If u wish to open link in browser click enter, if not close window.", "red", attrs=["bold"]))
input("")

webbrowser.open(Link)


