from cores.utils import *
import requests


def fingerprint(client, target, verbose_cb, found_cb, not_found_cb):
    from modules.info import version
    version.get_version(client, target, verbose_cb, found_cb, not_found_cb)
    # FIXME firewall is so slow
    # from modules.info import firewall
    # firewall.firewall_detector(client, target, verbose_cb, found_cb, not_found_cb)
    # TODO check robots.txt
    from modules.info import validator
    validator.run(client, target, verbose_cb, found_cb, not_found_cb)

    from modules.info import misconfig
    misconfig.apache_config_checkder(client, target, verbose_cb, found_cb, not_found_cb)

    from modules.info import finder
    finder.cp_finder(client, target, verbose_cb, found_cb, not_found_cb)
    # TODO: check backup and log
    finder.error_finder(client, target, verbose_cb, found_cb, not_found_cb)
    # TODO check config
    # finder.config_finder(client, target, verbose_cb, found_cb, not_found_cb)
    finder.backup_finder(client, target, verbose_cb, found_cb, not_found_cb)


def vuln_scan(client, target, verbose_cb, found_cb, not_found_cb):
    import cores
    import importlib
    for module_name in cores.exploit_modules():
        module = importlib.import_module("modules.exploits." + module_name)
        try:
            import traceback
            module.run(client, target, verbose_cb, found_cb, not_found_cb)
        except Exception as error:
            print("Runtime error")
            traceback.print_exc()


def main_logic(target, verbose=True):
    is_verbose = verbose
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
