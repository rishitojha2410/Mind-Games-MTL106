payoff_matrix = {
        (0, 0): (lambda na,nb:nb/(na+nb),0,lambda na,nb: na/(na+nb)),
        (0, 1): (0.7, 0, 0.3),
        (0, 2): (5/11, 0, 6/11),
        (1, 0): (0.3, 0, 0.7),
        (1, 1): (1/3, 1/3, 1/3),
        (1, 2): (3/10, 1/2, 1/5),
        (2, 0): (6/11, 0, 5/11),
        (2, 1): (0.2, 0.5, 0.3),
        (2, 2): (0.1, 0.8, 0.1)
    }

# Problem 3b
def optimal_strategy(na, nb, tot_rounds):
    """
    Calculate the optimal strategy for Alice maximize her points in the future rounds
    given the current score of Alice(na) and Bob(nb) and the total number of rounds(tot_rounds).
    
    Return the answer in form of a list [p1, p2, p3],
    where p1 is the probability of playing Attacking
    p2 is the probability of playing Balanced
    p3 is the probability of playing Defensive
    """
    if tot_rounds ==0:
        return [0,0,0]

    if (na,nb,tot_rounds) in memo:
        return memo[(na,nb,tot_rounds)]
    
    best_strat = [0,0,0] #placeholder
    best_expected_points = -10000 #placeholder
    for alice_move in range(3):
        expected_points_move = 0
        for bob_move in range(3):
            if callable(payoff_matrix[(alice_move,bob_move)][0]):
                p_win, p_draw,p_loss = payoff_matrix[(alice_move,bob_move)][0](na,nb),payoff_matrix[(alice_move,bob_move)][1],payoff_matrix[(alice_move,bob_move)][2](na,nb)
            else:
                p_win, p_draw,p_loss = payoff_matrix[(alice_move,bob_move)]
            future_points_win = p_win*(1+expected_points(tot_rounds-1,na+1,nb))
            future_points_draw = p_draw*(0.5+expected_points(tot_rounds-1,na+0.5,nb+0.5))
            future_points_loss = p_loss*(expected_points(tot_rounds-1,na,nb+1))
            expected_points_move += (future_points_win+future_points_draw+future_points_loss)
        if expected_points_move>=best_expected_points:
            best_expected_points = expected_points_move
            best_strat = [1 if alice_move==0 else 0, 1 if alice_move==1 else 0, 1 if alice_move==2 else 0]
    memo[(na,nb,tot_rounds)] = best_strat
    return best_strat
memo={}
def expected_points(tot_rounds,na=1,nb=1):
    """
    Given the total number of rounds(tot_rounds), calculate the expected points that Alice can score after the tot_rounds,
    assuming that Alice plays optimally.

    Return : The expected points that Alice can score after the tot_rounds.
    """
    na = nb = 1
    if tot_rounds == 0:
        return 0
    if (na,nb,tot_rounds) in memo:
        return memo[(na,nb,tot_rounds)]
    optimal_strat = optimal_strategy(na,nb,tot_rounds)
    p_attack,p_balanced,p_defence = optimal_strat
    p_win = 1/3*(p_attack*(sum([payoff_matrix[(0,0)][0](na,nb),payoff_matrix[(0,1)][0],payoff_matrix[(0,2)][0]])) + p_balanced*(sum([payoff_matrix[(1,i)][0] for i in range(3)])) + p_defence*(sum([payoff_matrix[(2,i)][0] for i in range(3)])))
    p_draw = 1/3*(p_attack*(sum([payoff_matrix[(0,i)][1] for i in range(3)])) + p_balanced*(sum([payoff_matrix[(1,i)][1] for i in range(3)])) + p_defence*(sum([payoff_matrix[(2,i)][1] for i in range(3)])))
    p_loss = 1/3*(p_attack*(sum([payoff_matrix[(0,0)][2](na,nb),payoff_matrix[(0,1)][2],payoff_matrix[(0,2)][2]])) + p_balanced*(sum([payoff_matrix[(1,i)][2] for i in range(3)])) + p_defence*(sum([payoff_matrix[(2,i)][2] for i in range(3)])))
    points = p_win*(1+expected_points(tot_rounds-1,na+1,nb)) +p_draw*(0.5+expected_points(tot_rounds-1,na+0.5,nb+0.5)) + p_loss*expected_points(tot_rounds-1,na,nb+1)
    memo[(na,nb,tot_rounds)] = points
    return points


