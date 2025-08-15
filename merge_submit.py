import json
from pprint import pprint
import shutil

with open("golf.json", "r") as file:
    golf = json.load(file)

if not golf:
    print("smh no solutions")
    exit(1)


golf_min = {}

for folder, data in golf.items():
    for task, size in data.items():
        if task not in golf_min or golf_min[task][1] > size:
            golf_min[task] = [folder, size]

with open("golf_min.json", "r") as file:
    golf_min_old = json.load(file)
    if golf_min_old == golf_min:
        print("smh no better solutions")

        exit(1)


with open("golf_min.json", "w") as file:
    json.dump(golf_min, file, indent=4)

byte_count = 0
sol_count = 0
score_count = 0
size_list = []
folder_dict = {}

for task, data in golf_min.items():
    folder, size = data
    byte_count += size
    sol_count += 1
    score_count += max(0, 2500 - size)
    if folder not in folder_dict:
        folder_dict[folder] = 0
    folder_dict[folder] += 1

    shutil.copyfile(f"{folder}/task{task}.py", f"submission/task{task}.py") 

with open("sheet.txt", "w") as file:
    for task in range(1,401):
        task = f"{task:03}"
        if task in golf_min:
            size_list.append(str(golf_min[task][1]))
        else:
            size_list.append("")

    file.write("\n".join(size_list))

shutil.make_archive("submission", "zip", "submission")

print(f"score: {score_count}")
print(f"solution count: {sol_count}")
print(f"total bytes: {byte_count}")

if sol_count != 0:
    print(f"average bytes: {byte_count / sol_count:.2f}")

for k, v in sorted(folder_dict.items(), key = lambda x: -x[1]):
    print(f"{k}: {v}")