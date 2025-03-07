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








import os
import requests
import time
import threading
from colorama import init, Fore, Style
from datetime import datetime

init(autoreset=True)

def display_ascii():
    ascii_art = """


██╗    ██╗███████╗██████╗ ██╗  ██╗ ██████╗  ██████╗ ██╗  ██╗    ███████╗██████╗  █████╗ ███╗   ███╗███╗   ███╗███████╗██████╗ 
██║    ██║██╔════╝██╔══██╗██║  ██║██╔═══██╗██╔═══██╗██║ ██╔╝    ██╔════╝██╔══██╗██╔══██╗████╗ ████║████╗ ████║██╔════╝██╔══██╗
██║ █╗ ██║█████╗  ██████╔╝███████║██║   ██║██║   ██║█████╔╝     ███████╗██████╔╝███████║██╔████╔██║██╔████╔██║█████╗  ██████╔╝
██║███╗██║██╔══╝  ██╔══██╗██╔══██║██║   ██║██║   ██║██╔═██╗     ╚════██║██╔═══╝ ██╔══██║██║╚██╔╝██║██║╚██╔╝██║██╔══╝  ██╔══██╗
╚███╔███╔╝███████╗██████╔╝██║  ██║╚██████╔╝╚██████╔╝██║  ██╗    ███████║██║     ██║  ██║██║ ╚═╝ ██║██║ ╚═╝ ██║███████╗██║  ██║
 ╚══╝╚══╝ ╚══════╝╚═════╝ ╚═╝  ╚═╝ ╚═════╝  ╚═════╝ ╚═╝  ╚═╝    ╚══════╝╚═╝     ╚═╝  ╚═╝╚═╝     ╚═╝╚═╝     ╚═╝╚══════╝╚═╝  ╚═╝
                                                                                                                              

                           

"""
    print(Fore.RED + ascii_art)

def send_message(webhook_url, webhook_name, message, infinite, count, ping_everyone, delay):
    data = {
        "content": message,
        "username": webhook_name,
    }
    
    if ping_everyone:
        data["allowed_mentions"] = {"parse": ["everyone"]}
    
    if infinite:
        print(Fore.RED + "[INFO] Sending infinitely... Press Enter to stop.")
        while True:
            try:
                response = requests.post(webhook_url, json=data)
                if response.status_code == 200:
                    print(Fore.GREEN + f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] Message sent: {message}")
                elif response.status_code == 429:
                    print(Fore.RED + f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] Rate limit: {message}")
                time.sleep(delay)
            except requests.exceptions.RequestException as e:
                print(Fore.RED + f"[ERROR] {e}")
                break
    else:
        for _ in range(count):
            try:
                response = requests.post(webhook_url, json=data)
                if response.status_code == 200:
                    print(Fore.GREEN + f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] Message sent: {message}")
                elif response.status_code == 429:
                    print(Fore.RED + f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] Rate limit: {message}")
                time.sleep(delay)
            except requests.exceptions.RequestException as e:
                print(Fore.RED + f"[ERROR] {e}")
                break

def start_sending(webhook_url, webhook_name, message, infinite, count, ping_everyone, delay):
    send_message(webhook_url, webhook_name, message, infinite, count, ping_everyone, delay)

def main():
    while True:
        os.system("cls" if os.name == "nt" else "clear")
        
        display_ascii()
        
        print(Fore.RED + "[~] Enter the webhook URL below:")
        webhook_url = input("@root.user > ")
        
        print(Fore.RED + "[~] Enter the webhook name:")
        webhook_name = input("@root.user > ")

        print(Fore.RED + "[INFO] Webhook URL and name accepted!")

        print(Fore.RED + "[~] Enter the message to send (supports Markdown):")
        message = input("@root.user > ")
        
        print(Fore.RED + "[~] Ping everyone (y/n):")
        ping_everyone = input("@root.user > ").strip().lower() == "y"
        
        print(Fore.RED + "[~] Send Infinity? (y/n):")
        infinite = input("@root.user > ").strip().lower() == "y"

        print(Fore.RED + "[~] Delay (seconds) between messages:")
        delay = float(input("@root.user > ").strip())

        if infinite:
            threading.Thread(target=start_sending, args=(webhook_url, webhook_name, message, True, 0, ping_everyone, delay), daemon=True).start()
            input(Fore.RED + "[~] Press Enter to stop infinite sending.")
        else:
            print(Fore.RED + "[~] How many times to send the message?")
            count = int(input("@root.user > ").strip())
            send_message(webhook_url, webhook_name, message, False, count, ping_everyone, delay)

        print(Fore.RED + "[~] Delete Webhook? (y/n):")
        delete = input("@root.user > ").strip().lower()
        if delete == "y":
            try:
                requests.delete(webhook_url)
                print(Fore.GREEN + "[INFO] Webhook deleted successfully.")
            except requests.exceptions.RequestException as e:
                print(Fore.RED + f"[ERROR] Failed to delete webhook: {e}")
        else:
            print(Fore.RED + "[INFO] Webhook not deleted.")

        print(Fore.RED + "[~] Do you want to restart the program? (y/n):")
        restart = input("@root.user > ").strip().lower()
        if restart != "y":
            break

if __name__ == "__main__":
    main()
