def run(req, target, info_cb, found_cb, not_found_cb):
    # https://github.com/OWASP/vbscan/blob/master/modules/validator.pl
    name = "validator.php information disclosure"
    uri = f"{target}validator.php"
    is_vulnerable = False

    info_cb(f"Checking {name}")
    r = req.get(uri)

    if r.status_code == 200 and "validate" in r.text:
        found_cb(name, uri)
        is_vulnerable = True

    if not is_vulnerable:
        not_found_cb(name)
