def get_version():
    return "0.1.1"


def verify_target(target):
    result = target
    if not result.startswith("http"):
        result = "http://" + result
    if not result.endswith("/"):
        result = result + "/"
    return result


def exploit_modules():
    import os
    from modules import exploits
    modules_path = exploits.__path__[0]
    for root, dirs, files in os.walk(modules_path):
        for file in files:
            if not file.startswith("__") and file.endswith(".py"):
                yield file.split(".")[0]


def gen_hash():
    # https://stackoverflow.com/a/2257449
    import string
    import random
    str_gen = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(8))
    import hashlib
    return hashlib.md5(str_gen.encode('utf-8')).hexdigest()


def enum_vuln(version):
    from cores import db_handler
    import json
    import resources
    resources_path = resources.__path__[0]
    with open(resources_path + "/db.json") as vuln_db_file:
        vuln_db = json.load(vuln_db_file)
        for each_vuln in vuln_db['vuln_db']:
            if db_handler.version_match(version, each_vuln['version']):
                print(f"  [*] \033[97m{each_vuln['id']}\033[0m - \033[95m{each_vuln['name']}\033[0m")
                print(f"      \033[94m{each_vuln['link']}\033[0m")
                if each_vuln['exploit']:
                    print(f"      \033[91m{each_vuln['exploit']}\033[0m")
