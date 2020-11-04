import os

path = "/home/danny/Downloads"
files = list(filter(lambda x: x.endswith(".jpg"), os.listdir(path)))
print(files)
