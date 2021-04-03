def match_lesser(version, db_version):
    pass


def match_range(version, db_version):
    pass


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
        if "<" in db_versions:
            match_lesser(version, db_version)
        elif "-" in db_version:
            match_range(version, db_version)
        else:
            # Compare version
            return compare_version(version, db_version)
