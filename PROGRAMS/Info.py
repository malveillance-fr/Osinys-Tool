from colorama import init, Fore

init(autoreset=True)

ascii_art = '''
████████╗ ██████╗  ██████╗ ██╗         ██╗███╗   ██╗███████╗ ██████╗     
╚══██╔══╝██╔═══██╗██╔═══██╗██║         ██║████╗  ██║██╔════╝██╔═══██╗    
   ██║   ██║   ██║██║   ██║██║         ██║██╔██╗ ██║█████╗  ██║   ██║    
   ██║   ██║   ██║██║   ██║██║         ██║██║╚██╗██║██╔══╝  ██║   ██║    
   ██║   ╚██████╔╝╚██████╔╝███████╗    ██║██║ ╚████║██║     ╚██████╔╝    
   ╚═╝    ╚═════╝  ╚═════╝ ╚══════╝    ╚═╝╚═╝  ╚═══╝╚═╝      ╚═════╝     
'''

info_text = '''
[+] ~ Creator : Malveillance
[+] ~ Contact : 2l0x (Discord)
[+] ~ License : Copyright (c) [2025] Osinys : Malveillance
[+] ~ Help ? : Open the Help's file (help.txt) 
'''

def display_ascii_and_info():
    print(Fore.RED + ascii_art)
    print(Fore.RED + info_text)

display_ascii_and_info()

input("Enter For Return To Menu")