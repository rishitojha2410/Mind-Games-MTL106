# MTL106 - Probability and Stochastic Processes  
## Assignment 1: Mind Games

### Overview
Alice and Bob are playing a series of chess matches, where they can choose different strategies each round (aggressive, balanced, or defensive). The assignment explores the optimal strategies for Alice based on different scenarios involving probabilistic outcomes. You are required to solve both theoretical and coding problems, using Monte Carlo simulations to validate your solutions.
### Payoff Matrix:

The following matrix describes the probabilities for each possible combination of strategies Alice and Bob might choose in a round:

|                 | Attack (Bob)         | Balanced (Bob)        | Defence (Bob)         |
|-----------------|----------------------|-----------------------|-----------------------|
| **Attack (Alice)**   | (nB / (nA + nB), 0, nA / (nA + nB)) | (7/10, 0, 3/10)       | (5/11, 0, 6/11)       |
| **Balanced (Alice)** | (3/10, 0, 7/10)   | (1/3, 1/3, 1/3)       | (3/10, 1/2, 1/5)      |
| **Defence (Alice)**  | (6/11, 0, 5/11)   | (1/2, 1/2, 3/10)      | (1/10, 4/5, 1/10)     |

### Problem Breakdown
Alice wins the first round and loses the second. Determined to outperform Bob, Alice decides to analyze what her optimal strategy should be in response to various strategies that Bob might use.


#### 1. Alice and Bob Always Attack
- **Q1(a)**: Calculate the probability that after `T` rounds, Alice wins `T1T2` matches and Bob wins `T3T4` matches.
  - Let `T1T2` and `T3T4` represent the last four digits of your entry number. Replace any zeros in your entry number with 9.
  - Example: If the entry number is `2020AB12345`, then `T1T2 = 23` and `T3T4 = 45`, with `T = 68`.

- **Q1(b)**: Define a random variable `Xi`:
  - `Xi = 1` if Alice wins round `i`, 
  - `Xi = 0` if it’s a draw, 
  - `Xi = -1` if Alice loses.
  
  Calculate the expected value and variance of the sum of `Xi` over `T` rounds, where `T` is the last two digits of your entry number.

#### 2. Bob's Strategy Depends on His Previous Round
- **Q2(a)**: If Bob's current strategy is based on his performance in the previous round (defensive if he won, balanced if it was a draw, and aggressive if he lost), determine Alice's optimal strategy to maximize points in the current round.
  - Validate your findings with Monte Carlo simulations.

- **Q2(b)**: Is Alice's greedy strategy (optimal per round) the best approach for maximizing total points over all rounds? If not, identify a situation where a non-greedy strategy outperforms the greedy strategy.
  - Use Monte Carlo simulations to support your answer.

- **Q2(c)**: Estimate the expected number of rounds `τ` for Alice to win `T` matches, using Monte Carlo simulations.
  - `T` is the last two digits of your entry number.

#### 3. Bob Chooses Play Style Randomly
- **Q3(a)**: Determine Alice's optimal strategy when Bob's play style is chosen uniformly at random for each round.
  
- **Q3(b)**: Calculate Alice's optimal strategy and expected number of points after `T` rounds, where `T` is the last two digits of your entry number.
  - Validate your solution with Monte Carlo simulations.

### Instructions
- Run Monte Carlo simulations for **10^5 iterations**.
- Clearly show all your calculations and **comment your code** for readability.
- Ensure your code runs within **20 seconds** for all test cases.
- **Plagiarism** will be penalized heavily, and all code will be checked for plagiarism.

### Notes
- Replace any zeros in your entry number with 9 while solving the assignment.
- Make sure all code files follow the format provided in the starter code.

Good luck, and happy coding!

