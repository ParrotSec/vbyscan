import re

def pathDisclure(req, target, info_cb, found_cb, not_found_cb):
    name = "vBulletin's Path Disclure"
    info_cb(f"Checking {name}")

    is_found = False

    plinks = ["forumdisplay.php?do[]=[test.dll]",
              "calendar.php?do[]=[test.dll]",
              "search.php?do[]=[test.dll]",
              "forumrunner/include/album.php",
              "core/vb5/route/channel.php",
              "core/vb5/route/conversation.php",
              "includes/api/interface/noncollapsed.php",
              "includes/api/interface/collapsed.php",
              "vbseo_sitemap/addons/vbseo_sm_vba.php",
              "vbseo_sitemap/addons/vbseo_sm_vba_links.php"]
    
    for plink in plinks:
        uri = req.get(target+'/'+plink).content.decode()
        if 'Cannot modify header information' in uri or 'trim()' in uri or 'class_core.php' in uri or 'header already sent' in uri or 'Fatal error' in uri:
            pathdis = re.search(r'array given in (.*?) on line', uri, re.I)
            if pathdis == None:
                pathdis = re.search(r"array given in (.*?) on line", uri, re.I)
            if pathdis == None:
                pathdis = re.search(r"occurred in (.*?) on line", uri, re.I)
            if pathdis == None:
                pathdis = re.search(r"on a non-object in (.*?) on line", uri, re.I)
            if pathdis == None:
                pathdis = re.search(r"on a non-object in (.*?) in line", uri, re.I)
            if pathdis == None:
                pathdis = re.search(r"No such file or directory (errno 2) in (.*?) on line", uri, re.I)
            if pathdis == None:
                pathdis = re.search(r"No such file or directory in (.*?) in line", uri, re.I)

            if not pathdis == None:
                pathdis = re.sub(r'<b>', '', pathdis.group(1), re.I)
                pathdis = re.sub(r'</b>', '', pathdis, re.I)
                pathdis = re.sub(r'<strong>', '', pathdis, re.I)
                pathdis = re.sub(r'</strong>', '', pathdis, re.I)
                target = re.sub(r'/$', '', target)
                found_cb(f"Full Path Disclosure (FPD) in '{target}/{plink}' : {pathdis}")
                is_found = True
                break

    if not is_found:
        not_found_cb(name)