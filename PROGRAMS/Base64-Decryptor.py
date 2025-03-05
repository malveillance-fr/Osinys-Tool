import base64
from colorama import Fore, init

init(autoreset=True)

ascii_art = """


                         ██████╗ ███████╗ ██████╗██████╗ ██╗   ██╗██████╗ ████████╗ ██████╗ ██████╗ 
                         ██╔══██╗██╔════╝██╔════╝██╔══██╗╚██╗ ██╔╝██╔══██╗╚══██╔══╝██╔═══██╗██╔══██╗
                         ██║  ██║█████╗  ██║     ██████╔╝ ╚████╔╝ ██████╔╝   ██║   ██║   ██║██████╔╝
                         ██║  ██║██╔══╝  ██║     ██╔══██╗  ╚██╔╝  ██╔═══╝    ██║   ██║   ██║██╔══██╗
                         ██████╔╝███████╗╚██████╗██║  ██║   ██║   ██║        ██║   ╚██████╔╝██║  ██║
                         ╚═════╝ ╚══════╝ ╚═════╝╚═╝  ╚═╝   ╚═╝   ╚═╝        ╚═╝    ╚═════╝ ╚═╝  ╚═╝
                                                                                                       


"""

print(Fore.RED + ascii_art)

encoded_text = input("Enter the text to decode from base64: ")

try:
    decoded_text = base64.b64decode(encoded_text).decode('utf-8')
    print(f"\nDecoded text: {decoded_text}")
except Exception as e:
    print(f"Error during decoding: {e}")
input("\nEnter for return to menu")