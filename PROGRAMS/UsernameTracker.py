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
from colorama import Fore, Style, init
import time
import sys
import pystyle

init(autoreset=True)

ascii_art = """                           



██╗   ██╗███████╗███████╗██████╗     ████████╗██████╗  █████╗  ██████╗██╗  ██╗███████╗██████╗ 
██║   ██║██╔════╝██╔════╝██╔══██╗    ╚══██╔══╝██╔══██╗██╔══██╗██╔════╝██║ ██╔╝██╔════╝██╔══██╗
██║   ██║███████╗█████╗  ██████╔╝       ██║   ██████╔╝███████║██║     █████╔╝ █████╗  ██████╔╝
██║   ██║╚════██║██╔══╝  ██╔══██╗       ██║   ██╔══██╗██╔══██║██║     ██╔═██╗ ██╔══╝  ██╔══██╗
╚██████╔╝███████║███████╗██║  ██║       ██║   ██║  ██║██║  ██║╚██████╗██║  ██╗███████╗██║  ██║
 ╚═════╝ ╚══════╝╚══════╝╚═╝  ╚═╝       ╚═╝   ╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝
                                                                                              

                                                                                                                                 

"""

print(Fore.RED + ascii_art)

username = input(Fore.RED + "\n[~] Enter USERNAME: ").strip()

urls = [
    f"https://www.facebook.com/{username}",
    f"https://www.instagram.com/{username}",
    f"https://twitter.com/{username}",
    f"https://www.linkedin.com/in/{username}",
    f"https://www.youtube.com/{username}",
    f"https://github.com/{username}",
    f"https://www.reddit.com/user/{username}",
    f"https://www.tiktok.com/@{username}",
    f"https://pinterest.com/{username}",
    f"https://www.snapchat.com/add/{username}",
    f"https://www.tumblr.com/{username}",
    f"https://www.flickr.com/people/{username}",
    f"https://www.quora.com/profile/{username}",
    f"https://www.discordapp.com/users/{username}",
    f"https://twitch.tv/{username}",
    f"https://www.medium.com/@{username}",
    f"https://soundcloud.com/{username}",
    f"https://vimeo.com/{username}",
    f"https://dribbble.com/{username}",
    f"https://www.behance.net/{username}",
    f"https://about.me/{username}",
    f"https://www.deviantart.com/{username}",
    f"https://www.last.fm/user/{username}",
    f"https://keybase.io/{username}",
    f"https://www.gitlab.com/{username}",
    f"https://bitbucket.org/{username}",
    f"https://www.kaggle.com/{username}",
    f"https://500px.com/{username}",
    f"https://www.badoo.com/en/{username}",
    f"https://www.weheartit.com/{username}",
    f"https://www.producthunt.com/@{username}",
    f"https://www.ello.co/{username}",
    f"https://www.clubhouse.com/@{username}",
    f"https://www.yelp.com/user_details?userid={username}",
    f"https://www.rumble.com/{username}",
    f"https://www.dailymotion.com/{username}",
    f"https://www.slideshare.net/{username}",
    f"https://www.scribd.com/{username}",
    f"https://www.bandcamp.com/{username}",
    f"https://www.artstation.com/{username}",
    f"https://www.furaffinity.net/user/{username}",
    f"https://www.myspace.com/{username}",
    f"https://www.patreon.com/{username}",
    f"https://www.ko-fi.com/{username}",
    f"https://www.buymeacoffee.com/{username}",
    f"https://www.onlyfans.com/{username}",
    f"https://www.gofundme.com/{username}",
    f"https://www.change.org/u/{username}",
    f"https://www.tripadvisor.com/Profile/{username}",
    f"https://www.trustpilot.com/users/{username}",
    f"https://www.vk.com/{username}",
    f"https://www.ok.ru/profile/{username}",
    f"https://www.meetup.com/members/{username}",
    f"https://www.tinder.com/@{username}",
    f"https://www.bumble.com/en/{username}",
    f"https://www.zoosk.com/{username}",
    f"https://www.chess.com/member/{username}",
    f"https://www.strava.com/athletes/{username}",
    f"https://www.nike.com/membership/{username}",
    f"https://www.adidas.com/us/{username}",
    f"https://www.polar.com/{username}",
    f"https://www.fitbit.com/user/{username}",
    f"https://www.openstreetmap.org/user/{username}",
    f"https://www.deezer.com/profile/{username}",
    f"https://www.applemusic.com/{username}",
    f"https://www.spotify.com/user/{username}",
    f"https://www.mastodon.social/@{username}",
    f"https://www.google.com/search?q={username}",
    
]

def check_link(link):
    try:
        response = requests.get(link, timeout=5)
        return response.status_code == 200
    except requests.RequestException:
        return False

def loading_bar(current, total, duration=3, size=30):
    progress = (current / total) * 100
    filled = "█" * int((progress / 100) * size)
    empty = "-" * (size - len(filled))
    sys.stdout.write(f"\r[{pystyle.Colors.red}{filled}{pystyle.Colors.white}{empty}] {int(progress)}%")
    sys.stdout.flush() 

def username_tracker():
    found_accounts = []
    not_found_accounts = []

    total_urls = len(urls)

    for index, link in enumerate(urls):
        loading_bar(index + 1, total_urls)  

        if check_link(link):
            found_accounts.append(link)
        else:
            not_found_accounts.append(link)

    print(Fore.CYAN + "\n[ Accounts found ]")
    for account in found_accounts:
        print(Fore.GREEN + f"[+] FOUND : {account}")

    print(Fore.CYAN + "\n[ Accounts not found ]")
    for account in not_found_accounts:
        print(Fore.RED + f"[-] NOT FOUND : {account}")

    save_results = input(Fore.YELLOW + "\nDo you want to save the results to a file? (y/n): ").strip().lower()
    if save_results == 'y':
        with open("osinys_tracker.txt", "w") as file:
            file.write("[ Accounts found ]\n")
            for account in found_accounts:
                file.write(f"[+] FOUND : {account}\n")
            file.write("\n[ Accounts not found ]\n")
            for account in not_found_accounts:
                file.write(f"[-] NOT FOUND : {account}\n")
        print(Fore.GREEN + "[!] Results saved in 'osinys_tracker.txt'")

if __name__ == '__main__':
    username_tracker()

input(Fore.YELLOW + "\nPress Enter to quit")
