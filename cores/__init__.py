def verify_target(target):
    if not target.startswith("http"):
        target = "http://" + target
    if not target.endswith("/"):
        target = target + "/"
        return target


def exploit_modules():
    import os
    from modules import exploits
    modules_path = exploits.__path__[0]
    for root, dirs, files in os.walk(modules_path):
        for file in files:
            if not file.startswith("__") and file.endswith(".py"):
                yield file.split(".")[0]
