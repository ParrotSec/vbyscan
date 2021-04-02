from cores.utils import *
import requests


def fingerprint(client, target, verbose_cb, found_cb, not_found_cb):
    from modules.info import version
    from modules.info import firewall
    version.get_version(client, target, verbose_cb, found_cb, not_found_cb)
    firewall.firewall_detector(client, target, verbose_cb, found_cb, not_found_cb)


def vuln_scan(client, target, verbose_cb, found_cb, not_found_cb):
    import cores
    import importlib
    for module_name in cores.exploit_modules():
        module = importlib.import_module("modules.exploits." + module_name)
        try:
            module.run(client, target, verbose_cb, found_cb, not_found_cb)
        except Exception as error:
            print("Runtime error: " + error)


def main_logic(target):
    is_verbose = True
    vuln_cb = print_vuln
    info_found_cb = print_found
    info_not_found_cb = print_not_found
    if is_verbose:
        verbose_cb = print_verbose
        not_vuln_cb = print_not_vuln
    else:
        verbose_cb = dummy
        not_vuln_cb = dummy
    client = requests.Session()
    client.headers.update({'User-agent': 'Mozilla/5.0'})
    fingerprint(client, target, verbose_cb, info_found_cb, info_not_found_cb)
    vuln_scan(client, target, verbose_cb, vuln_cb, not_vuln_cb)
