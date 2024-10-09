#3a
import numpy as np #type: ignore

class Alice:
    def __init__(self):
        self.past_play_styles = [1,1] 
        self.results = [1,0]         
        self.opp_play_styles = [1,1]  
        self.points = 1
            

    def play_move(self):
        """
        Decide Alice's play style for the current round. Implement your strategy for 3a here.
        
        Returns: 
            0 : attack
            1 : balanced
            2 : defence

        """
        n_a = self.points
        n_b = len(self.results)-n_a
        temp1 = n_b/(n_a+n_b)
        p_attack = (temp1+0.7)/3 #subtracted some terms of balanced from attack to make it simpler
        p_defence = 0.346969696969696969697 #not the actual expected payoff from defence as some terms are subtracted
        p_balanced = 3/30 + 1/9 + 1/10 + 0.5*(1/9+1/6) 
        # we can see that p_balanced is always less than p_defence, so we can leave that.
        if p_attack > p_defence:
            return 0
        else:
            return 2
        
        
    
    def observe_result(self, own_style, opp_style, result):
        """
        Update Alice's knowledge after each round based on the observed results.
        
        Returns:
            None
        """
        self.past_play_styles.append(own_style)
        self.results.append(result)
        self.opp_play_styles.append(opp_style)
        self.points += result
 

class Bob:
    def __init__(self):
        # Initialize numpy arrays to store Bob's past play styles, results, and opponent's play styles
        self.past_play_styles = [1,1]
        self.results = [0,1]          
        self.opp_play_styles = [1,1]
        self.points = 1

    def play_move(self):
        """
        Decide Bob's play style for the current round.

        Returns:
            Returns: 
            0 : attack
            1 : balanced
            2 : defence
        
        """
        move = np.random.choice([0, 1, 2])
        return move
        
    
    def observe_result(self, own_style, opp_style, result):
        """
        Update Bob's knowledge after each round based on the observed results.
        
        Returns:
            None
        """
        self.past_play_styles.append(own_style)
        self.results.append(result)
        self.opp_play_styles.append(opp_style)
        self.points += result
 

def simulate_round(alice, bob, payoff_matrix):
    """
    Simulates a single round of the game between Alice and Bob.
    
    Returns:
        None
    """
    payoff_matrix[(0,0)] = (bob.points/(bob.points+alice.points),0,alice.points/(bob.points+alice.points))
    alice_move = alice.play_move()
    bob_move  = bob.play_move()
    key = (alice_move,bob_move)
    p1,p2,p3 = payoff_matrix[key]
    outcome = np.random.choice([1,0.5,0], p = [p1,p2,p3])
    alice.observe_result(alice_move,bob_move,outcome)
    bob.observe_result(bob_move,alice_move,1-outcome)
    


def monte_carlo(num_rounds):
    """
    Runs a Monte Carlo simulation of the game for a specified number of rounds.
    
    Returns:
        None
    """
    alice = Alice()
    bob = Bob()
    payoff_matrix = {
        (0, 0): (bob.points/(bob.points+alice.points),0,alice.points/(bob.points+alice.points)),
        (0, 1): (0.7, 0, 0.3),
        (0, 2): (5/11, 0, 6/11),
        (1, 0): (0.3, 0, 0.7),
        (1, 1): (1/3, 1/3, 1/3),
        (1, 2): (3/10, 1/2, 1/5),
        (2, 0): (6/11, 0, 5/11),
        (2, 1): (0.2, 0.5, 0.3),
        (2, 2): (0.1, 0.8, 0.1)
    }
    for _ in range(num_rounds):
        simulate_round(alice,bob,payoff_matrix)
    print("Alice's avg points:", alice.points/num_rounds)
    print("Bob's avg points:", bob.points/num_rounds)
 

# Run Monte Carlo simulation with a specified number of rounds
if __name__ == "__main__":
    monte_carlo(num_rounds=10**5)
