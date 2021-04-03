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
