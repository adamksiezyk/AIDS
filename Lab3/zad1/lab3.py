import glob
import os
import shutil

files = glob.glob("./zadanie1/*")
names = []
for path in files:
    names.append(path[11:])

for name in names:
    try:
        os.mkdir('./output/'+name[0])
    except OSError:
        pass
    shutil.copy('./zadanie1/'+name, './output/'+name[0]+'/')



