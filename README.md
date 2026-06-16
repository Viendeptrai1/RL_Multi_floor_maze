# RL Multi-Floor Maze

A project for simulating and training an AI agent to navigate a multi-floor maze environment using Reinforcement Learning algorithms. The agent must learn how to reach the destination, avoid traps, collect resources such as health and ammunition, and deal with enemies.

---

## Project Features

The current project includes the following main components:

### 1. Multi-Floor Maze Environment (Gymnasium)

* Simulates a 2D/3D grid-based maze consisting of multiple floors connected by staircases.
* Includes survival-related mechanics such as Health Points (HP), ammunition, stamina, and a noise-based stealth system.
* Features different enemy types:

  * **Patrol**: Moves along predefined patrol routes.
  * **Chaser**: Actively tracks and pursues the agent.
  * **Sniper**: Attacks the agent from a distance.
* Supports visual rendering of the entire maze and all entities within the environment.

### 2. Reinforcement Learning Training

* Built using the `stable-baselines3` library.
* Implements and customizes the following algorithms:

  * **PPO**
  * **A2C**
  * **DQN**
* Uses Curriculum Learning across nine difficulty levels, ranging from **Crawl**, the easiest level, to **Master**, the most challenging level.

### 3. Project Files

* `Multi_Floor_Maze.ipynb`: Contains the complete source code for the environment simulation, CNN-based feature extraction, and the agent training pipeline.
* `Multi_Floor_Maze.json`: A backup of the original project structure in Zeppelin Notebook format.

---

## Installation and Usage

### System Requirements

Install the required dependencies using:

```bash
pip install gymnasium numpy torch stable-baselines3 Pillow
```

### How to Run

1. Install Apache Zeppelin version `0.8.2`.
2. Import the `Multi_Floor_Maze.json` file into Zeppelin.
3. Install the required libraries.
4. Run all notebook cells in order by following the instructions provided in the imported notebook.
