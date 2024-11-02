import os

def navigate_folder(path, indent=0):
    for item in os.listdir(path):
        print("  " * indent + item)
        if os.path.isdir(os.path.join(path, item)):
            navigate_folder(os.path.join(path, item), indent + 1)

navigate_folder('/dev-core-102')