def apache_config_checker(req, target, info_cb, found_cb, not_found_cb):
    name = "Apache configurations"
    is_found = False
    list_uri = [
        "server-status",
        "server-enumerate"
    ]

    info_cb(f"Checking {name}")

    for tmp_path in list_uri:
        uri = f"{target}{tmp_path}"
        r = req.get(uri)
        if r.status_code == 200:
            if "Apache Server Information" in str(r.content) or "Server Root" in str(r.content) or \
                    "Apache Status" in str(r.content):
                found_cb("Interesting file is found", uri)
                is_found = True
    if not is_found:
        not_found_cb(name)
