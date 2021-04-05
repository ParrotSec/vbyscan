
def cmp_min_ver(version, db_version):
    for v_sub, db_sub in zip(version.split("."), db_version.split(".")):
        if db_sub == "x":
            return True
        elif "rc" not in db_sub and "rc" not in v_sub:
            if int(v_sub) > int(db_sub):
                return True
            elif int(v_sub) < int(db_sub):
                return False

    return True


def cmp_max_ver(version, db_version):
    # Return code:
    # -1: version > db_version
    # 0: version < db_version
    # >=1: version = db_version
    for v_sub, db_sub in zip(version.split("."), db_version.split(".")):
        if db_sub == "x":
            return 0
        elif "rc" not in db_sub and "rc" not in v_sub:
            if int(v_sub) < int(db_sub):
                return 0
            elif int(v_sub) > int(db_sub):
                return -1
            else:
                pass
    return 1


def match_lesser(version, db_version):
    min_ver, max_ver = db_version.split("<")
    if not min_ver:
        # Match lesser -> <. We only accept 0
        if cmp_max_ver(version, max_ver) == 0:
            return True
        else:
            return False
    elif not max_ver:
        return cmp_min_ver(version, min_ver)
    else:
        if cmp_min_ver(version, min_ver) and cmp_max_ver(version, max_ver) == 0:
            return True
        else:
            return False


def match_range(version, db_version):
    min_ver, max_ver = db_version.split("-")
    if not min_ver:
        # Match range -> <=. We only exclude >
        if cmp_max_ver(version, max_ver) == -1:
            return False
        else:
            return True
    elif not max_ver:
        return cmp_min_ver(version, min_ver)
    else:
        if cmp_min_ver(version, min_ver) and cmp_max_ver(version, max_ver) != -1:
            return True
        else:
            return False


def compare_version(version, db_version):
    """
    Match version with unknown version from db
    Version format: x.y.z
    But db could contains version like "4.1.x"
    :param version: string that has version format
    :param db_version: string that has version format
    :return:
    """
    if "x" not in db_version:
        return version == db_version
    else:
        if version.count(".") != db_version.count("."):
            return False
        else:
            for v_sub, db_sub in zip(version.split("."), db_version.split(".")):
                if db_sub == "x":
                    return True
                if v_sub != db_sub:
                    return False


def version_match(version, db_versions):
    for db_version in db_versions.split("|"):
        if "<" in db_version:
            match_lesser(version, db_version)
        elif "-" in db_version:
            match_range(version, db_version)
        else:
            # Compare version
            return compare_version(version, db_version)
