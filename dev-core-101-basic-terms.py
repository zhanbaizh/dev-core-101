print('What is your age?')
n = int(input())
def is_mushel(x):
    if (x % 12) == 0:
        return True
    else:
        return False
print(is_mushel(n))