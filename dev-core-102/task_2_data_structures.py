def add_member(member_list, name):
    member_list.append(name)

def remove_member(member_list, name):
    if name in member_list:
        member_list.remove(name)
    else:
        print(f"{name} is not in the list")

base = []
add_member(base, input('enter the name   '))

print(*base, sep=' ')