
def robot_check(req, target, info_cb, found_cb, not_found_cb):
    name = "robots.txt"
    info_cb(f"Checking {name}")

    uri = f"{target}robots.txt"
    r = req.get(uri)

    try:
        if r.status_code == 200 and "text/plain" in r.headers["Content-Type"]:
            found_cb(name, uri)
            for line in r.text.split("\n"):
                if line.startswith("Disallow:"):
                    branch = line.split(": /")[1].replace("\r", "").replace("\n", "")
                    new_uri = f"{target}{branch}"
                    sr = req.get(new_uri)
                    if sr.status_code == 404:
                        pass
                    if sr.status_code < 300:
                        # Bright green
                        print(f"  \033[94m{new_uri} \033[92m{sr.status_code}\033[00m")
                    elif sr.status_code < 400:
                        # Bright white
                        print(f"  \033[94m{new_uri} \033[97m{sr.status_code}\033[00m")
                    elif sr.status_code < 500:
                        # Bright red
                        print(f"  \033[94m{new_uri} \033[91m{sr.status_code}\033[00m")
                    else:
                        # Bright cyan
                        print(f"  \033[94m{new_uri} \033[96m{sr.status_code}\033[00m")
        else:
            not_found_cb(name)
    except Exception as error:
        print(error)
        not_found_cb(name)
