import re

def robot_check(req, target, info_cb, found_cb, not_found_cb):
    name = r'robots.txt existing'
    info_cb(name)

    uri = target + "/robots.txt"
    respond = req.get(uri)

    header = respond.headers
    content = respond.content.decode()
    respond.close()

    if respond.ok and r'text/plain' in header:
        lines = content.split('\n')
        probots = ''
        for line in lines:
            if 'llow:' in line:
                between = re.search(r'.*: (.*)',line).group(1)
                probots = f'{target}{between}\n'

        found_cb(f'robots.txt is found\n'
                 f'Path : {target}/robots.txt \n\n'
                 f'Interesting path found from robots.txt\n{probot}')
    else:
        not_found_cb(name)
