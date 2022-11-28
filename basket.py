class PriceBasket:
    def __init__(self,items_dict):   
        self.soup = .65
        self.bread = .80
        self.milk = 1.30
        self.apple = 1.00
        self.total = 0
        self.items_dict = items_dict

    def get_input(self): 
        basket_input = str(input("Enter the items required:")).lower()  # To get the input for different items as required and are converted to lower case.
        temp = basket_input.split()        # converting the string input and to convert into a list of words
        self.items_dict = {'soup':0, 'bread':0, 'milk':0, 'apple':0}  # To reinitialise the dictionary when in case of invalid input is chosen
        for i in temp:  
            if i in self.items_dict:    
                self.items_dict[i] += 1 # updating the dictionary with the value of the number's occurance
            else:
                print(f"choose a valid input, {i} is not acceptable") 
                self.items_dict  = self.get_input()  # in case of an invalid  input the function will be called recursively
        return self.items_dict

# DECISION MADE: Dictionary is used to get the inputs by intialising it with 0's and updating the values of the dictionary
# with the number of times input keys were entered as input. Once an ivalid input is entered it calls the function recursively 
# Dictionary is chosen so to make the implementation effective and simpler.

    def calculate(self):    # To calculate the price value of all the items that have been given as inputs
        self.total = 0 
        for k,v in (self.items_dict.items()):  # Iterating through the dictionary and when the given input is valid & matches with the list of items
            if k == 'soup':                          # the values will be summed up to the 'total'  
                self.total += int(v) * self.soup
            if k == 'bread':
                self.total += int(v) * self.bread
            if k == 'milk':
                self.total += int(v) * self.milk
            if k == 'apple':
                self.total += int(v) * self.apple 
        self.total = round(self.total,2)     
        return self.total 

    def discount_calc(self):      # this function is to calculate the discount value if applicable 
        discount1,discount2,price = 0,0,0      
        x = int(self.items_dict['soup'] )  # the values from the dictionary who's key have a discount ,
        y = int(self.items_dict['bread'])      #  the values will be the number of times it is entered as input
        z = int(self.items_dict['apple'])
        # print(x,y)
        # print(self.items_dict)
        while x > 1 and y > 0:             #  If the number of soup tins are greater than 1 and number of bread is atleast 1 
            discount1 += .5 * self.bread     # The discount1 is discount of 2 soup tins + bread = 50% off for bread can be availed.
            x -= 1
            y -= 1                           # the values are decremented until it meets the requirement 
        while z > 0:
            discount2 += .1 * self.apple    # discount2 is the discount obtained if number of apples entered is atleast 1, 
            z -= 1                             # an offer 10% off can be applied to the total value 
        # print(discount1,discount2)
        price = self.total - discount1 - discount2 # the final price is calculated by deducting the discount price from that of total value 
        if discount1 == 0 and discount2 == 0: 
            print(f"Subtotal: £{self.total} (No offers available), Total price: £{self.total}")
        else:
            print(f"Subtotal: £{self.total}")
            if discount2 != 0:               
                print("Apples 10% off: 10p")
            if discount1 != 0:
                print("50% off on Bread: With 2 Soup tins") 
        return(round(price,2))

#-------------------------------To Run the code this code Please remove the comment for the below given code ---------------------------------

# items_dict = {'soup':0, 'bread':0, 'milk':0, 'apple':0}
# p = PriceBasket(items_dict)
# initial_dict = p.get_input()
# item_count = p.calculate()
# final_price = p.discount_calc()
# print(final_price) 