import numpy as np

class Customer:
    """
    a single customer that moves through the supermarket
    in a MCMC simulation
    """

    def __init__(self, state):        
        self.state = state
        self.store_time = 0     ## how many minutes the person was shopping

    def __str__(self):
        return f"This is the Customer {self.name}"
    
    def __repr__(self):
        return f"Customer {self.name} in {self.state}"

    def next_state(self):
        '''
        Propogates the customer to the next state.
        Returns nothing
        '''
        location = np.random.choice(["fruit","spices","drinks","dairy","checkout"])

    def locations(self):
        if 
        
    def send_shoppping(self):
        return

    def is_active(self):
        '''
        Returns True if the customer has not reached the checkout yet.
        '''

## To Do
# multiplication of transition_prob
