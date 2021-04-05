import re


def get_version(req, target, info_cb, found_cb, not_found_cb):
    def parse_version(data):
        regex = r"([vV][bB]ulletin [\d.]+ .*)\n"
        try:
            result = re.findall(regex, data)[0]
            if result:
                return result
        except:
            return ""

    name = "Enumerate Vbulletin version"
    is_found = False
    list_files = [
        "clientscript/vbulletin_menu.js",
        "clientscript/vbulletin_global.js",
        "clientscript/vbulletin-core.js",
        "",
    ]

    info_cb(name)

    for file_name in list_files:
        uri = f"{target}{file_name}"
        r = req.get(uri)
        if r.status_code == 200:
            if uri == target:
                # <meta name="generator" content="vBulletin 3.7.1" />, line 10
                # cmp_data = r.text
                cmp_data = "\n".join(r.text.split("\n")[0:15])
            else:
                # Likely the code gets version from banner only. We try cut the data to very short text
                cmp_data = "\n".join(r.text.split("\n")[0:5])
            version = parse_version(cmp_data)
            if version:
                found_cb(version)
                return version.split(" ")[1]
        # TODO handle powered by https://github.com/OWASP/vbscan/blob/master/core/ver.pl#L47

    if not is_found:
        not_found_cb(name)
        return ""
