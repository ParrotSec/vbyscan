import re


def parse_path(data):
    rg_list = [
        r"array given in (.*?) on line",
        r"occurred in (.*?) on line",
        r"on a non-object in (.*?) [o|i]n line",
        r"No such file or directory (errno 2) in (.*?) on line",
        r"No such file or directory in (.*?) in line",
    ]

    for rg_text in rg_list:
        try:
            path = re.findall(rg_text, data)[0]
            if path:
                return path
        except:
            pass

    return ""


def path_disclosure(req, target, info_cb, found_cb, not_found_cb):
    name = "vBulletin's path disclosure"
    info_cb(f"Checking {name}")

    is_found = False

    plinks = [
        "forumdisplay.php?do[]=[test.dll]",
        "calendar.php?do[]=[test.dll]",
        "search.php?do[]=[test.dll]",
        "forumrunner/include/album.php",
        "core/vb5/route/channel.php",
        "core/vb5/route/conversation.php",
        "includes/api/interface/noncollapsed.php",
        "includes/api/interface/collapsed.php",
        "vbseo_sitemap/addons/vbseo_sm_vba.php",
        "vbseo_sitemap/addons/vbseo_sm_vba_links.php"
    ]
    
    for plink in plinks:
        r = req.get(target + plink)
        if "Cannot modify header information" in r.text or "trim()" in r.text or \
                "class_core.php" in r.text or "header already sent" in r.text or \
                "Fatal error" in r.text:
            path = parse_path(r.text)
            if path:
                tags = [
                    "<b>",
                    "</b>",
                    "<strong>",
                    "</strong>",
                ]
                for tag in tags:
                    if tag in path:
                        path = path.replace(tag, "")
                found_cb(name, path)
                return

    if not is_found:
        not_found_cb(name)
