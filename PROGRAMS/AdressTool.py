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
from colorama import Fore, init

init(autoreset=True)

print(Fore.RED + '''
█████╗ ██████╗ ██████╗ ███████╗███████╗███████╗    ████████╗ ██████╗  ██████╗ ██╗     
██╔══██╗██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝    ╚══██╔══╝██╔═══██╗██╔═══██╗██║     
███████║██║  ██║██████╔╝█████╗  ███████╗███████╗       ██║   ██║   ██║██║   ██║██║     
██╔══██║██║  ██║██╔══██╗██╔══╝  ╚════██║╚════██║       ██║   ██║   ██║██║   ██║██║     
██║  ██║██████╔╝██║  ██║███████╗███████║███████║       ██║   ╚██████╔╝╚██████╔╝███████╗
╚═╝  ╚═╝╚═════╝ ╚═╝  ╚═╝╚══════╝╚══════╝╚══════╝       ╚═╝    ╚═════╝  ╚═════╝ ╚══════╝
''')

first_name = input(Fore.GREEN + "Enter first name: ")
last_name = input(Fore.GREEN + "Enter last name: ")

search_urls = [
    f"https://www.pagesjaunes.fr/pagesblanches/recherche?quoiqui={first_name}+{last_name}",
    f"https://www.tumblr.com/search/{first_name}%20{last_name}",
    f"https://www.peekyou.com/{first_name}-{last_name}",
    f"https://www.118000.fr/search?who={first_name}+{last_name}"
]

open_result = input(Fore.YELLOW + "\nOpen result ? (y/n): ").lower()

if open_result == 'y':
    print(Fore.YELLOW + "\nSearching for results...")

    for url in search_urls:
        print(Fore.CYAN + f"Opening: {url}")
        webbrowser.open(url)

    print(Fore.GREEN + "\nSearch complete! Check the opened tabs for results.")
else:

