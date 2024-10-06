def sum(a,b): #функция для нахождения сумм
    return a + b
def substration (a,b):
    return a - b #to find substraction
def product(a,b):
    return a*b # to find the product
def divide(a,b):
    return a / b #to find delenie
print('Please define n,m')
n = int(input('Enter first number:'))
m = int(input('Enter second number:'))
print (sum(n,m), substration(n,m), product(n,m), divide(n,m))
