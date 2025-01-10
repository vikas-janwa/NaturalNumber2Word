def interger2word():
    # number = input("Please enter your name: ")
    # number = int(number)
    number = 80
    # Create a dictionary to hold number-word mappings
    number_words = {}

    # Fill in the numbers 1 to 20
    number_words[0] = ""
    number_words[1] = "One"
    number_words[2] = "Two"
    number_words[3] = "Three"
    number_words[4] = "Four"
    number_words[5] = "Five"
    number_words[6] = "Six"
    number_words[7] = "Seven"
    number_words[8] = "Eight"
    number_words[9] = "Nine"
    number_words[10] = "Ten"
    number_words[11] = "Eleven"
    number_words[12] = "Twelve"
    number_words[13] = "Thirteen"
    number_words[14] = "Fourteen"
    number_words[15] = "Fifteen"
    number_words[16] = "Sixteen"
    number_words[17] = "Seventeen"
    number_words[18] = "Eighteen"
    number_words[19] = "Nineteen"
    number_words[20] = "Twenty"

    # Fill in multiples of ten from 30 to 100
   
    number_words[30] = "Thirty"
    number_words[40] = "Forty"
    number_words[50] = "Fifty"
    number_words[60] = "Sixty"
    number_words[70] = "Seventy"
    number_words[80] = "Eighty"
    number_words[90] = "Ninety"
       

    # Add 1000 and higher
    number_words[1000] = "Thousand"
    number_words[1000000] = "Million"
    number_words[1000000000] = "Billion"

    # Print the dictionary
    # for key, value in number_words.items():
    #     print(f"{key} => {value}")
    length = len(str(number))
    if (length <= 1):
         print(number_words[number])
    elif(1 < length < 3):
        if(number<=20):
           print(number_words[number])  
        else:
           ones = number % 10
           tens = number - ones
           print(f"{number_words[tens]} {number_words[ones]}")
    elif(2 < length < 4):
        
    
        
interger2word()




    