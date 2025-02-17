This code creates a tictactoe game using the concepts of Reinforcement Learning, particularly Q learning.
It uses the Bellman Equation to train the machine over a series of multiple episodes and then the user plays against it.
It can be improved by increasing the number of episodes or by changing the values of epsilong and gamma.

## How to Play
1. Run the game using the instructions below.
2. Select the game mode:
   - Human vs. Human: Both players take turns to play.
   - Human vs. AI: The human player competes against an AI agent.
3. Players will be prompted to enter their moves by specifying the position (1-9) of their choice on a 3x3 grid:
   ```
   1 | 2 | 3
   ---------
   4 | 5 | 6
   ---------
   7 | 8 | 9
   ```
4. The game continues until:
   - One player gets three marks in a row (horizontal, vertical, or diagonal).
   - The grid is full, resulting in a draw.


## Prerequisites
- Python 3.x
