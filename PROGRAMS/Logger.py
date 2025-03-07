# ============================================
# LICENCE D'UTILISATION
# ============================================
# Ce code est protégé par des droits d'auteur et est destiné à un usage personnel uniquement. 
# Vous n'êtes pas autorisé à le modifier, le distribuer, le vendre, ou à en faire des copies à des fins commerciales sans l'autorisation explicite de l'auteur.
# Toute tentative de modification, de revente, ou de redistribution du code sans permission constitue une violation de cette licence et pourra entraîner des poursuites judiciaires.
# 
# Propriétaire du code : Malveillance
# Version : 3.2
# Copyright © 2025
# ============================================



# ============================================
# USAGE LICENSE
# ============================================
# This code is copyrighted and intended for personal use only. 
# You are not allowed to modify, distribute, sell, or make copies of it for commercial purposes without explicit permission from the author.
# Any attempt to modify, resell, or redistribute the code without permission constitutes a breach of this license and may result in legal action.
# 
# Code Owner: Malveillance
# Version: 3.2
# Copyright © 2025
# ============================================






#Ce code est a but éducatif, tout usage malveillant ne sera en aucun cas de la faute de l'auteur
#This code is for educational purposes, any malicious use will in no way be the fault of the author.








import webbrowser
from colorama import init, Fore

init(autoreset=True)


ascii_art = '''
██╗      ██████╗  ██████╗  ██████╗ ███████╗██████╗ 
██║     ██╔═══██╗██╔════╝ ██╔════╝ ██╔════╝██╔══██╗
██║     ██║   ██║██║  ███╗██║  ███╗█████╗  ██████╔╝
██║     ██║   ██║██║   ██║██║   ██║██╔══╝  ██╔══██╗
███████╗╚██████╔╝╚██████╔╝╚██████╔╝███████╗██║  ██║
╚══════╝ ╚═════╝  ╚═════╝  ╚═════╝ ╚══════╝╚═╝  ╚═╝
'''

def show_menu():
   
    print(Fore.RED + ascii_art)


    print(Fore.RED + "[1] IP Logger")
    print(Fore.RED + "[2] Grabify")

def open_link(choice):
    if choice == "1":
     
        webbrowser.open("https://iplogger.org/")
        print(Fore.RED + "[+] Opening IP Logger...")
    elif choice == "2":
        
        webbrowser.open("https://grabify.link/")
        print(Fore.RED + "[+] Opening Grabify...")
    else:
        print(Fore.RED + "[!] Invalid choice, please select 1 or 2.")

def main():
    show_menu()
    
    
    choice = input(Fore.RED + "\nChoose an option [1/2]: ")
    open_link(choice)

if __name__ == "__main__":
    main()
