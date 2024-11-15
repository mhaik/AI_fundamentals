# Programs for uni subject: AI Fundamentals

This repository contains my implementations for tasks assigned in the **AI Fundamentals** course. These tasks involve data generation, machine learning models, neural networks, and game-based AI using Python and Streamlit, among other libraries.

---

## Table of Contents

- [Overview](#overview)
- [Tasks](#tasks)
  - [Task 4.1: Data Generator and Visualizer](#task-41-data-generator-and-visualizer)
  - [Task 4.2: Single Neuron Implementation](#task-42-single-neuron-implementation)
  - [Task 4.3: Shallow Neural Network](#task-43-shallow-neural-network)
  - [Task 4.4: Search Algorithms](#task-44-search-algorithms)
  - [Task 4.5: Fuzzy Control for Pong Game](#task-45-fuzzy-control-for-pong-game)
- [Technologies Used](#technologies-used)
- [Installation](#installation)
- [Usage](#usage)
- [Acknowledgements](#acknowledgements)

---

## Overview

This project demonstrates fundamental AI concepts through practical tasks. These tasks encompass data visualization, training machine learning models, neural network backpropagation, implementing search algorithms, and designing a fuzzy logic controller for a game. The implementations prioritize GUI-based interactivity and visualization using Python tools.

---

## Tasks

### Task 4.1: Data Generator and Visualizer

- **Objective:** Create a GUI to generate and visualize 2D data samples from two classes.  
- **Features:**
  - Generate Gaussian-distributed data samples.
  - Configure the number of modes per class and samples per mode.
  - Visualize samples in a 2D plot, colored by class labels.
  - Implemented using **Streamlit** for an interactive interface.

---

### Task 4.2: Single Neuron Implementation

- **Objective:** Implement a trainable artificial neuron that predicts class membership.
- **Features:**
  - Supports multiple activation functions:
    - Heaviside (Step Function)
    - Logistic (Sigmoid)
    - Sin, Tanh, Sign, ReLU, and Leaky ReLU
  - Training using gradient descent.
  - Visualize decision boundaries in the GUI.

---

### Task 4.3: Shallow Neural Network

- **Objective:** Build a shallow (up to 5 layers) fully connected neural network.
- **Features:**
  - Configurable number of layers and neurons per layer.
  - Logistic activation function for training and evaluation (with options for more functions).
  - Visualize decision boundaries on a 2D plot.
  - Training via backpropagation.

---

### Task 4.4: Search Algorithms

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

### Task 4.5: Fuzzy Control for Pong Game

- **Objective:** Implement a fuzzy logic controller for controlling a paddle in a simplified Pong game.
- **Features:**
  - Designed using **scikit-fuzzy**.
  - Mamdami and TSK methods for rule evaluation.
  - Complex ruleset for edge deflection to increase ball speed.
  - Ensures the paddle accurately follows and deflects the ball.

---

## Technologies Used

- **Programming Language:** Python
- **Libraries:**  
  - Data & Visualization: `numpy`, `matplotlib`, `scikit-fuzzy`, `streamlit`, `plotly`
  - GUI: `streamlit`, `PyGame`
  - Neural Networks: Custom implementations, `numpy`

---

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/ai-fundamentals.git
   cd ai-fundamentals
