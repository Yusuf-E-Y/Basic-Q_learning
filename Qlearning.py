import numpy as np
import random
import os
import time

# Environment size
grid_size = 4  # 4x4 grid
actions = ["up", "down", "left", "right"]

# Q-table: (number of states x number of actions)
Q_table = np.zeros((grid_size * grid_size, len(actions)))

# Reward table: +10 for goal, 0 elsewhere
reward_table = np.zeros(grid_size * grid_size)
reward_table[-1] = 10  # Goal at the last cell

# Calculate state from coordinates
def get_state(x, y):
    return x * grid_size + y

# Apply action and return new state
def take_action(state, action):
    x, y = divmod(state, grid_size)
    if action == "up" and x > 0:
        x -= 1
    elif action == "down" and x < grid_size - 1:
        x += 1
    elif action == "left" and y > 0:
        y -= 1
    elif action == "right" and y < grid_size - 1:
        y += 1
    return get_state(x, y)

# Display the grid
def render_grid(state):
    os.system('cls' if os.name == 'nt' else 'clear')
    for i in range(grid_size):
        row = ""
        for j in range(grid_size):
            idx = get_state(i, j)
            if idx == state:
                row += " A "  # Agent
            elif idx == grid_size * grid_size - 1:
                row += " G "  # Goal
            else:
                row += " . "
        print(row)
    print()
    time.sleep(0.5)

# Q-Learning parameters
learning_rate = 0.1
discount_factor = 0.9
epsilon = 0.1
episodes = 1000

# Training loop
for episode in range(episodes):
    state = random.randint(0, grid_size * grid_size - 2)  # Start anywhere except goal
    while state != grid_size * grid_size - 1:
        # Epsilon-greedy action selection
        if random.uniform(0, 1) < epsilon:
            action_index = random.randint(0, len(actions) - 1)
        else:
            action_index = np.argmax(Q_table[state])

        action = actions[action_index]
        next_state = take_action(state, action)
        reward = reward_table[next_state]

        # Q-table update
        Q_table[state, action_index] += learning_rate * (
            reward + discount_factor * np.max(Q_table[next_state]) - Q_table[state, action_index]
        )

        state = next_state

# Print Q-table after training
print("Q-table after training:")
print(Q_table)

# Test: Show learned path
state = 0
path = [state]
while state != grid_size * grid_size - 1:
    render_grid(state)
    action_index = np.argmax(Q_table[state])
    state = take_action(state, actions[action_index])
    path.append(state)

render_grid(state)  # Show final state
print("Learned path:")
print(path)
