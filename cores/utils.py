

def dummy(*args, **kwargs):
    pass


def print_verbose(message):
    print(f"[*] {message}")


def print_vuln(name, uri= ""):
    # TODO not found and not vulnerable
    print(f"  [+] {name} is vulnerable")
    if uri:
        print(f"  {uri}")


def print_not_vuln(name):
    # TODO not found and not vulnerable
    print(f"  [-] {name} is not vulnerable")


def print_found(message):
    print(f" [^] {message}")


def print_not_found(message, uri = ""):
    print(f" [!] {message} not found")
    if uri:
        print(f"  {uri}")
