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
    name = "Find backup files"
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
        r = req.get(uri)
        if r.status_code == 200 and not r.headers['Content-Type'].startwith("text/html"):
            found_cb("Found backup file: " + uri)
            is_found = True
    if not is_found:
        not_found_cb(name)


def config_finder(req, target, info_cb, found_cb, not_found_cb):
    # TODO need to check original code again
    # https://github.com/OWASP/vbscan/blob/master/modules/configfinder.pl
    name = "Find config files"
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

    info_cb(f"Checking {name}")

    for file_name in list_config:
        uri = f"{target}{file_name}"
        r = req.get(uri)
        if r.status_code == 200:
            found_cb("Found config file: " + uri)
            is_found = True

    if not is_found:
        not_found_cb(name)
    """
    $source=$ua->get("$target/$incl/$config")->decoded_content;
    if($source =~ m/admincpdir/i || $source =~ m/dbtype/i || $source =~ m/technicalemail/i){
        $cnftmp="$cnftmp\Readable config file is found \n config file path : $target/$incl/$config\n";
        $ctf=1;
    """


def cp_finder(req, target, info_cb, found_cb, not_found_cb):
    # https://github.com/OWASP/vbscan/blob/master/modules/cpfinder.pl
    # https://github.com/OWASP/vbscan/blob/master/modules/cpupgrade.pl
    name = "Admin Control Panel finder"
    uri = f"{target}admincp/index.php"
    is_admin_found = False

    info_cb(name)
    r = req.get(uri)

    if r.status_code == 200 and "Admin Control Panel" in str(r.content) or \
            "form action=\"../login.php?do=login" in str(r.content) or "ADMINHASH" in str(r.content):
        found_cb("Admin panel found: " + uri)
        is_admin_found = True
    else:
        not_found_cb(name)

    name = "Moderator Control Panel finder"
    uri = f"{target}modcp/index.php"

    info_cb(name)
    r = req.get(uri)

    if r.status_code == 200 and "Moderator Control Panel" in str(r.content) or \
            "form action=\"../login.php?do=login" in str(r.content) or "ADMINHASH" in str(r.content):
        found_cb("Moderator panel found: " + uri)
    else:
        not_found_cb(name)

    if not is_admin_found:
        name = "Find Admin Control Panel using upgrade.php"
        uri = f"{format}install/upgrade.php"

        info_cb(name)
        r = req.get(uri)

        if r.status_code == 200:
            # Original source uses regex /ADMINDIR = \"\.\.\/(.*?)\"\;/
            if "ADMINDIR = \"" in str(r.content):
                found_cb("Admin panel found: " + uri)
                is_admin_found = True

    if not is_admin_found:
        not_found_cb(name)


def error_finder(req, target, info_cb, found_cb, not_found_cb):
    # https://github.com/OWASP/vbscan/blob/master/modules/errfinder.pl
    name = "Find error logs"
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

    info_cb(f"Checking {name}")

    for file_name in list_err_logs:
        uri = f"{target}{file_name}"
        r = req.get(uri)
        if r.status_code == 200 and not r.headers['Content-Type'].startwith("text/html"):
            found_cb("Found config file: " + uri)
            is_found = True

    if not is_found:
        not_found_cb(name)
