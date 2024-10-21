def calculate_discount():
    product_prices = []  

    
    while True:
        user_price = input("Enter the price of the product (or type 'stop' to finish): ")

        if user_price.lower() == 'stop':  # Allow the user to stop entering products
            break

        user_amount = input("Enter the amount of the product: ")

        try:
            price = float(user_price)
            amount = int(user_amount)
            total_price = price * amount  
            product_prices.append(total_price)  
        except ValueError:
            print("Invalid input. Please enter a numeric value for both price and amount.")

 
    discounted_prices = list(map(lambda x: x * 0.9 if x > 100 else x, product_prices))

  
    products_with_discount = list(filter(lambda x: x > 100, product_prices))

   
    total_sum = sum(discounted_prices)

    
    print("\nOriginal total prices of products:", product_prices)
    print("Discounted total prices:", discounted_prices)
    print("Products that received a discount:", products_with_discount)
    print(f"Overall cost with discounts applied: {total_sum:.2f}")


if __name__ == "__main__":
    calculate_discount()
