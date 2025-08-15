import json
import sys
from pprint import pprint
import shutil
import os.path
import os
import re

check = list(range(1,401))

ALL = False
FOLDER = "submission"
delete = 0

if len(sys.argv) == 1:
    ALL = True

elif len(sys.argv) == 2:
    if sys.argv[1].isnumeric():
        check = [int(sys.argv[1])]
    else:
        ALL = True
        FOLDER = sys.argv[1]

elif len(sys.argv) == 3:
    FOLDER = sys.argv[1]
    check = [int(sys.argv[2])]

else:
    print("enter nothing or enter a folder and/or number")
    exit(1)

ORIG_CHECK_COUNT = len(check)
if ALL:
    check = []
    for i in range(1,401):
        if os.path.isfile(f"{FOLDER}/task{i:03}.py"):
            check.append(i)

if not len(check):
    exit(2)

delete_list = []
for checker in check:
    with open(f"{FOLDER}/task{checker:03}.py") as file:
        if re.search(r"""\s*def\s+p\(g\):\s*return\s+g\s*""",file.read()):
            delete_list.append(checker)

if delete_list:
    print(end = "DED FILE ")
    for delete in delete_list:
        os.remove(f"{FOLDER}/task{delete:03}.py")
        check.remove(delete)
        delete += 1        
        print(end=f"{delete} ")

    print()

print("starting to check")
delete_list = []

for checker in check:
    with open(f"google-code-golf-2025/task{checker:03}.json","r") as file:
        data = json.load(file)
    sub = __import__(f"{FOLDER}.task{checker:03}")

    data_string = ["train", "test", "arc-gen"]
    for data_str in data_string:
        for dicter in data[data_str]:
            res = eval(f'sub.task{checker:03}.p(dicter["input"])')
            if res != dicter["output"]:
                print(f"TASK {checker:03} | {data_str.upper().replace('-',' ')} DATA FAILED")
                # pprint(dicter["input"])
                # print()
                # print("-----EXPECTED-----")
                # pprint(dicter["output"])
                # print()
                # print("-----ACTUAL-----")
                # pprint(res)
                delete_list.append(checker)
                break
        else:
            continue
        break

for delete in delete_list:
    check.remove(delete)

print(f"yay {len(check)}/{ORIG_CHECK_COUNT} passed")
print(f"{delete} empty")
print(f"{len(delete_list)} failed")
print(*delete_list)

exit(0)