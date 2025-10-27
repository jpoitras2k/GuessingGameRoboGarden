import random
import math

class NumberGuesser:
    
    # A class designed to pick a random number within a given range and pre-calculate five required hint properties using private methods.
    
    def __init__(self, min_num=1, max_num=100):
        # Private attributes for range management
        self._min_num = min_num
        self._max_num = max_num
        
        # The randomly selected secret number using random import
        self.secret_number = random.randint(min_num, max_num)
        
        # Five properties (public attributes) to store the hints in str or an empty list
        self.parity_hint = "" 
        self.factors_hint = []
        self.multiples_hint = []
        self.larger_hint = ""
        self.smaller_hint = ""
        
        # Call the required private methods to calculate and set the hints
        self._calculate_hints()
        
    def _calculate_hints(self):
        
        # Private method to coordinate the calculation of all five hints.

        #print(f"DEBUG: Secret number selected is {self.secret_number}")
        
        # Calculate Parity (Even/Odd)
        self._set_parity()
        
        # Calculate Factors
        self._set_factors()
