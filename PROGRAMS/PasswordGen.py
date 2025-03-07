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








import random
import string
import os

from pystyle import Colorate, Colors

os.system('mode con: cols=120 lines=30')

def generate_password(digits, letters):
    digits_part = ''.join(random.choice(string.digits) for _ in range(digits))
    letters_part = ''.join(random.choice(string.ascii_letters) for _ in range(letters))
    
    password = ''.join(random.sample(digits_part + letters_part, len(digits_part + letters_part)))
    
    return password

def password_force(length):
    if length < 10:
        return "LOW"
    elif length < 25:
        return "MEDIUM"
    else:
        return "HARD"

def save_password(password, force):
    ascii_art = '''
██████╗  █████╗ ███████╗███████╗     ██████╗ ███████╗███╗   ██╗███████╗██████╗  █████╗ ████████╗ ██████╗ ██████╗ 
██╔══██╗██╔══██╗██╔════╝██╔════╝    ██╔════╝ ██╔════╝████╗  ██║██╔════╝██╔══██╗██╔══██╗╚══██╔══╝██╔═══██╗██╔══██╗
██████╔╝███████║███████╗███████╗    ██║  ███╗█████╗  ██╔██╗ ██║█████╗  ██████╔╝███████║   ██║   ██║   ██║██████╔╝
██╔═══╝ ██╔══██║╚════██║╚════██║    ██║   ██║██╔══╝  ██║╚██╗██║██╔══╝  ██╔══██╗██╔══██║   ██║   ██║   ██║██╔══██╗
██║     ██║  ██║███████║███████║    ╚██████╔╝███████╗██║ ╚████║███████╗██║  ██║██║  ██║   ██║   ╚██████╔╝██║  ██║
╚═╝     ╚═╝  ╚═╝╚══════╝╚══════╝     ╚═════╝ ╚══════╝╚═╝  ╚═══╝╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝   ╚═╝    ╚═════╝ ╚═╝  ╚═╝
    '''
    with open("osinys_password.txt", "a") as file:
        file.write("=======Osinys=======\n\n")
        file.write(f"[+] PASSWORD : {password}\n")
        file.write(f"[+] Password Force: {force}\n")
        file.write(f"\n-------------------\n\n")
        file.write(f"{ascii_art}\n")

def main():
    ascii_art = '''
██████╗  █████╗ ███████╗███████╗     ██████╗ ███████╗███╗   ██╗███████╗██████╗  █████╗ ████████╗ ██████╗ ██████╗ 
██╔══██╗██╔══██╗██╔════╝██╔════╝    ██╔════╝ ██╔════╝████╗  ██║██╔════╝██╔══██╗██╔══██╗╚══██╔══╝██╔═══██╗██╔══██╗
██████╔╝███████║███████╗███████╗    ██║  ███╗█████╗  ██╔██╗ ██║█████╗  ██████╔╝███████║   ██║   ██║   ██║██████╔╝
██╔═══╝ ██╔══██║╚════██║╚════██║    ██║   ██║██╔══╝  ██║╚██╗██║██╔══╝  ██╔══██╗██╔══██║   ██║   ██║   ██║██╔══██╗
██║     ██║  ██║███████║███████║    ╚██████╔╝███████╗██║ ╚████║███████╗██║  ██║██║  ██║   ██║   ╚██████╔╝██║  ██║
╚═╝     ╚═╝  ╚═╝╚══════╝╚══════╝     ╚═════╝ ╚══════╝╚═╝  ╚═══╝╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝   ╚═╝    ╚═════╝ ╚═╝  ╚═╝
    '''
    print(Colorate.Horizontal(Colors.red_to_purple, ascii_art))

    digits = int(input(Colorate.Horizontal(Colors.red_to_purple, "Enter the number of digits: ")))
    letters = int(input(Colorate.Horizontal(Colors.red_to_purple, "Enter the number of letters: ")))

    password = generate_password(digits, letters)
    force = password_force(len(password))
    
    print(Colorate.Horizontal(Colors.red_to_purple, f"\nGenerated Password: {password}"))
    print(Colorate.Horizontal(Colors.red_to_purple, f"\n[+] Password Force: {force}"))

    save_choice = input(Colorate.Horizontal(Colors.red_to_purple, "\nDo you want to save this password ? (y/n): ")).strip().lower()
    if save_choice == 'y':
        save_password(password, force)
        print(Colorate.Horizontal(Colors.red_to_purple, "[+] Password saved in 'generated_pass.txt'"))
    else:
        print(Colorate.Horizontal(Colors.red_to_purple, "[!] Password not saved."))

if __name__ == "__main__":
    main()
