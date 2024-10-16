from datetime import datetime #imported library to track time

#function to calculate discount
def apply_basic_discount(price, basic_discount): 
    return price * (1-basic_discount/100)

#function to calculate additional discount
def apply_loyalty_discount(price, loyalty_discount):
    return price*loyalty_discount/100

#function to calculate tax
def apply_tax(price, tax_rate):
    return price*tax_rate/100

#function to calculate wildcard tax
def apply_wildcard_tax():
    return 0

#function to add new customer    
def add_new_customer(list,name):
    list.append(name)

custumer_base = ['Zhandos', 'Adilet', 'Serik'] #the list of customers
customer_name = input('Enter the constumer name:') #it accepts customer name


if customer_name in custumer_base:
    print('This customer already exists', customer_name) #here it checks if customer exists
else:
    print('This is a new custumer, print "yes" if you want to add him?') #it offers to add customer to the base
    decision = input('do you want to add him "yes/no"') #it asks yes or no
    if decision == 'yes':
        add_new_customer(custumer_base, customer_name)
    else:
        print('You have decided to not to add this one')

#input values of cost, discount, additional discount, tax rate
cost = int(input('enter the price:'))
discount = int(input('Enter basic discount in percent:'))
additional_discount = int(input('Enter loyalty discount in percent:'))
tax_rate = int(input('Enter tax rate in percent'))

#check if customer exists
if customer_name in custumer_base:
    print('Total price for this customer:', apply_basic_discount(cost, discount)-apply_loyalty_discount(cost, additional_discount))
else:    
    print('Total price', apply_basic_discount(cost, discount))

#how to check date and time
current_time = datetime.now().minute
discount_minutes = [12, 14]
if current_time in discount_minutes:
    print('It is wild tax time: no tax', apply_wildcard_tax(cost))
else: 
    print('You will be charged:', apply_tax(cost,tax_rate))





