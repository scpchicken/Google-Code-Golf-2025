import json
from pprint import pprint
import shutil

with open("golf.json", "r") as file:
    golf = json.load(file)


golf_min = {}

for folder, data in golf.items():
    for task, size in data.items():
        if task not in golf_min or golf_min[task][1] > size:
            golf_min[task] = (folder, size)


byte_count = 0
sol_count = 0
score_count = 0
size_list = []

for task, data in golf_min.items():
    folder, size = data
    byte_count += size
    sol_count += 1
    score_count += max(0, 2500 - size)

    shutil.copyfile(f"{folder}/task{task}.py", f"submission/task{task}.py") 

with open("sheet.txt", "w") as file:
    for task in range(1,401):
        task = f"{task:03}"
        if task in golf_min:
            size_list.append(str(golf_min[task][1]))
        else:
            size_list.append("")

    file.write("\n".join(size_list))

print(f"score: {score_count}")
print(f"solution count: {sol_count}")
print(f"total bytes: {byte_count}")

if sol_count != 0:
    print(f"average bytes: {byte_count / sol_count:.2f}")