from game import SnakeGame, Point, Direction, BLOCK_SIZE
from collections import deque
import torch
import random
import numpy as np

from model import LinearQNet, QTrainer
from plot import plot

# Define constants
MAX_MEMORY = 100_000  # Maximum size of long term memory
BATCH_SIZE = 1_000    # Maximum number of steps to store in long term memory
LEARNING_RATE = 0.001
EPSILON_CONSTANT = 80  # Used to control randomness

INPUT_SIZE = 11
HIDDEN_SIZE = 256
OUTPUT_SIZE = 3


class Agent:
    def __init__(self):
        self.n_games = 0    # Number of games played
        self.epsilon = 0    # Control the randomness
        self.gamma = 0.9    # Discount rate, must be smaller than 1
        self.memory = deque(maxlen=MAX_MEMORY)  # Long term memory of steps
        
        self.model = LinearQNet(INPUT_SIZE, HIDDEN_SIZE, OUTPUT_SIZE)
        self.trainer = QTrainer(self.model, LEARNING_RATE, self.gamma)
        self.last_10_scores = [0] * 10

    def get_state(self, game):
        # TODO: Write some code
        pass

    def remember(self, state, action, reward, next_state, done):
        # TODO: Write some code
        pass

    def train_long_memory(self):
        # TODO: Write some code
        pass

    def train_short_memory(self, state, action, reward, next_state, done):
        # TODO: Write some code
        pass

    def get_action(self, state):
        # TODO: Write some code
        pass

    def _get_danger(self, danger_state, game, heading):
        # TODO: Write some code
        pass


def train():
    plot_score = []
    plot_mean = []
    plot_last_10 = []

    total_score = 0
    record_score = 0

    agent = Agent()
    game = SnakeGame(width=1080, height=800, fps=120)

    # Training loop
    while True:
        # TODO: Write some code
        pass
