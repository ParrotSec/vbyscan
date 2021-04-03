def dummy(*args, **kwargs):
    pass


def print_verbose(message):
    print(f"[+] {message}")


def print_vulnerable(name, uri=""):
    # Bright Magenta
    print(f"  [\033[96m*\033[00m] \033[95m{name}\033[00m is\033[91m vulnerable\033[00m")
    if uri:
        # Bright Cyan
        print(f"  \033[96m{uri}\033[0m")


def print_not_vulnerable(name):
    # Bright yellow
    print(f"  [\033[93m!\033[00m] \033[93m{name}\033[00m is\033[37m not vulnerable\033[00m")


def print_found(message, uri=""):
    # Bright green
    print(f"  [\033[97m*\033[00m] \033[92m{message}\033[00m")
    if uri:
        # Bright blue
        print(f"  \033[94m{uri}\033[00m")


def print_not_found(message):
    print(f"  [\033[91m-\033[00m] {message} not found")


def help_banner(program):
    print(f"{program} <target> [--verbose / --silent]")


def program_banner():
    print("      ___      ___               ")
    print(" __ _| _ )_  _/ __| __ __ _ _ _  ")
    print(" \\ V / _ \\ || \\__ \\/ _/ _` | ' \\ ")
    print("  \\_/|___/\\_, |___/\\__\\__,_|_||_|")
    print("          |__/                   \n")
    print("vByScan - vBulletin scanner of Parrot OS")
    print("This program is a fork of vbscan\n")
