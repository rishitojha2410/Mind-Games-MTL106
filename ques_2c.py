import numpy as np  #type: ignore

class Alice:
    def __init__(self):
        self.past_play_styles = [1,1]
        self.results = [1,0]          
        self.opp_play_styles = [1,1]
        self.points = 1

    def play_move(self):
        """
        Decide Alice's play style for the current round. If you think there is no better strategy than 2a,
        then implement the same strategy here. Else implement that non-greedy strategy here.
        
        Returns: 
            0 : attack
            1 : balanced
            2 : defence
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
        # Initialize numpy arrays to store Bob's past play styles, results, and opponent's play styles
        self.past_play_styles = [1,1]
        self.results = [0,1]          
        self.opp_play_styles = [1,1]
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
    
    alice_move = alice.play_move()
    bob_move  = bob.play_move()
    key = (alice_move,bob_move)
    p1,p2,p3 = payoff_matrix[key]
    outcome = np.random.choice([1,0.5,0], p = [p1,p2,p3])
    alice.observe_result(alice_move,bob_move,outcome)
    bob.observe_result(bob_move,alice_move,1-outcome)


def estimate_tau(T):
    """
    Estimate the expected value of the number of rounds taken for Alice to win 'T' rounds.
    Your total number of simulations must not exceed 10^5.

    Returns:
        Float: estimated value of E[tau]
    """
    a = Alice()
    b = Bob()
    payoff_matrix = {
        (0, 0): (b.points/(a.points+b.points), 0, a.points/(a.points+b.points)),
        (0, 1): (0.7, 0, 0.3),
        (0, 2): (5/11, 0, 6/11),
        (1, 0): (0.3, 0, 0.7),
        (1, 1): (1/3, 1/3, 1/3),
        (1, 2): (3/10, 1/2, 1/5),
        (2, 0): (6/11, 0, 5/11),
        (2, 1): (0.2, 0.5, 0.3),
        (2, 2): (0.1, 0.8, 0.1)
    }
    k = 0
    p = []
    while k <=10**5:
        a = Alice() #reinitializes alice and bob after each time alice reaches T wins
        b = Bob()
        wins = 1
        rounds = 2
        while wins<T:
            simulate_round(a,b,payoff_matrix)
            k+=1
            rounds+=1
            if a.results[-1]==1:
                wins+=1
        p.append(rounds)
    return sum(p)/len(p)
# estimate_tau(32)