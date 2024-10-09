import numpy as np     #type: ignore

class Alice:
    def __init__(self):
        self.past_play_styles = [0, 0]  
        self.results = [1, 0]           
        self.opp_play_styles = [0, 0]  
        self.points = 1

    def play_move(self):
        """
        Decide Alice's play style for the current round. Implement your strategy for 2a here.
         
        Returns: 
            0 : attack
            1 : balanced
            2 : defence

        """
        """
        the optimal strategy is greedy. we can use dp (which considers all future rounds)
        to show that Alice's choice of action depends solely on maximizing her points in 
        the current round as the transition between rounds is influenced only by the immediate result.
        """
        if self.results[-1] == 1:
            return 0 if (1 - self.points/len(self.results))>6/11 else 2
        if self.results[-1]==0:
            return 1
        else:
            return 0
        
    
    def observe_result(self, own_style, opp_style, result):
        """
        Update Alice's knowledge after each round based on the observed results.
        
        Returns:
            None
        """
        self.past_play_styles.append(own_style)
        self.opp_play_styles.append(opp_style)
        self.results.append(result)
        self.points += result


class Bob:
    def __init__(self):
        self.past_play_styles = [0, 0] 
        self.results = [0, 1]          
        self.opp_play_styles = [0, 0]   
        self.points = 1

    def play_move(self):
        """
        Decide Bob's play style for the current round.

        Returns: 
            0 : attack
            1 : balanced
            2 : defence
        """
        if self.results[-1] == 1:
            return 2  
        elif self.results[-1] == 0.5:
            return 1  
        else:  
            return 0  
        
    
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
    payoff_matrix[(0,0)] = (bob.points/(alice.points+bob.points),0,alice.points/(alice.points+bob.points))
    alice_move = alice.play_move()
    bob_move = bob.play_move()
    p1, p2, p3 = payoff_matrix[(alice_move,bob_move)]
    outcome = np.random.choice([1, 0.5, 0], p=[p1, p2, p3])
    alice.observe_result(alice_move, bob_move, outcome)
    bob.observe_result(bob_move, alice_move, 1-outcome)
    
def monte_carlo(num_rounds):
    """
    Runs a Monte Carlo simulation of the game for a specified number of rounds.
    
    Returns:
        None
    """
    alice = Alice()
    bob = Bob()
    payoff_matrix = {
        (0, 0): (bob.points/(alice.points+bob.points), 0, alice.points/(alice.points+bob.points)),
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
        simulate_round(alice, bob, payoff_matrix)
    print("Alice's avg points:", alice.points/num_rounds)
    print("Bob's avg points:",bob.points/num_rounds)

# Run Monte Carlo simulation with a specified number of rounds
if __name__ == '__main__':
    monte_carlo(num_rounds = 100000)
