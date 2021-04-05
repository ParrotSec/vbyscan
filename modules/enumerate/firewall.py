def firewall_detector(req, target, info_cb, found_cb, not_found_cb):
    name = "vBulletin's default firewall"
    is_found = False

    info_cb(f"Checking {name}")

    r = req.get(target)

    if r.status_code == 200:
        if "dnp_firewall" in r.text or "DnP Firewall" in r.text or \
                "dnp_fw" in r.text:
            found_cb("Firewall is detected")
            is_found = True
    # TODO bypass with agent https://github.com/OWASP/vbscan/blob/master/modules/firewall.pl
    if not is_found:
        not_found_cb(name)
