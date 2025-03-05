import webbrowser
from colorama import init, Fore

init(autoreset=True)


ascii_art = '''
██╗      ██████╗  ██████╗  ██████╗ ███████╗██████╗ 
██║     ██╔═══██╗██╔════╝ ██╔════╝ ██╔════╝██╔══██╗
██║     ██║   ██║██║  ███╗██║  ███╗█████╗  ██████╔╝
██║     ██║   ██║██║   ██║██║   ██║██╔══╝  ██╔══██╗
███████╗╚██████╔╝╚██████╔╝╚██████╔╝███████╗██║  ██║
╚══════╝ ╚═════╝  ╚═════╝  ╚═════╝ ╚══════╝╚═╝  ╚═╝
'''

def show_menu():
   
    print(Fore.RED + ascii_art)


    print(Fore.RED + "[1] IP Logger")
    print(Fore.RED + "[2] Grabify")

def open_link(choice):
    if choice == "1":
     
        webbrowser.open("https://iplogger.org/")
        print(Fore.RED + "[+] Opening IP Logger...")
    elif choice == "2":
        
        webbrowser.open("https://grabify.link/")
        print(Fore.RED + "[+] Opening Grabify...")
    else:
        print(Fore.RED + "[!] Invalid choice, please select 1 or 2.")

def main():
    show_menu()
    
    
    choice = input(Fore.RED + "\nChoose an option [1/2]: ")
    open_link(choice)

if __name__ == "__main__":
    main()
