import os  # works with system
directory = "dir"
lst = os.listdir(directory)
for fl in lst:
    if not fl.endswith(".txt"):
        continue
    f = open(directory + os.sep + fl, "r", encoding="utf-8")  # find file in right dir
    c = f.read()
    f.close()

for root, dirs, files in os.walk(directory):
    for fl in files:
        f = open(root + os.sep + fl)
        ...
        f.close()

import shutil
shutil.copyfile(src, dst)

#разобрать текст, создать несколько мал. файлы, дерево каталогов: каждая папка часть/акт, каждый файл глава/явления