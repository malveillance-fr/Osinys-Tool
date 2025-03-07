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

