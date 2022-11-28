import unittest
from basket import *

class TestPriceBasket(unittest.TestCase):

    def setUp(self):
        self.test_basket = PriceBasket(
            {'soup': 0, 'bread': 0, 'milk': 0, 'apple': 0})

    def test_get_input(self): # Testing the Get Input condition by giving the inputs: 1- apple , 1-bread
        test_input = self.test_basket.get_input()
        self.assertEqual(
            test_input, {'soup': 0, 'bread': 1, 'milk': 0, 'apple': 1})

    def test_get_input1(self): # Testing the Get Input condition by giving the inputs: 1- apple , 2-bread 
        test_input = self.test_basket.get_input()
        self.assertEqual(
            test_input, {'soup': 0, 'bread': 2, 'milk': 0, 'apple': 1})

    def test_calculate(self): # Testing the CALUCALATE function to calculate the total value for each of the basket without discounts 
        self.test_basket.items_dict = {          
            'soup': 0, 'bread': 0, 'milk': 1, 'apple': 2}     #  by giving the inputs: 2- apple , 1-milk 
        self.assertEqual(self.test_basket.calculate(), 3.30)

    
    def test_calculate1(self): # Changing the function name and testing the CALCULATE function with 2- apples
        self.test_basket.items_dict = {
            'soup': 0, 'bread': 0, 'milk': 0, 'apple': 2}
        self.assertEqual(self.test_basket.calculate(), 2.00)

    def test_calculate2(self):
        self.test_basket.items_dict = { 
            'soup': 1, 'bread': 1, 'milk': 1, 'apple': 2}  # Changing the function name and testing the CALCULATE function with 2- apples,
        self.assertEqual(self.test_basket.calculate(), 4.75)      # 1- soup, 1- bread, 1 - milk

    def test_discount_calc(self):        # Testing the DISCOUNT_CALC function and passing the values of total value: 4.3 & final value : 4.0 
        self.test_basket.total = 4.30    # with the values 1 - milk, 3 - apple
        self.test_basket.items_dict = {       
            'soup': 0, 'bread': 0, 'milk': 1, 'apple': 3}
        self.assertEqual(self.test_basket.discount_calc(), 4.00)

    def test_discount_calc_1(self):    # Testing the DISCOUNT_CALC function and passing the values of total value: 6.4 & final value :5.7
        self.test_basket.total = 6.40  # with the values 1 - milk, 3 - apple , soup - 2, bread - 1
        self.test_basket.items_dict = {
            'soup': 2, 'bread': 1, 'milk': 1, 'apple': 3}
        self.assertEqual(self.test_basket.discount_calc(), 5.70)
    
    def test_discount_calc_2(self):     # Testing the DISCOUNT_CALC function and passing the values of total value: 4.2 & final value : 3.4
        self.test_basket.total = 4.2    # with the values 0 - milk, 0 - apple , soup - 4, bread - 2
        self.test_basket.items_dict = {
            'soup': 4, 'bread': 2, 'milk': 0, 'apple': 0}
        self.assertEqual(self.test_basket.discount_calc(), 3.40)

    
    