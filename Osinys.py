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








from pystyle import Colorate, Colors
import os
import ctypes


ctypes.windll.kernel32.SetConsoleTitleW("Osinys")
os.system('mode con: cols=120 lines=30')

def run_program(choice):
    
    programs = {
        "D": "Debugger.py",
        "I": "Info.py",
        "01": "TokenChecker.py",
        "02": "NukeCord.py",
        "03": "WebhookSpammer.py",
        "04": "WebhookWriter.py",
        "05": "ID2TOKEN.py",
        "06": "UsernameTracker.py",
        "07": "Look2Map.py",
        "08": "Logger.py",
        "09": "AdressTool.py",
        "10": "GrabberBuilder.py",
        "11": "PasswordGen.py",
        "12": "ExploitSql.py",
        "13": "PasswordTester.py",
        "14": "Base64-Decryptor.py",
        "15": "DonateCenter.py"
    }

    
    program_path = f"PROGRAMS/{programs.get(choice, '')}"
    if os.path.exists(program_path):
        os.system('cls')
        os.system(f"python {program_path}")  
        input(Colorate.Horizontal(Colors.green_to_blue, "Press Enter to return to the menu..."))
    else:
        print(Colorate.Horizontal(Colors.red_to_purple, "[!] Invalid option or missing program."))

def main():
 
   
    menu = '''


                                    
                                                     ▄██████▄     ▄████████  ▄█  ███▄▄▄▄   ▄██   ▄      ▄████████ 
                                                    ███    ███   ███    ███ ███  ███▀▀▀██▄ ███   ██▄   ███    ███ 
                                                    ███    ███   ███    █▀  ███▌ ███   ███ ███▄▄▄███   ███    █▀  
                                                    ███    ███   ███        ███▌ ███   ███ ▀▀▀▀▀▀███   ███        
                                                    ███    ███ ▀███████████ ███▌ ███   ███ ▄██   ███ ▀███████████ 
                                                    ███    ███          ███ ███  ███   ███ ███   ███          ███ 
                                                    ███    ███    ▄█    ███ ███  ███   ███ ███   ███    ▄█    ███ 
                                                     ▀██████▀   ▄████████▀  █▀    ▀█   █▀   ▀█████▀   ▄████████▀  
                                                                                                                        
                                  [D] Debug
                 [I] Info             ┌─────────────────┐                        ┌─────────────┐                     ┌──────────────┐            
                  └─────────┬─────────┤     DISCORD     ├─────────┬──────────────┤ OSINT/CSINT ├──────────────┬──────┤    Others    ├───────────────────┘
                            │         └─────────────────┘         │              └─────────────┘              │      └──────────────┘          │
                            ├─ [01] Token Checker                 ├─ [06] Username Tracker                    ├─ [11] Password Gen             │
                            ├─ [02] Nukecord                      ├─ [07] Look2Map                            ├─ [12] Injection SQL            │
                            ├─ [03] Webhook Spammer               ├─ [08] Logger (IP)                         ├─ [13] Password Tester          │
                            ├─ [04] Webhook Writer                ├─ [09] Adress Tool (with L&F Name)         ├─ [14] Base64 Decryptor         │
                            ├─ [05] ID to Token                   ├─ [10] Grabber Builder                     └─ [15] Donate Center            │
                             ──────────────────────────────────────────────────────────────────────────────────────────────────────────────────                                '''                      
    print(Colorate.Horizontal(Colors.yellow_to_red, menu))

    
    while True:
        choice = input(Colorate.Horizontal(Colors.red_to_purple, "Choice : ")).strip()
        
        
        if choice.lower() == 'exit':
            print("Exiting the program...")
            break
        

        run_program(choice)
        
       
        os.system('cls')
        print(Colorate.Horizontal(Colors.yellow_to_red, menu))
        

if __name__ == "__main__":
    main()
