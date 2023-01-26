# SI 206 HW4
# Your name:
# Your student id:
# Your email:
# Who you worked with on this homework:

import unittest

class Customer:
    def __init__(self, name, ticket_no, wallet = 50):
        '''initializes the name, ticket number, and the amount of money on the customer's wallet'''
        self.name = name
        self.wallet = wallet
        self.ticket_no = ticket_no

    def __str__(self):
        '''returns the name of the customer and their ticket number'''
        return f'My name is {self.name}, and my ticket number is {self.ticket_no}'

    def reload_wallet(self, amount):
        '''reloads the customers wallet with the passed amount'''
        self.wallet += amount

    def place_order(self, vendor, order):
        ''' 
        1) Call the calculate_cost method to calculate the total cost of the 
           order by totaling the cost for each food object in the order.
        2) Check if the customer has the total cost or more in their wallet.
           If they do not have enough money then print "Insufficient funds"
           and return False.
        3) Call the process_order method on the vendor object. If process_order
           returns True remove the total cost from the customer’s wallet and
           add it to the vendor's earnings and return True.
           Otherwise, return False.
        '''

        pass

    ### EXTRA CREDIT ###
    def raffle(self):
        '''
        draw a list of 5 random, non-repeating winners and award $25 to the winners
        if selected, print 'Congratulations! You are one of the winners.'
        if not, print 'You were not selected. Better luck next time!'
        '''
        pass

    ####################
 
class Food:

    def __init__(self, name, cost):
        ''' initializes the name and cost '''
        self.name = name
        self.cost = cost

    def __str__(self):
        ''' returns the name and cost '''
        return self.name + " " + str(self.cost)

class Vendor:

    def __init__(self, name, earnings=0):
        ''' 
        initializes the name and earnings of the vendor
        sets the inventory to an empty dictionary
        '''
        self.name = name
        self.earnings = earnings
        self.inventory = {}
    
    def __str__(self):
        '''returns the name of the vendor and their menu'''
        print(f"Hello we are {self.name}. This is the current menu {self.inventory.keys()}")

    def receive_payment(self, amount):
        '''adds the passed amount to the vendors earnings'''
        self.earnings += amount

    def calculate_cost(self, food, quantity, customer):
        '''
        takes the quantity and returns the total for a food item 

        checks if the customer is one of the first twenty people that purchased a
        ticket for the festival and gives the customer a 25% discount
        '''
        pass

    def stock_up(self, food, quantity):
        ''' 
        If the food is already in the inventory then add the passed quantity
        to the existing value.  Otherwise set the value for the food
        in the inventory dictionary.
        '''
        pass

    def process_order(self, order):
        '''
        Checks that there is enough food for an order and if not returns False,
        otherwise it subtracts the food item from the quantity in the inventory
        and returns True.
        '''
    
        pass


class TestAllMethods(unittest.TestCase):

    def setUp(self):
        self.bowl = Food('Mediterranean Bowl',10.00)
        self.falafel = Food('Falafel', 4.50)
        self.pasta = Food('Pasta', 9.50)
        self.pizza = Food('Pizza', 10.00)

        self.bob = Customer(name='Bob', ticket_no=10)
        self.alice = Customer(name='Alice', ticket_no=50, wallet=1.50)

        self.vegano_italiano = Vendor(name='Vegano Italiano')
        self.pita_pita = Vendor(name='Pita Pita')

    # Check the constructors
    def test_customer_constructor(self):
        self.assertEqual(self.bob.name, 'Bob')
        self.assertEqual(self.bob.wallet, 50)

    def test_food_constructor(self):
        self.assertEqual(self.pasta.name, 'Pasta')
        self.assertAlmostEqual(self.pasta.cost, 9.50, 1)
        self.assertEqual(self.pizza.name, 'Pizza')
        self.assertAlmostEqual(self.pizza.cost, 10.00, 0)

    def test_vendor_constructor(self):
        self.assertEqual(self.vegano_italiano.name, 'Vegano Italiano')
        self.assertEqual(self.vegano_italiano.earnings, 0)
        self.assertEqual(self.pita_pita.name,'Pita Pita')
        self.assertEqual(self.pita_pita.inventory, {})

    # Check the reload_wallet method for customer
    def test_customer_reload_wallet(self):
        self.alice.reload_wallet(10)
        self.assertAlmostEqual(self.alice.wallet, 11.50, 1)

    # Check the calculate_cost for vendor
    def test_vendor_calculate_cost(self):
        self.assertAlmostEqual(self.vegano_italiano.calculate_cost(self.pasta, 10, self.alice), 95.00, 0)

    # Check if discount is applied
        self.assertAlmostEqual(self.pita_pita.calculate_cost(self.bowl, 1, self.bob), 7.50, 1)

    # Check the receive_payment method for vendor
    def test_vendor_receive_payment(self):
        self.pita_pita.receive_payment(50)
        self.assertAlmostEqual(self.pita_pita.earnings, 50.00, 0)

    # Check the stock_up method for vendor
    def test_vendor_stock_up(self):
        self.pita_pita.stock_up(self.bowl.name, 4)
        self.pita_pita.stock_up(self.falafel.name, 10)
        self.assertEqual(self.pita_pita.inventory, {'Mediterranean Bowl': 4, 'Falafel': 10})

        self.vegano_italiano.stock_up(self.pasta.name, 5)
        self.vegano_italiano.stock_up(self.pizza.name, 3)
        self.assertEqual(self.vegano_italiano.inventory, {'Pasta': 5, 'Pizza': 3})

    # Check the place_order method for customer
    def test_customer_place_order(self):
        ted = Customer(name='Ted', ticket_no=50)
        vegano_italiano = Vendor(name='Vegano Italiano')

        vegano_italiano.stock_up(self.pasta.name, 5)
        vegano_italiano.stock_up(self.pizza.name, 3)

        # Scenerio 1: customer doesn't have enough money in their wallet
        
    
		# Scenerio 2: vendor doesn't have enough food left in stock
        

        # Scenerio 3: vendor doesn't sell that food item
        
   
    def test_customer_place_order_2(self):
        ali = Customer(name='Ali', ticket_no=61)
        pita_pita = Vendor(name='Pita Pita')
        pita_pita.stock_up(self.bowl.name, 5)
        pita_pita.stock_up(self.falafel.name, 10)

        # Fix the test cases below to check if the customer's wallet and the vendor's earnings has 
        # the right amount after an order is processed
        
        self.assertEqual(ali.place_order(pita_pita, {self.bowl: 2, self.falafel: 4}), False)
        self.assertAlmostEqual(self.ali.wallet, 12.00, 0)
        self.assertAlmostEqual(ali.earnings, 38.00, 0)


def main():
    pass

if __name__ == '__main__':
    unittest.main(verbosity = 2)
    main()
