from cores.utils import *
import requests


def fingerprint(client, target, version, verbose_cb, found_cb, not_found_cb):
    # FIXME firewall is so slow
    # from modules.enumerate import firewall
    # firewall.firewall_detector(client, target, verbose_cb, found_cb, not_found_cb)

    from modules.enumerate import robots
    robots.robot_check(client, target, verbose_cb, found_cb, not_found_cb)

    from modules.enumerate import validator
    validator.run(client, target, verbose_cb, found_cb, not_found_cb)

    from modules.enumerate import misconfig
    misconfig.apache_config_checker(client, target, verbose_cb, found_cb, not_found_cb)

    from modules.enumerate import finder
    finder.license_finder(client, target, verbose_cb, found_cb, not_found_cb)
    finder.admin_finder(client, target, verbose_cb, found_cb, not_found_cb)
    finder.moderator_finder(client, target, verbose_cb, found_cb, not_found_cb)

    finder.config_finder(client, target, version, verbose_cb, found_cb, not_found_cb)

    from modules.enumerate import dir_listing
    dir_listing.check_dir_listing(client, target, verbose_cb, found_cb, not_found_cb)

    from modules.enumerate import path_disclosure
    path_disclosure.path_disclosure(client, target, verbose_cb, found_cb, not_found_cb)

    finder.error_finder(client, target, verbose_cb, found_cb, not_found_cb)
    finder.backup_finder(client, target, verbose_cb, found_cb, not_found_cb)


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

    try:
        from modules.enumerate import version
        vb_version = version.get_version(client, target, verbose_cb, info_found_cb, info_not_found_cb)
        if not vb_version:
            if not verbose:
                print_not_found("vBulletin version")
            while True:
                user_choice = input("  Do you want to continue? [Y/n] ")
                if user_choice == "y" or user_choice == "Y":
                    break
                elif user_choice == "n" or user_choice == "N":
                    return
                else:
                    print(f"  Unknown choice \"{user_choice}\". Please select 'Y' or 'N'.")
    except Exception as error:
        print("  Error while checking target's version")
        print(error)
        return

    print("\nTarget enumeration\n")
    fingerprint(client, target, vb_version, verbose_cb, info_found_cb, info_not_found_cb)

    if vb_version:
        import cores
        print("\nEnumerate vulnerabilities from version")
        cores.enum_vuln(vb_version)

    print("\nVulnerability scan\n")
    vulnerability_scan(client, target, verbose_cb, vulnerability_cb, not_vulnerability_cb)

    print("")
    print_verbose("Completed")
