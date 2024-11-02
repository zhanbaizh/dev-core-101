import os

def print_directory_structure(path, indent=0):
    for item in os.listdir(path):
        item_path = os.path.join(path, item)
        print("  " * indent + item)
        if os.path.isdir(item_path):
            print_directory_structure(item_path, indent + 1)

def search_file(directory, filename):
    for item in os.listdir(directory):
        if item == filename:
            return os.path.join(directory, item)
        if os.path.isdir(os.path.join(directory, item)):
            result = search_file(os.path.join(directory, item), filename)
            if result:
                return result
    return None

def calculate_total_size(directory):
    total_size = 0
    for item in os.listdir(directory):
        path = os.path.join(directory, item)
        if os.path.isfile(path):
            total_size += os.path.getsize(path)
        elif os.path.isdir(path):
            total_size += calculate_total_size(path)
    return total_size

print_directory_structure('/Users/zhandosbaizhuma/documents/GitHub')
search_file('/Users/zhandosbaizhuma/documents/GitHub', 'root')
calculate_total_size('/Users/zhandosbaizhuma/documents/GitHub')