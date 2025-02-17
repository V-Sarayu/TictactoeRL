import numpy as np
import random

class TicTacToeAI:
    def __init__(self, alpha=0.5, gamma=0.9, epsilon=0.2):
        self.q_table = {}  # Store state-value pairs
        self.alpha = alpha  # Learning rate
        self.gamma = gamma  # Discount factor
        self.epsilon = epsilon  # Exploration vs Exploitation

    def get_q_value(self, state, action):
        #Returns Q-value for a given state-action pair
        return self.q_table.get((state, action), 0)

    def choose_action(self, state, available_actions):
        #choose action using epsilon-greedy strategy
        if random.uniform(0, 1) < self.epsilon: # if a random floating number is less than 0.2
            return random.choice(available_actions)  # With 20% probability of epsilon , the AI chooses a random move to explore new possibilities
        q_values = {action: self.get_q_value(state, action) for action in available_actions}
        return max(q_values, key=q_values.get)  # Exploit (choose best known move)

    def update_q_table(self, state, action, reward, next_state, next_available_actions):
        #Update Q-table using the Q-learning formula
        old_value = self.get_q_value(state, action)
        future_rewards = [self.get_q_value(next_state, a) for a in next_available_actions] if next_available_actions else [0]
        best_future_reward = max(future_rewards)
        new_value = old_value + self.alpha * (reward + self.gamma * best_future_reward - old_value)
        self.q_table[(state, action)] = new_value  # Update Q-value

class TicTacToe:
    def __init__(self):
        self.board = [" "] * 9
        self.winner = None

    def reset(self):
        """Reset the board for a new game."""
        self.board = [" "] * 9
        self.winner = None

    def available_moves(self):
        """Return available positions on the board."""
        return [i for i in range(9) if self.board[i] == " "]

    def make_move(self, position, symbol):
        """Place X or O on the board."""
        if self.board[position] == " ":
            self.board[position] = symbol
            return True
        return False

    def check_winner(self):
        """Check if someone has won."""
        win_conditions = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
            [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
            [0, 4, 8], [2, 4, 6]             # Diagonals
        ]
        for condition in win_conditions:
            if self.board[condition[0]] == self.board[condition[1]] == self.board[condition[2]] and self.board[condition[0]] != " ":
                self.winner = self.board[condition[0]]
                return self.winner
        return None

    def is_draw(self):
        """Check if the board is full (draw)."""
        return " " not in self.board and self.winner is None

# Training AI
def train_ai(episodes=60000):
    ai = TicTacToeAI()
    game = TicTacToe()

    for episode in range(episodes):
        game.reset()
        state = tuple(game.board)

        while True:
            available_moves = game.available_moves()
            action = ai.choose_action(state, available_moves)
            game.make_move(action, "O")

            if game.check_winner() == "O":
                ai.update_q_table(state, action, 1, None, [])
                break
            if game.is_draw():
                ai.update_q_table(state, action, 0, None, [])
                break

            # Opponent (random moves)
            opponent_action = random.choice(game.available_moves())
            game.make_move(opponent_action, "X")

            if game.check_winner() == "X":
                ai.update_q_table(state, action, -1, None, [])
                break

            # Update Q-table
            next_state = tuple(game.board)
            next_available_moves = game.available_moves()
            ai.update_q_table(state, action, 0, next_state, next_available_moves)

            state = next_state  # Move to next state

        if episode % 5000 == 0:
            print(f"Episode {episode} complete.") # formatting string instead of %

    print("Training finished!")
    return ai

# Test the trained AI
def play_against_ai(ai):
    game = TicTacToe()
    game.reset()

    print("Play against the AI! You are X.")

    while True:
        # Player Move
        move = int(input("Enter your move (1-9): ")) - 1
        if move not in game.available_moves():
            print("Invalid move, try again.")
            continue
        game.make_move(move, "X")

        if game.check_winner() == "X":
            print("You win!")
            break
        if game.is_draw():
            print("It's a draw!")
            break

        # AI Move
        ai_move = ai.choose_action(tuple(game.board), game.available_moves())
        game.make_move(ai_move, "O")

        # Print board
        for row in [game.board[i:i+3] for i in range(0, 9, 3)]:
            print("| " + " | ".join(row) + " |")

        if game.check_winner() == "O":
            print("AI wins!")
            break
        if game.is_draw():
            print("It's a draw!")
            break

# Train the AI and play
trained_ai = train_ai()
play_against_ai(trained_ai)
