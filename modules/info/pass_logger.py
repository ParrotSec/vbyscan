
def check_password_logger(req, target, info_cb, found_cb, not_found_cb):
    # https://github.com/OWASP/vbscan/blob/master/modules/passlogger.pl
    name = 'vBulletin password logger'
    info_cb('Checking' + name)

    r = req.get(target)
    if "vb_login_md5password_utf, )" in r.text or "vb_login_md5password_utf,)" in r.text:
        found_cb(name)
    else:
        not_found_cb(name)
