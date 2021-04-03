
# https://github.com/OWASP/vbscan/blob/master/modules/passlogger.pl

def passLogger(req, target, info_cb, found_cb, not_found_cb):
    name = 'vBulletin password logger Detecting'
    info_cb('Checking' + name)

    content = req.get(f'{target}/').content.decode()
    if r'vb_login_md5password_utf, )' in content.lower() or r'vb_login_md5password_utf,)' in content.lower():
        found_cb("This website has been password logger and store user's password as cleartext")
    else:
        not_found_cb("Password logger not found")