def dummy(*args, **kwargs):
    pass


def print_verbose(message):
    print(f"[*] {message}")


def print_vulnerable(name, uri=""):
    # TODO not found and not vulnerable
    print(f"  [+] {name} is vulnerable")
    if uri:
        print(f"  {uri}")


def print_not_vulnerable(name):
    # TODO not found and not vulnerable
    print(f"  [!] {name} is not vulnerable")


def print_found(message):
    print(f"  [i] {message}")


def print_not_found(message, uri=""):
    print(f"  [-] {message} not found")
    if uri:
        print(f"  {uri}")


def help_banner(program):
    print(f"{program} <target> [--verbose / --silent]")


def program_banner():
    print("      ___      ___               ")
    print(" __ _| _ )_  _/ __| __ __ _ _ _  ")
    print(" \\ V / _ \\ || \\__ \\/ _/ _` | ' \\ ")
    print("  \\_/|___/\\_, |___/\\__\\__,_|_||_|")
    print("          |__/                   \n")
    print("vByScan - vBulletin scanner")
    print("This program is a fork of vbscan\n")
