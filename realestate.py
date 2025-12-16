#Kevin Lashley
#Professor Chloe Gerhardson
#Python 115
#12-15-2025

# (Loops) and(Functions)
def getFloatInput(prompt_text):
    """
    Prompts the user for a float value using a loop and error handling.
    Ensures the value is numeric, non-zero, and positive.
    """
    while True:
        try:
            # Input function 
            user_input = input(prompt_text)
            # float() conversion 
            value = float(user_input)

            # Data validation using conditional logic 
            if value <= 0:
                print("Error: The value must be a positive, non-zero number.")
                continue  # Jumps back to the start of the while loop
            else:
                # Return statement 
                return value

        # Error handling using try/except 
        # Catches cases where float() conversion fails
        except ValueError:
            print("Error: Invalid input. Please enter a numeric value.")
            # The loop continues automatically after the except block

#  (Functions) and  (Lists)
def getMedian(data_list):
    """
    Calculates the median of a list of numbers without using statistics module.
    Assumes the input list is already sorted.
    """
    # len() function 
    n = len(data_list)

    if n == 0:
        return 0.0 # Handle empty list case 

    # Conditional logic to check if the length is odd or even
    if n % 2 == 1:
        # Odd number of entries: the median is the middle entry.
        # Integer division // 
        middle_index = n // 2
        median_value = data_list[middle_index] # List indexing 
    else:
        # Even number of entries: average the two middle entries.
        mid_right_index = n // 2
        mid_left_index = mid_right_index - 1
        
        median_value = (data_list[mid_left_index] + data_list[mid_right_index]) / 2.0
    
    return float(median_value) # Return a float 


# Main function 
def main():
    # List initialization 
    sales_values = []
    
    # Outer loop for user input repetition
    while True:
        # Call the input function defined in step 1
        fSalesPrice = getFloatInput("Enter property sales value: ")
        
        # Append value to list 
        sales_values.append(fSalesPrice)
        
        # Inner loop for validating Y/N prompt
        while True:
            # input() function 
            user_choice = input("Enter another value Y or N: ")
            
            # String methods .upper()  and conditional logic 
            if user_choice.upper() == 'N':
                repeat_input = False
                break # Exit the inner Y/N validation loop
            elif user_choice.upper() == 'Y':
                repeat_input = True
                break # Exit the inner Y/N validation loop
            else:
                print("Error: Please enter Y or N.")
                # Loop continues until valid Y/N is entered

        # Exit the outer loop if the user chose 'N'
        if not repeat_input:
            break

    # Check data before processing 
    if not sales_values:
        print("No sales data entered. Exiting program.")
        return

    # Sort the list 
    sales_values.sort()

    # Data processing using built-in functions (min, max, sum)
    min_value = min(sales_values)
    max_value = max(sales_values)
    total_value = sum(sales_values)
    average_value = total_value / len(sales_values)
    
    # Call the median function defined in step 2 
    median_value = getMedian(sales_values)
    
    # Calculation for commission 
    commission = total_value * 0.03

    # Output Section 
    print("\n--- Sales Report ---")
    
    # Loop through the sorted list to print each entry 
    print("Entered Sales Values (Sorted):")
    for value in sales_values:
        # Format as currency with 2 decimal places
        print(f"${value:,.2f}") 
        
    print("-" * 20) # Simple separator using string multiplication 
    
    # Outputting summary statistics formatted as currency
    # f-strings for formatting 
    print(f"Minimum Value:   ${min_value:,.2f}")
    print(f"Maximum Value:   ${max_value:,.2f}")
    print(f"Total Value:     ${total_value:,.2f}")
    print(f"Average Value:   ${average_value:,.2f}")
    print(f"Median Value:    ${median_value:,.2f}")
    print(f"Commission (3%): ${commission:,.2f}")
    print("--------------------")

# Call the main function to start the program 
if __name__ == "__main__":
    main()
