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
