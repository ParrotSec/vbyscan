"""
Contains:
    1. Backup finder
    2. c99 finder
    3. config finder
    4. cp finder
    5. Error logs finder
"""


def backup_finder(req, target, info_cb, found_cb, not_found_cb):
    # https://github.com/OWASP/vbscan/blob/master/modules/backupfinder.pl
    name = "Backup files"
    is_found = False
    list_backups = [
        "1.zip",
        "2.zip",
        "admincp.zip",
        "backup.sql",
        "backup.tar.gz",
        "backup.zip",
        "database.sql",
        "database.zip",
        "files.zip",
        "forum.tar",
        "forum.tar.gz",
        "forum.zip",
        "forums.zip",
        "includes.zip",
        "sql.zip",
        "upload.zip",
        "vb.zip"
    ]

    info_cb(f"Checking {name}")

    for file_name in list_backups:
        uri = f"{target}{file_name}"
        try:
            r = req.get(uri)
            if r.status_code == 200 and not r.headers['Content-Type'].startwith("text/html"):
                found_cb(f"Found {name}", uri)
                is_found = True
        except:
            pass
    if not is_found:
        not_found_cb(name)


def config_finder(req, target, version, info_cb, found_cb, not_found_cb):
    # https://github.com/OWASP/vbscan/blob/master/modules/configfinder.pl
    name = "Config files"
    is_found = False
    list_config = [
        "config.php~",
        "config.php.new",
        "config.php.new~",
        "config.php.old",
        "config.php.old~",
        "config.bak",
        "config.php.bak",
        "config.php.bkp",
        "config.txt",
        "config.php.txt",
        "config - Copy.php",
        "config.php.swo",
        "config.php_bak",
        "config.php#",
        "config.orig",
        "config.php.save",
        "config.php.original",
        "config.php.swp",
        "config.save",
        ".config.php.swp",
        "config.php1",
        "config.php2",
        "config.php3",
        "config.php4",
        "config.php4",
        "config.php6",
        "config.php7",
        "config.phtml"
    ]

    info_cb(f"Finding {name}")

    if version.startswith("5"):
        include = "core/includes/"
    else:
        include = "includes/"

    for file_name in list_config:
        uri = f"{target}{include}{file_name}"
        r = req.get(uri)
        if r.status_code == 200 and ("admincpdir" in r.text or "dbtype" in r.text or "technicalemail" in r.text):
            found_cb(f"Found {name}", uri)
            is_found = True

    if not is_found:
        not_found_cb(name)


def admin_finder(req, target, info_cb, found_cb, not_found_cb):
    # https://github.com/OWASP/vbscan/blob/master/modules/cpfinder.pl
    # https://github.com/OWASP/vbscan/blob/master/modules/cpupgrade.pl
    name = "Admin's Control Panel"
    uri = f"{target}admincp/index.php"
    is_admin_found = False

    info_cb(f"Finding {name}")
    r = req.get(uri)

    if r.status_code == 200 and "Admin Control Panel" in r.text or \
            "form action=\"../login.php?do=login" in r.text or "ADMINHASH" in r.text:
        found_cb(f"Found {name}", uri)
        is_admin_found = True
    else:
        not_found_cb(f"Using upgrade.php technique. {name}")

        uri = f"{target}install/upgrade.php"
        r = req.get(uri)

        if r.status_code == 200:
            if "ADMINDIR = \"" in r.text:
                def parse_admin_dir(data):
                    import re
                    regex = r"ADMINDIR = \"\.\.\/(.*?)\"\;"
                    try:
                        result = re.findall(regex, data)[0]
                        if result:
                            return result
                    except:
                        return ""
                admin_url = parse_admin_dir(r.text)
                found_cb(f"Found {name}", admin_url)
                is_admin_found = True

    if not is_admin_found:
        not_found_cb(name)


def moderator_finder(req, target, info_cb, found_cb, not_found_cb):
    name = "Moderator's Control Panel"
    uri = f"{target}modcp/index.php"

    info_cb(f"Finding {name}")
    r = req.get(uri)

    if r.status_code == 200 and "Moderator Control Panel" in r.text or \
            "form action=\"../login.php?do=login" in r.text or "ADMINHASH" in r.text:
        found_cb(f"Found {name}", uri)
    else:
        not_found_cb(name)


def error_finder(req, target, info_cb, found_cb, not_found_cb):
    # https://github.com/OWASP/vbscan/blob/master/modules/errfinder.pl
    name = "Error logs"
    is_found = False
    list_err_logs = [
        "error.log",
        "error_log",
        "php-scripts.log",
        "php.errors",
        "php5-fpm.log",
        "php_errors.log",
        "debug.log",
    ]

    info_cb(f"Finding {name}")

    for file_name in list_err_logs:
        uri = f"{target}{file_name}"

        try:
            r = req.get(uri)
            if r.status_code == 200 and not r.headers['Content-Type'].startwith("text/html"):
                found_cb(f"Found {name}", uri)
                is_found = True
        except:
            pass

    if not is_found:
        not_found_cb(name)


def license_finder(req, target, info_cb, found_cb, not_found_cb):
    # https://github.com/OWASP/vbscan/blob/master/modules/license.pl
    name = "License"
    is_found = False
    uri = f"{target}LICENSE"

    info_cb(f"Finding {name}")

    try:
        r = req.get(uri)
        if r.status_code == 200 and "text" in r.headers['Content-Type'] and "vBulletin License Agreement" in r.text:
            found_cb(f"Found {name}", uri)
            is_found = True
    except:
        pass
    if not is_found:
        not_found_cb(name)
