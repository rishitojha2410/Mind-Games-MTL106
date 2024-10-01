"""
Use the following functions to add, multiply and divide, taking care of the modulo operation.
Use mod_add to add two numbers taking modulo 1000000007. ex : c=a+b --> c=mod_add(a,b)
Use mod_multiply to multiply two numbers taking modulo 1000000007. ex : c=a*b --> c=mod_multiply(a,b)
Use mod_divide to divide two numbers taking modulo 1000000007. ex : c=a/b --> c=mod_divide(a,b)
"""
M=1000000007

def mod_add(a, b):
    a=(a%M+M)%M
    b=(b%M+M)%M
    return (a+b)%M

def mod_multiply(a, b):
    a=(a%M+M)%M
    b=(b%M+M)%M
    return (a*b)%M

def mod_divide(a, b):
    a=(a%M+M)%M
    b=(b%M+M)%M
    return mod_multiply(a, pow(b, M-2, M))

# Problem 1a
def calc_prob(alice_wins, bob_wins):
    """
    Returns:
        The probability of Alice winning alice_wins times and Bob winning bob_wins times will be of the form p/q,
        where p and q are positive integers,
        return p.q^(-1) mod 1000000007.
    """

    #i= no_of rounds alice has won
    #j = no_of rounds bob has won
    def Probab(i,j,k,n_A,n_B,memo):
        if k ==0:
            return 1 if i==0 and j==0 else 0
        if (i,j,k,n_A,n_B) in memo:
            return memo[(i,j,k,n_A,n_B)]
        probability = 0 
        if i>0 and n_A>0:
            probability = mod_add(probability,mod_multiply(Probab(i-1,j,k-1,n_A-1,n_B,memo),mod_divide(n_B,n_A+n_B-1))) #probability that alice was at (nA-1) points and won the current round to get to nA points
        if j>0 and n_B>0:
            probability = mod_add(probability,mod_multiply(Probab(i,j-1,k-1,n_A,n_B-1,memo),mod_divide((n_A),n_A+n_B-1))) #probability that bob was at (nB-1) points and won the current round to get to nB points
        memo[(i,j,k,n_A,n_B)] = probability #memoization
        return memo[(i,j,k,n_A,n_B)]
            
    rounds = mod_add(alice_wins,bob_wins)
    memo = {}
    return Probab(alice_wins-1,bob_wins-1,rounds-2,alice_wins,bob_wins,memo)
    

    
    
# Problem 1b (Expectation)      
def calc_expectation(t):
    """
    Returns:
        The expected value of \sum_{i=1}^{t} Xi will be of the form p/q,
        where p and q are positive integers,
        return p.q^(-1) mod 1000000007.

    """
    ans = 0
    for i in range(t+1):
        ans = mod_add(ans,mod_multiply((2*i-t),calc_prob(i,t-i)))
    return ans
       

# Problem 1b (Variance)
def calc_variance(t):
    """
    Returns:
        The variance of \sum_{i=1}^{t} Xi will be of the form p/q,
        where p and q are positive integers,
        return p.q^(-1) mod 1000000007.

    """
    ans1 = 0
    for i in range(t+1):
        ans1 = mod_add(ans1,mod_multiply(((2*i-t)**2),calc_prob(i,t-i)))
    ans1 -= mod_multiply(calc_expectation(t),calc_expectation(t))
    return ans1

    
