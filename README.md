# 🐍 Snake-RL: Reinforcement Learning Snake Game

Welcome to **Snake-RL**, a classic Snake game powered by **Reinforcement Learning (RL)**! This project demonstrates how an AI agent can learn to master the game of Snake using popular RL techniques such as **Q-Learning** or **Deep Q-Networks (DQN)**.

## 🎯 Project Goals

- Implement a classic Snake game from scratch
- Train an AI agent using Reinforcement Learning
- Visualize the learning progress and gameplay
- Provide configurable training and inference modes

## 🧠 Technologies Used

- **Python 3.8+**
- **Pygame** – for game visualization
- **NumPy / PyTorch / TensorFlow** – for reinforcement learning logic (based on your implementation)
- **Matplotlib** – for plotting training metrics

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/yourusername/snake-rl.git
cd snake-rl
```
📈 Metrics Tracked
- Total reward per episode

- Episode length

- Epsilon over time

- Average score in last N episodes

📚 RL Techniques Used
Q-Learning (Tabular) – for small state spaces

Deep Q-Learning (DQN) – with replay buffer and target network

Epsilon-greedy – exploration strategy

Reward Shaping – bonus points for eating food, penalties for dying

🧑‍💻 Author
Made by heubert-69

📄 License
This project is licensed under the MIT License. See LICENSE file for details.
