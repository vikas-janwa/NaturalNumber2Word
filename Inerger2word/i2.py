def interger2word(value=''):
    # Input handling
    if value:
        number = int(value)
    else:
        number = input("Please enter a number: ")
        number = int(number)

    # Create a dictionary for numbers to words
    number_words = {
        0: "", 1: "One", 2: "Two", 3: "Three", 4: "Four", 5: "Five", 6: "Six", 
        7: "Seven", 8: "Eight", 9: "Nine", 10: "Ten", 11: "Eleven", 12: "Twelve", 
        13: "Thirteen", 14: "Fourteen", 15: "Fifteen", 16: "Sixteen", 17: "Seventeen", 
        18: "Eighteen", 19: "Nineteen", 20: "Twenty", 30: "Thirty", 40: "Forty", 
        50: "Fifty", 60: "Sixty", 70: "Seventy", 80: "Eighty", 90: "Ninety", 
        100: "Hundred", 1000: "Thousand", 1000000: "Million", 1000000000: "Billion"
    }
    
    # Helper function for two-digit numbers
    def twodigit(digit):
        if digit <= 20:
            return number_words[digit]
        else:
            ones = digit % 10
            tens = digit - ones
            return f"{number_words[tens]} {number_words[ones]}" if ones != 0 else number_words[tens]
    
    length = len(str(number))  # Get the length of the number (1 to 3 digits)

    if length == 1:
        # Single digit
        return print(number_words[number])
    
    elif length == 2:
        # Two digits (10 - 99)
        return print(twodigit(number))
    
    elif length == 3:
        # Three digits (100 - 999)
        hundreds = number // 100  # Get the hundreds place
        remainder = number % 100  # Get the remaining two digits
        
        # For numbers like 100, 200, etc., we need to handle the case where remainder is 0
        if remainder == 0:
            return print(f"{number_words[hundreds]} Hundred")
        else:
            # For numbers like 356, 452, we add the remainder part
            return print(f"{number_words[hundreds]} Hundred and {twodigit(remainder)}")

# Test the function
interger2word(178)  # This should print "Three Hundred and Fifty Six"
interger2word(105)  # This should print "One Hundred and Five"
interger2word(50)   # This should print "Fifty"
