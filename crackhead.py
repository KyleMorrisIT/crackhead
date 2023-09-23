import subprocess
import glob
from colorama import init, Fore, Style

# Initialize colorama
init()

# ANSI escape codes for text colors
GREEN = Fore.GREEN
BLUE = Fore.BLUE
RED = Fore.RED
YELLOW = Fore.YELLOW
RESET = Style.RESET_ALL

# Banner text
banner = f"""
{Fore.GREEN}
             .-"--\"\"\"\".__`.
            |            `    |
            `._....------.._.:
             .()''        ``().
             () .=='  `===  `-.
             (  (X      X)
              )     /        J
              |.   /      . (
              (.  (_'.   , )|`
              |\\`-....--'/  ' \\
               \\\\ | | | /  /   \.
                \\`-===-'  '     \o.
                 `. --   / (     OObaaaad888b.
             .a888b`.__.'d\\     OO888888888888a.
             .8888888aaaa88POOOOOO888888888888888.
             .888888888888888888888888888888888888b
          .d88888P88888888888888888888888b8888888.
         .d88888P8888888888888888a:f888888|888888b
          888888|8888888888888888888888888\8888888

                     | |  | |                  | |
   ___ _ __ __ _  ___| | _| |__   ___  __ _  __| |
  / __| '__/ _` |/ __| |/ / '_ \\ / _ \\/ _` |/ _` |
 | (__| | | (_| | (__|   <| | | |  __/ (_| | (_| |
  \\___|_|  \\__,_|\\___|_|\\_\\_| |_|\\___|\\__,_|\\__,_|
            (THE DEFAULT CRACKER)            v1.5
{Style.RESET_ALL}
"""

# Get the list of .hc22000 files in the current directory
hc22000_files = glob.glob("*.hc22000")

if not hc22000_files:
    print(f"{YELLOW}No .hc22000 files found in the current directory.{RESET}")
    exit(1)

# Display the available .hc22000 files
print(f"{BLUE}Available .hc22000 files:{RESET}")
for i, file in enumerate(hc22000_files, start=1):
    print(f'{i}. {file}')

# Select a .hc22000 file
while True:
    try:
        choice = int(input(f"Please select a .hc22000 file (1 to {len(hc22000_files)}): "))
        if 1 <= choice <= len(hc22000_files):
            selected_file = hc22000_files[choice - 1]
            break
        else:
            print(f"{RED}Invalid choice. Please enter a valid number.{RESET}")
    except ValueError:
        print(f"{RED}Please enter a valid number.{RESET}")

# Define hashcat commands
hashcat_commands = {
    "2WIREXXX": '?d?d?d?d?d?d?d?d?d?d',
    "AOLBB-XXXXXX": '?H?H?H?H?H?H?H?H',
    "belkin.xxx": '?h?h?h?h?h?h?h?h',
    "belkin.xxxx": '?h?h?h?h?h?h?h?h',
    "Belkin.XXXX": '?H?H?H?H?H?H?H?H',
    "Belkin_XXXXXX": '?H?H?H?H?H?H?H?H',
    "BELL###": '?H?H?H?H?H?H?H?H',
    "BELL####": '?H?H?H?H?H?H?H?H?H?H',
    "BigPondXXXXXX": '?H?H?H?H?H?H?H?H?H?H',
    "BTHomeHub-XXXX": '?h?h?h?h?h?h?h?h?h?h',
    "BTHomeHub2-XXXX": '?h?h?h?h?h?h?h?h?h?h',
    "BTHub3": '?h?h?h?h?h?h?h?h?h?h',
    "BTHub4": '?h?h?h?h?h?h?h?h?h?h',
    "BTHub5": '?h?h?h?h?h?h?h?h?h?h',
    "CenturyLinkXXXX": '?h?h?h?h?h?h?h?h?h?h?h?h?h',
    "DJAWEB_#####": '?d?d?d?d?d?d?d?d?d?d',
    "Domino-XXXX": '?H?H?H?H?H?H?H?H',
    "EasyBox-######": '?H?H?H?H?H?H?H?H?H',
    "E583x-xxxx": '?d?d?d?d?d?d?d?d',
    "E583x-xxxxx": '?H?H?H?H?H?H?H?H',
    "INFINITUM####": '?d?d?d?d?d?d?d?d?d?d',
    "MobileWifi-xxxx": '?d?d?d?d?d?d?d?d',
    "Netia-XXXXXX": '?h?h?h?h?h?h?h?h?h?h?h?h?h',
    "ONOXXXX": '?d?d?d?d?d?d?d?d?d?d',
    "Orange-XXXX": '?H?H?H?H?H?H?H?H',
    "PlusnetWireless-XXXXXX": '?H?H?H?H?H?H?H?H?H?H',
    "SKYXXXXX": '?u?u?u?u?u?u?u?u',
    "TALKTALK-XXXXXX": '?H?H?H?H?H?H?H?H',
    "Tech_XXXXXXXX": '?u?u?u?u?u?u?u?u',
    "TelstraXXXXXX": '?H?H?H?H?H?H?H?H?H?H',
    "ThomsonXXXXXX": '?h?h?h?h?h?h?h?h?h?h',
    "TNCAPXXXXXX": '?H?H?H?H?H?H?H?H?H?H',
    "TP-LINK_######": '?H?H?H?H?H?H?H?H',
    "TDC-####": '?h?h?h?h?h?h?h?h?h',
    "TIM_PN51T_XXXX": '?d?d?d?d?d?d?d?d',
    "UNITE-XXXX": '?d?d?d?d?d?d?d?d',
    "UPCXXXXXXX": '?u?u?u?u?u?u?u?u',
    "Verizon MIFIXXXX XXXX": '?d?d?d?d?d?d?d?d?d?d?d',
    "Virgin Media": '?l?l?l?l?l?l?l?l',
    "VirginMobile MiFiXXXX XXX": '?d?d?d?d?d?d?d?d?d?d?d',
    "VMXXXXXXX-2G": '?l?l?l?l?l?l?l?l',
    "VMXXXXXXX-5G": '?l?l?l?l?l?l?l?l',
    "WLAN1-XXXXXX": '?H?H?H?H?H?H?H?H?H?H?H',
}

# Commands that use dictionaries
special_command = f"hashcat -a 6 -m 22000 {selected_file} /usr/share/dict/NETGEARXX.txt ?d?d?d"

# Display the banner
print(banner)

while True:
    try:
        # Display options menu and get input
        print(f"{BLUE}Please enter your choice:{RESET}")
        print(f"Options:")
        for i, opt in enumerate(hashcat_commands.keys(), start=1):
            print(f'{i}. {YELLOW}{opt}{RESET}')
        print(f'{len(hashcat_commands) + 1}. Dictionary Combo: {YELLOW}NETGEARXX{RESET}')
        choice = int(input())

        if choice == len(hashcat_commands) + 1:
            selected_option = special_command
            break
        elif 1 <= choice <= len(hashcat_commands):
            selected_option = list(hashcat_commands.keys())[choice - 1]
            break
        else:
            print(f"{RED}INVALID OPTION{RESET}")
    except ValueError:
        print(f"{RED}Please enter a valid number{RESET}")

# Perform the selected action
if selected_option == special_command:
    subprocess.run(selected_option, shell=True)
else:
    pattern = hashcat_commands[selected_option]
    subprocess.run(['hashcat', '-a', '3', '-m', '22000', selected_file, pattern])
