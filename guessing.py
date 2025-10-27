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
        
        # Calculate Multiples
        self._set_multiples()
        
        # Calculate Larger/Smaller Comparisons
        self._set_comparison_hints()


    # Calculates a hint for either even or odd 
    def _set_parity(self):
        if self.secret_number % 2 == 0:
            self.parity_hint = "It's an **even** number."
        else:
            self.parity_hint = "It's an **odd** number."
   
    # Calculates a hint for whether a number is a prime number or not 
    def _set_factors(self):
        all_factors = []
        # We only check up to the square root for efficiency
        for i in range(1, int(math.sqrt(self.secret_number)) + 1):
            if self.secret_number % i == 0:
                all_factors.append(i)
                if i * i != self.secret_number:
                    all_factors.append(self.secret_number // i)
                    
        all_factors = sorted([f for f in all_factors if f > 1 and f < self.secret_number])
        
        if len(all_factors) > 2:
            # Provide the two largest non-self factors as the hint
            self.factors_hint = [all_factors[-1], all_factors[-2]] 
        elif len(all_factors) > 0:
            self.factors_hint = all_factors
        else:
            # Prime number case
            self.factors_hint = ["(It appears to be a prime number!)"]


    def _set_multiples(self):
        #Calculates and sets the multiples_hint property.
        # Give a small list of multiples just above the secret number
        self.multiples_hint = [
            self.secret_number * 2, 
            self.secret_number * 3, 
            self.secret_number * 4
        ]

    def _set_comparison_hints(self):
        """
        Calculates and sets the larger and smaller comparison hints.
        We'll use the midpoint of the range as the comparison for this example.
        """
        midpoint = (self._min_num + self._max_num) // 2
        
        # Larger Hint (comparison against the midpoint)
        if self.secret_number > midpoint:
            self.larger_hint = f"The number is larger than {midpoint}."
        elif self.secret_number < midpoint:
            self.larger_hint = f"The number is smaller than or equal to {midpoint}."
        else:
            self.larger_hint = f"The number is exactly {midpoint}."
            
        # Smaller Hint (comparison against a quarter-point or another relevant number)
        quarter_point = self._min_num + (self._max_num - self._min_num) // 4
        if self.secret_number < quarter_point:
            self.smaller_hint = f"The number is less than {quarter_point}."
        else:
            self.smaller_hint = f"The number is greater than or equal to {quarter_point}."
# The Chatbot Logic - guesses and gives a few calculated guesses

def run_guesser_chatbot():
    
    guesser = NumberGuesser(min_num=1, max_num=100)
    secret = guesser.secret_number
    guess = None
    attempts = 0

    print("\n--- Welcome to the Number Guesser Chatbot! ---")
    print(f"I've picked a number between {guesser._min_num} and {guesser._max_num}.")
    print("You have 5 attempts. I'll give you three hints now.\n")

    # The required three hints are easily accessible from the public properties
    hints = [
        guesser.parity_hint,
        f"Some of its factors are: {guesser.factors_hint}",
        guesser.larger_hint,
    ]
    
    print("YOUR HINTS:")
    for i, hint in enumerate(hints, 1):
        print(f"{i}. {hint}")
    print("\n-------------------------------------------")

    while guess != secret and attempts < 5:
        try:
            guess_input = input(f"Attempt {attempts + 1} of 5. What is your guess? ")
            guess = int(guess_input)
            attempts += 1

            if guess == secret:
                print(f"\n🎉 CONGRATULATIONS! You guessed the number {secret} in {attempts} attempts!")
            elif guess < secret:
                print("Too low! Try a higher number.")
            else:
                print("Too high! Try a lower number.")

        except ValueError:
            print("That's not a valid number. Please try again.")
            
    if guess != secret:
        print(f"\nGame Over. You ran out of attempts! The secret number was {secret}.")

run_guesser_chatbot()
