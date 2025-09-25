# Assignment: Discount Calculator

def calculate_discount(price, discount_percent):
    """
    Calculate the final price after applying a discount.
    
    Args:
        price: Original price of the item
        discount_percent: Discount percentage (e.g., 20 for 20%)
    
    Returns:
        Final price after discount (if discount >= 20%), otherwise original price
    """
    if discount_percent >= 20:
        # Calculate discount amount and subtract from original price
        discount_amount = price * (discount_percent / 100)
        final_price = price - discount_amount
        return final_price
    else:
        # Return original price if discount is less than 20%
        return price


# Part 2: Get user input and use the function
try:
    # Prompt user for original price
    original_price = float(input("Enter the original price of the item: $"))
    
    # Prompt user for discount percentage
    discount_percentage = float(input("Enter the discount percentage: "))
    
    # Calculate final price using the function
    final_price = calculate_discount(original_price, discount_percentage)
    
    # Display results
    if discount_percentage >= 20:
        savings = original_price - final_price
        print(f"\nDiscount applied! ({discount_percentage}%)")
        print(f"Original price: ${original_price:.2f}")
        print(f"You saved: ${savings:.2f}")
        print(f"Final price: ${final_price:.2f}")
    else:
        print(f"\nNo discount applied (discount must be 20% or higher)")
        print(f"Final price: ${final_price:.2f}")

except ValueError:
    print("Please enter valid numbers for price and discount percentage.")