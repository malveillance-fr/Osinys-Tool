import requests
import colorama
from colorama import Fore, Style
import socket
import datetime

colorama.init()

def get_ip_info(ip):
    url = f"http://ip-api.com/json/{ip}?fields=status,message,country,regionName,city,zip,lat,lon,isp,org,as,mobile,proxy,timezone,continent,query"
    try:
        response = requests.get(url, timeout=5).json()
        return response
    except requests.RequestException:
        return {"status": "fail", "message": "API request failed"}

def get_public_ip():
    try:
        return requests.get("https://api4.ipify.org?format=text", timeout=5).text
    except requests.RequestException:
        return "Unavailable"

def main():
    hostname_of_user = socket.gethostname()
    ip = get_public_ip()

    print(Fore.RED + f"""
  ▄█        ▄██████▄   ▄██████▄     ▄█   ▄█▄          ███      ▄██████▄         ▄▄▄▄███▄▄▄▄      ▄████████    ▄███████▄ 
 ███       ███    ███ ███    ███   ███ ▄███▀      ▀█████████▄ ███    ███      ▄██▀▀▀███▀▀▀██▄   ███    ███   ███    ███ 
 ███       ███    ███ ███    ███   ███▐██▀           ▀███▀▀██ ███    ███      ███   ███   ███   ███    ███   ███    ███ 
 ███       ███    ███ ███    ███  ▄█████▀             ███   ▀ ███    ███      ███   ███   ███   ███    ███   ███    ███ 
 ███       ███    ███ ███    ███ ▀▀█████▄             ███     ███    ███      ███   ███   ███ ▀███████████ ▀█████████▀  
 ███       ███    ███ ███    ███   ███▐██▄            ███     ███    ███      ███   ███   ███   ███    ███   ███        
 ███▌    ▄ ███    ███ ███    ███   ███ ▀███▄          ███     ███    ███      ███   ███   ███   ███    ███   ███        
 █████▄▄██  ▀██████▀   ▀██████▀    ███   ▀█▀         ▄████▀    ▀██████▀        ▀█   ███   █▀    ███    █▀   ▄████▀      
 ▀                                 ▀                                                                                
                            ___________  
                          ,o88~~88888888o,
                        ,~~?8P  88888     8,       | Status : Worked
                       d  d88 d88 d8_88     b      | Logged in as : {hostname_of_user}      
                      d  d888888888          b     | Your IP : {ip}
                      8,?88888888  d8.b o.   8     
                      8~88888888~ ~^8888\\ db 8      DEVLOPPER :
                      ?  888888_         ,888P
                       ?  `8888b,       d888P      | Dev by : Malveillance 
                       `   8888888b_   ,888'       | Discord : 2l0x
                          ~-?8888888  .P-~         | Copyright © 2025, Look2Map. Tous droits réservés.
                               ~~~~~~
    """ + Style.RESET_ALL)

    ip_input = input(Fore.RED + f"root.user@{hostname_of_user} | [+] Enter IP : " + Style.RESET_ALL).strip()
    
    if not ip_input:
        print(Fore.RED + "[-] Error: No IP entered." + Style.RESET_ALL)
        return

    ip_to_lookup = ip_input if ip_input != "public" else get_public_ip()
    
    data = get_ip_info(ip_to_lookup)
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    if data.get("status") != "success":
        print(Fore.RED + f"{timestamp} | [$] Status: INVALID" + Style.RESET_ALL)
        print(Fore.RED + f"{timestamp} | [¤] Reason: {data.get('message', 'Unknown error')}" + Style.RESET_ALL)
        input(Fore.RED + "\n[+] By Malveillance" + Style.RESET_ALL)
        return
    
    print(Fore.RED + f"\n{timestamp} | [$] Status: VALID" + Style.RESET_ALL)
    print(Fore.RED + f"{timestamp} | [¤] Platform: {'Mobile' if data['mobile'] else 'PC'}" + Style.RESET_ALL)
    print(Fore.RED + f"{timestamp} | [¤] City: {data.get('city', 'N/A')}" + Style.RESET_ALL)
    print(Fore.RED + f"{timestamp} | [¤] Region: {data.get('regionName', 'N/A')}" + Style.RESET_ALL)
    print(Fore.RED + f"{timestamp} | [¤] ZipCode: {data.get('zip', 'N/A')}" + Style.RESET_ALL)
    print(Fore.RED + f"{timestamp} | [¤] AS: {data.get('as', 'N/A')}" + Style.RESET_ALL)
    print(Fore.RED + f"{timestamp} | [¤] Organisation: {data.get('org', 'N/A')}" + Style.RESET_ALL)
    print(Fore.RED + f"{timestamp} | [¤] ISP: {data.get('isp', 'N/A')}" + Style.RESET_ALL)
    print(Fore.RED + f"{timestamp} | [¤] Type: {'IPv4' if '.' in data['query'] else 'IPv6'}" + Style.RESET_ALL)
    print(Fore.RED + f"{timestamp} | [¤] Latitude: {data.get('lat', 'N/A')}" + Style.RESET_ALL)
    print(Fore.RED + f"{timestamp} | [¤] Longitude: {data.get('lon', 'N/A')}" + Style.RESET_ALL)
    print(Fore.RED + f"{timestamp} | [¤] Timezone: {data.get('timezone', 'N/A')}" + Style.RESET_ALL)
    print(Fore.RED + f"{timestamp} | [¤] Continent: {data.get('continent', 'N/A')}" + Style.RESET_ALL)
    print(Fore.RED + f"{timestamp} | [¤] Country: {data.get('country', 'N/A')}" + Style.RESET_ALL)
    print(Fore.RED + f"{timestamp} | [$] Query: {data.get('query', 'N/A')}" + Style.RESET_ALL)
    
    input(Fore.RED + "\n[~] By Malveillance" + Style.RESET_ALL)


if __name__ == "__main__":
    main()
