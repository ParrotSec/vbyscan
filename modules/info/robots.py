
def robot_check(req, target, info_cb, not_found_cb):
    name = r'robots.txt existing'
    info_cb(name)

    uri = target + "/robots.txt"
    r = req.get(uri)

    try:
        if r.status_code == 200 and r'text/plain' in r.headers["Content-Type"]:
            for line in str(r.content).split("\n"):
                sub_path = line.split(": /")
                if len(sub_path) == 2 and "Disallow" == sub_path[0]:
                    branch = sub_path[1].replace("\n", "").replace("\r", "")
                    new_uri = f"{target}{branch}"
                    sr = req.get(new_uri)
                    # TODO custom color here
                    if sr.status_code == 404:
                        pass
                    if sr.status_code < 300:
                        print(uri)
                    elif sr.status_code < 400:
                        print(uri)
                    elif sr.status_code < 500:
                        print(uri)
                    else:
                        print(uri)
        else:
            not_found_cb(name)
    except:
        not_found_cb(name)
