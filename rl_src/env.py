from gymnasium import Env
from gymnasium.spaces import Discrete, Box
import numpy as np
import random

class EV_Env(Env):
    def __init__(self):
        self.action_space = Discrete(3)
        self.observation_space = Box(low=np.array([0]), high=np.array([100]))
        self.state = [random.uniform(30.0, 60.0), random.uniform(990.0, 1150.0), random.uniform(20.0, 40.0),
                      random.uniform(20, 90), random.uniform(500, 900), random.uniform(20, 90)]
        self.steps = 100
        self.alpha = 0.2
        self.beta = -0.6
        self.gamma = 0.2
        
    def step(self, action):
        if action == 0:
            self.state[5] = 1.05*self.state[5]
        elif action == 1:
            self.state[5] = 0.95*self.state[5]
        elif action == 2:
            self.state[2] = 0.75*self.state[5]
        elif action == 3:
            self.state[2] = 1.05*self.state[5]

        reward = 7 * (self.alpha * self.state[4] + self.beta * self.state[2] + self.gamma * self.state[5])

        if self.steps <= 0: 
            done = True
        else:
            done = False
        
        info = {}
        self.steps -= self.steps
        return self.state, reward, done, info

    def reset(self):
        self.state = [random.uniform(30.0, 60.0), random.uniform(990.0, 1150.0), random.uniform(20.0, 40.0),
                      random.uniform(20, 90), random.uniform(500, 900), random.uniform(20, 90)]
        self.steps = 100
        return self.state