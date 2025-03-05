import webbrowser
from colorama import Fore, init

init(autoreset=True)

print(Fore.RED + '''
█████╗ ██████╗ ██████╗ ███████╗███████╗███████╗    ████████╗ ██████╗  ██████╗ ██╗     
██╔══██╗██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝    ╚══██╔══╝██╔═══██╗██╔═══██╗██║     
███████║██║  ██║██████╔╝█████╗  ███████╗███████╗       ██║   ██║   ██║██║   ██║██║     
██╔══██║██║  ██║██╔══██╗██╔══╝  ╚════██║╚════██║       ██║   ██║   ██║██║   ██║██║     
██║  ██║██████╔╝██║  ██║███████╗███████║███████║       ██║   ╚██████╔╝╚██████╔╝███████╗
╚═╝  ╚═╝╚═════╝ ╚═╝  ╚═╝╚══════╝╚══════╝╚══════╝       ╚═╝    ╚═════╝  ╚═════╝ ╚══════╝
''')

first_name = input(Fore.GREEN + "Enter first name: ")
last_name = input(Fore.GREEN + "Enter last name: ")

search_urls = [
    f"https://www.pagesjaunes.fr/pagesblanches/recherche?quoiqui={first_name}+{last_name}",
    f"https://www.tumblr.com/search/{first_name}%20{last_name}",
    f"https://www.peekyou.com/{first_name}-{last_name}",
    f"https://www.118000.fr/search?who={first_name}+{last_name}"
]

open_result = input(Fore.YELLOW + "\nOpen result ? (y/n): ").lower()

if open_result == 'y':
    print(Fore.YELLOW + "\nSearching for results...")

    for url in search_urls:
        print(Fore.CYAN + f"Opening: {url}")
        webbrowser.open(url)

    print(Fore.GREEN + "\nSearch complete! Check the opened tabs for results.")
else:
    input(Fore.RED + "\nPress enter to quit...")
