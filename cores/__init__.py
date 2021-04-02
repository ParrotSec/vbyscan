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
