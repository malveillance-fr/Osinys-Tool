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


input("\nENTER FOR QUIT")