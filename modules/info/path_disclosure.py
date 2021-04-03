import re


def parse_path(data):
    rg_list = [
        r"array given in (.*?) on line",
        r"occurred in (.*?) on line",
        r"on a non-object in (.*?) [o|i]n line",
        r"No such file or directory (errno 2) in (.*?) on line",
        r"No such file or directory in (.*?) in line",
    ]
    # path = ""
    for rg_text in rg_list:
        try:
            path = re.findall(rg_text, data)[0]
            if path:
                return path
        except:
            pass

    return ""


def path_disclosure(req, target, info_cb, found_cb, not_found_cb):
    name = "vBulletin's Path Disclure"
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
        if "Cannot modify header information" in str(r.content) or "trim()" in str(r.content) or \
                "class_core.php" in str(r.content) or "header already sent" in str(r.content) or \
                "Fatal error" in str(r.content):
            path = parse_path(str(r.content))
            if path:
                found_cb(name, path)
            # if not pathdis == None:
            #     pathdis = re.sub(r'<b>', '', pathdis.group(1), re.I)
            #     pathdis = re.sub(r'</b>', '', pathdis, re.I)
            #     pathdis = re.sub(r'<strong>', '', pathdis, re.I)
            #     pathdis = re.sub(r'</strong>', '', pathdis, re.I)
            #     target = re.sub(r'/$', '', target)
            #     found_cb(f"Full Path Disclosure (FPD) in '{target}/{plink}' : {pathdis}")
            #     is_found = True
            #     break

    if not is_found:
        not_found_cb(name)
