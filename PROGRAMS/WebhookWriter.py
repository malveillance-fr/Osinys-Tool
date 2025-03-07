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








import requests
from pystyle import Colorate, Colors
import os


os.system('mode con: cols=120 lines=30')

def send_webhook(webhook_url, message):
    
    payload = {
        "content": message
    }
    
    try:
        response = requests.post(webhook_url, json=payload)
        if response.status_code == 204:
            print(Colorate.Horizontal(Colors.red_to_purple, "[+] Message sent successfully"))
        else:
            print(Colorate.Horizontal(Colors.red_to_purple, f"[!] Failed to send message. Status code: {response.status_code}"))
    except Exception as e:
        print(Colorate.Horizontal(Colors.red_to_purple, f"[!] Error: {str(e)}"))


def main():
    
    ascii_art = '''
██╗    ██╗██████╗ ██╗████████╗███████╗██████╗ 
██║    ██║██╔══██╗██║╚══██╔══╝██╔════╝██╔══██╗
██║ █╗ ██║██████╔╝██║   ██║   █████╗  ██████╔╝
██║███╗██║██╔══██╗██║   ██║   ██╔══╝  ██╔══██╗
╚███╔███╔╝██║  ██║██║   ██║   ███████╗██║  ██║
 ╚══╝╚══╝ ╚═╝  ╚═╝╚═╝   ╚═╝   ╚══════╝╚═╝  ╚═╝
'''
    print(Colorate.Horizontal(Colors.red_to_purple, ascii_art))

  
    webhook_url = input(Colorate.Horizontal(Colors.red_to_purple, "\nEnter Webhook URL: ")).strip()

    
    message = input(Colorate.Horizontal(Colors.red_to_purple, "\nEnter message to send: ")).strip()


    send_webhook(webhook_url, message)



if __name__ == "__main__":
    main()



