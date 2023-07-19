import gymnasium as gym, time
import numpy as np
import matplotlib.pyplot as plt
from dqn import Agent
from utils import plotLearning
from env import EV_Env

if __name__ == '__main__':
    env = EV_Env()
    num_games = 300

    agent = Agent(gamma=0.99, epsilon=1.0, lr=5e-4,
                  input_dims=[6], n_actions=4, max_mem_size=100000, eps_end=0.01,
                  batch_size=64, eps_dec=1e-2)

    filename = 'training.png'
    scores = []
    eps_history = []
    n_steps = 0

    for i in range(num_games):
        done = False
        observation = env.reset()
        score = 0

        while not done:
            action = agent.choose_action(observation)
            observation_, reward, done, info = env.step(action)
            n_steps += 1
            score += reward
            agent.store_transition(observation, action,
                                    reward, observation_, int(done))
            agent.learn()

            observation = observation_


        scores.append(score)
        avg_score = np.mean(scores[max(0, i-100):(i+1)])
        print('episode: ', i,'score %.1f ' % score,
             ' average score %.1f' % avg_score,
            'epsilon %.2f' % agent.epsilon)
        #if i > 0 and i % 10 == 0:
        #    agent.save_models()

        eps_history.append(agent.epsilon)

    x = [i+1 for i in range(num_games)]
    plotLearning(x, scores, eps_history, filename)