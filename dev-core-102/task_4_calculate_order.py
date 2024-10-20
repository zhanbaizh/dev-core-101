from datetime import datetime

def loyalty_program_member(clients_list, client_name, order_cost):
    if client_name in clients_list and order_cost >= 1000:
        return order_cost*0.85
    elif client_name in clients_list:
        return order_cost*0.9
    elif order_cost >= 1000:
        return order_cost*0.95
    else:
        return order_cost
    
def calculate_tax(price):
    return price*0.05

current_time = datetime.now().minute
clients = ["Zhandos", "Andrey", "Madina"]

client_name = input("Please enter the client name:  ")
order_price = int(input('Enter the price  '))
total_price = loyalty_program_member(clients,client_name,order_price)

if current_time % 2 != 0:
    tax = calculate_tax(order_price)
else:
    tax = 0
print(f"The final price is {total_price}, tax is {tax}")