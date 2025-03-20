# Tic-Tac-Toe AI

## Overview
This project implements a Tic-Tac-Toe game with a reinforcement learning AI using Q-learning. The AI learns optimal strategies by playing against a random opponent.

## Features
- **Q-learning AI** that learns optimal moves through self-play.
- **Trainable AI** with adjustable hyperparameters (`alpha`, `gamma`, `epsilon`).
- **Human vs AI mode** where a user can play against the trained AI.
- **State-based Q-table** for learning and decision-making.

## Files
- `tic_tac_toe_ai.py` - The main script containing game logic and AI training.

## How It Works
1. **Training:**
   - The AI plays games against a random opponent.
   - It updates its Q-values using the Q-learning formula.
   - Training runs for a specified number of episodes (default: 60,000).

2. **Playing Against AI:**
   - The user plays as `X`, and the AI plays as `O`.
   - The AI selects moves using an epsilon-greedy strategy.
   - The game board updates after each move, displaying the state.

## Installation
Ensure you have Python installed, then install dependencies:
```sh
pip install numpy
```

## Running the Game
1. Train the AI (optional):
   ```sh
   python tic_tac_toe_ai.py
   ```
2. Play against the trained AI:
   ```sh
   python tic_tac_toe_ai.py
   ```
   (The script automatically trains the AI before starting the game.)

## Future Enhancements
- Save and load Q-values for persistent learning.
- Improve opponent strategy for better AI training.
- Add a GUI for better user experience.

## Author
Sarayu Ventrapati

