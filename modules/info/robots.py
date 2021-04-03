
def robot_check(req, target, info_cb, not_found_cb):
    name = "robots.txt check"
    info_cb(name)

    uri = target + "/robots.txt"
    r = req.get(uri)

    try:
        if r.status_code == 200 and "text/plain" in r.headers["Content-Type"]:
            for line in r.content.decode('utf-8').split("\n"):
                if line.startswith("Disallow:"):
                    branch = line.split(": /")[1]
                    new_uri = f"{target}{branch}"
                    sr = req.get(new_uri)
                    # TODO custom color here
                    if sr.status_code == 404:
                        pass
                    if sr.status_code < 300:
                        print(f"  {new_uri} {sr.status_code}")
                    elif sr.status_code < 400:
                        print(f"  {new_uri} {sr.status_code}")
                    elif sr.status_code < 500:
                        print(f"  {new_uri} {sr.status_code}")
                    else:
                        print(f"  {new_uri} {sr.status_code}")
        else:
            not_found_cb(name)
    except Exception as error:
        print(error)
        not_found_cb(name)
