def dummy(*args, **kwargs):
    pass


def print_verbose(message):
    print(f"[+] {message}")


def print_vulnerable(name, uri=""):
    # Bright Magenta
    print(f"  [\033[96m*\033[0m] \033[95m{name}\033[0m is\033[91m vulnerable\033[0m")
    if uri:
        # Bright Cyan
        print(f"  \033[96m{uri}\033[0m")


def print_not_vulnerable(name):
    # Bright yellow
    print(f"  [\033[93m!\033[0m] \033[93m{name}\033[0m is\033[37m not vulnerable\033[0m")


def print_found(message, uri=""):
    # Bright white
    print(f"  [\033[97m*\033[0m] \033[97m{message}\033[0m")
    if uri:
        # Bright blue
        print(f"  \033[94m{uri}\033[0m")


def print_not_found(message):
    print(f"  [\033[91m-\033[0m] {message} not found")


def help_banner(program):
    print(f"{program} <target> [--verbose / --silent]")


def program_banner():
    import cores
    print("      ___      ___               ")
    print(" __ _| _ )_  _/ __| __ __ _ _ _  ")
    print(" \\ V / _ \\ || \\__ \\/ _/ _` | ' \\ ")
    print("  \\_/|___/\\_, |___/\\__\\__,_|_||_|")
    print("          |__/                   \n")
    print("-----[ \033[95mvBulletin Scanner\033[0m ]---[ ParrotOS Team ]")
    print(f"-----[ Version: \033[97m{cores.get_version()}\033[0m ]")
    print("-----[ Author: \033[96mNông Hoàng Tú\033[0m ]---[ \033[94mdmknght@parrotsec.org\033[0m ]")
    print("-----[ License: \033[93mGPL-3\033[0m ]")
    print("-----[ \033[94mhttps://nest.parrotsec.org/packages/tools/vbyscan/\033[0m ]")
    print("This program is a fork of OWASP_VBScan in python3\n")
