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
    misconfig.apache_config_checker(client, target, verbose_cb, found_cb, not_found_cb)

    from modules.info import finder
    finder.license_finder(client, target, verbose_cb, found_cb, not_found_cb)
    finder.admin_finder(client, target, verbose_cb, found_cb, not_found_cb)
    finder.moderator_finder(client, target, verbose_cb, found_cb, not_found_cb)

    # TODO: check backup and log
    finder.error_finder(client, target, verbose_cb, found_cb, not_found_cb)
    # TODO check config
    # finder.config_finder(client, target, verbose_cb, found_cb, not_found_cb)
    finder.backup_finder(client, target, verbose_cb, found_cb, not_found_cb)
    from modules.info import path_disclosure
    path_disclosure.path_disclosure(client, target, verbose_cb, found_cb, not_found_cb)


def vulnerability_scan(client, target, verbose_cb, found_cb, not_found_cb):
    import cores
    import importlib
    for module_name in cores.exploit_modules():
        module = importlib.import_module("modules.exploits." + module_name)
        try:
            module.run(client, target, verbose_cb, found_cb, not_found_cb)
        except Exception as error:
            print("Runtime error: " + str(error))


def main_logic(target, verbose=True):
    is_verbose = verbose
    vulnerability_cb = print_vulnerable
    info_found_cb = print_found
    if is_verbose:
        verbose_cb = print_verbose
        not_vulnerability_cb = print_not_vulnerable
        info_not_found_cb = print_not_found
    else:
        verbose_cb = dummy
        not_vulnerability_cb = dummy
        info_not_found_cb = dummy
    client = requests.Session()
    client.headers.update({'User-agent': 'Mozilla/5.0'})
    print("Target enumeration\n")
    fingerprint(client, target, verbose_cb, info_found_cb, info_not_found_cb)

    print("\nVulnerability scan\n")
    vulnerability_scan(client, target, verbose_cb, vulnerability_cb, not_vulnerability_cb)

    print("")
    print_verbose("Completed")
