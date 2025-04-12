# Programs for uni subject: AI Fundamentals

This repository contains my implementations for tasks assigned in the **AI Fundamentals** course.
All programs are written in Python with some libraries, main GUI tool was Streamlit.

### Task 1: Data Generator and Visualizer

- **Objective:** Create a GUI to generate and visualize 2D data samples from two classes.  
- **Features:**
  - Generate Gaussian-distributed data samples.
  - Configure the number of modes per class and samples per mode.
  - Visualize samples in a 2D plot, colored by class labels.
  - Implemented using **Streamlit** for an interactive interface.

---

### Task 2: Single Neuron Implementation

- **Objective:** Implement a trainable artificial neuron that predicts class membership.
- **Features:**
  - Supports multiple activation functions:
    - Heaviside (Step Function)
    - Logistic (Sigmoid)
    - Sin, Tanh, Sign, ReLU, and Leaky ReLU
  - Training using gradient descent.
  - Visualize decision boundaries in the GUI.

---

### Task 3: Shallow Neural Network

- **Objective:** Build a shallow (up to 5 layers) fully connected neural network.
- **Features:**
  - Configurable number of layers and neurons per layer.
  - Logistic activation function for training and evaluation (with options for more functions).
  - Visualize decision boundaries on a 2D plot.
  - Training via backpropagation.

---

### Task 4: Search Algorithms

- **Objective:** Implement search algorithms for a modified **Snake** game.  
- **Features:**
  - Implemented algorithms:
    - Breadth-First Search (BFS)
    - Depth-First Search (DFS)
    - Dijkstra’s Algorithm
    - A* Algorithm
  - Avoid penalty tiles while generating paths to the fruit.
  - Visualize visited nodes during search.

---

### Task 5: Fuzzy Control for Pong Game

- **Objective:** Implement a fuzzy logic controller for controlling a paddle in a simplified Pong game.
- **Features:**
  - Designed using **scikit-fuzzy**.
  - Mamdami method for rule evaluation.
  - Complex ruleset for edge deflection to increase ball speed.
  - Ensures the paddle accurately follows and deflects the ball.

