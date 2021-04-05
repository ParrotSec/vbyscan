# Test compare version

from cores import db_handler

version = "4.1.1"

print("Test compare match range")
db_versions = [
    ("4.1.0-4.1.3", True),
    ("4.1.6-4.1.7", False),
    ("4.0.2-4.3.x", True),
    ("-4.10.7", True),
    ("4.1.0-", True),
    ("3.0.x-5.x", True),
    ("4.1.1-4.5.9", True),
    ("4.0.2-4.1.1", True)
]

for db_version in db_versions:
    print(f" {version}: {db_version[0]}")
    result = db_handler.match_range(version, db_version[0])
    print(f"  Expected: {db_version[1]} | Result: {result}")
    if result != db_version[1]:
        print(f"   Test failed for {db_version[0]}")


db_versions = [
    ("4.1.0<4.1.3", True),
    ("4.1.6<4.1.7", False),
    ("4.0.2<4.3.x", True),
    ("<4.10.7", True),
    ("4.1.0<", True),
    ("3.0.x<5.x", True),
    ("4.1.0<4.1.1", False),
    ("4.1.1<4.1.3", True),
    ("4.1.1<4.5.3|5.7.2<5.9.9", True)
]

for db_version in db_versions:
    print(f" {version}: {db_version[0]}")
    result = db_handler.match_lesser(version, db_version[0])
    print(f"  Expected: {db_version[1]} | Result: {result}")
    if result != db_version[1]:
        print(f"   Test failed for {db_version[0]}")
