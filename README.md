# MTL106 - Probability and Stochastic Processes  
## Assignment 1: Mind Games

**Deadline**: 10th September 2024

### Overview
Alice and Bob are playing a series of chess matches, where they can choose different strategies each round (aggressive, balanced, or defensive). The assignment explores the optimal strategies for Alice based on different scenarios involving probabilistic outcomes. You are required to solve both theoretical and coding problems, using Monte Carlo simulations to validate your solutions.

### Problem Breakdown

#### 1. Alice and Bob Always Attack
- **1(a)**: Calculate the probability that after `T` rounds, Alice wins `T1T2` matches and Bob wins `T3T4` matches.
  - Let `T1T2` and `T3T4` represent the last four digits of your entry number. Replace any zeros in your entry number with 9.
  - Example: If the entry number is `2020AB12345`, then `T1T2 = 23` and `T3T4 = 45`, with `T = 68`.

- **1(b)**: Define a random variable `Xi`:
  - `Xi = 1` if Alice wins round `i`, 
  - `Xi = 0` if it’s a draw, 
  - `Xi = -1` if Alice loses.
  
  Calculate the expected value and variance of the sum of `Xi` over `T` rounds, where `T` is the last two digits of your entry number.

#### 2. Bob's Strategy Depends on His Previous Round
- **2(a)**: If Bob's current strategy is based on his performance in the previous round (defensive if he won, balanced if it was a draw, and aggressive if he lost), determine Alice's optimal strategy to maximize points in the current round.
  - Validate your findings with Monte Carlo simulations.

- **2(b)**: Is Alice's greedy strategy (optimal per round) the best approach for maximizing total points over all rounds? If not, identify a situation where a non-greedy strategy outperforms the greedy strategy.
  - Use Monte Carlo simulations to support your answer.

- **2(c)**: Estimate the expected number of rounds `τ` for Alice to win `T` matches, using Monte Carlo simulations.
  - `T` is the last two digits of your entry number.

#### 3. Bob Chooses Play Style Randomly
- **3(a)**: Determine Alice's optimal strategy when Bob's play style is chosen uniformly at random for each round.
  
- **3(b)**: Calculate Alice's optimal strategy and expected number of points after `T` rounds, where `T` is the last two digits of your entry number.
  - Validate your solution with Monte Carlo simulations.

### Instructions
- Run Monte Carlo simulations for **105 iterations**.
- Clearly show all your calculations and **comment your code** for readability.
- Ensure your code runs within **20 seconds** for all test cases.
- **Plagiarism** will be penalized heavily, and all code will be checked for plagiarism.

### Submission Format
1. Implement your solutions in the respective Python files for questions 1, 2a, 2b, 2c, 3a, and 3b.
2. For theoretical derivations, submit your solutions in **LaTeX** or upload neatly written derivations.
3. Organize your code in a folder named **EntryNumber_mtl106_a1** with files named according to the question number.
4. Ensure you implement the provided starter code functions:
   - `play_move` and `observe_result` for the Alice and Bob player classes.
   - Functions for `simulate_round` and `monte_carlo` to run the simulations.

### Notes
- Replace any zeros in your entry number with 9 while solving the assignment.
- Make sure all code files follow the format provided in the starter code.

Good luck, and happy coding!

