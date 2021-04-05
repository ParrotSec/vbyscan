def check_dir_listing(req, target, info_cb, found_cb, not_found_cb):
    name = "attachment dir listing"
    is_found = False
    uri = f"{target}attachment/"

    info_cb(f"Checking {name}")

    r = req.get(uri)

    if r.status_code == 200 and ("<title>Index of" in r.text or "Last modified</a>" in r.text):
        found_cb(name, uri)
        is_found = True
    if not is_found:
        not_found_cb(name)
