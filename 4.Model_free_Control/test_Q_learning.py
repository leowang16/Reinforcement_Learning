from Q_learning import *
import matplotlib.pyplot as plt
import numpy as np

if __name__ == "__main__":
    plt.close("all")
    max_Q_Q1, reward_Q1 = QLearning(1000, alpha=[0, 1])
    max_Q_Double_Q1, reward_Double_Q1 = Double_QLearning(1000, alpha=[0, 1])

    plt.figure(1)
    plt.plot(max_Q_Q1, label='QLearning')
    plt.plot(max_Q_Double_Q1, label='Double_QLearning')
    plt.legend(loc='best')
    plt.xlabel('Iterations')
    plt.title('One experiment: Max. Q')

    plt.figure(2)
    plt.plot(reward_Q1, label='QLearning')
    plt.plot(reward_Double_Q1, label='Double_QLearning')
    plt.legend(loc='best')
    plt.xlabel('Iterations')
    plt.title('One experiment: Reward')

    max_Q_Q2, reward_Q2 = QLearning(1000, alpha=[0, 1])
    max_Q_Double_Q2, reward_Double_Q2 = Double_QLearning(1000, alpha=[0, 1])

    plt.figure(3)
    plt.plot(max_Q_Q2, label='QLearning')
    plt.plot(max_Q_Double_Q2, label='Double_QLearning')
    plt.legend(loc='best')
    plt.xlabel('Iterations')
    plt.title('One experiment: Max. Q')

    plt.figure(4)
    plt.plot(reward_Q2, label='QLearning')
    plt.plot(reward_Double_Q2, label='Double_QLearning')
    plt.legend(loc='best')
    plt.xlabel('Iterations')
    plt.title('One experiment: Reward')

##########################################################################
    avg_times = 50
    iterations = 10000
    alphas = [[0, 1], [0, 0.5]]

    for i_alpha in xrange(len(alphas)):
        print 'alpha = : ', alphas[i_alpha]
        max_Q_Q2 = np.zeros((avg_times, iterations))
        reward_Q2 = np.zeros((avg_times, iterations))
        max_Q_Double_Q2 = np.zeros((avg_times, iterations))
        reward_Double_Q2 = np.zeros((avg_times, iterations))
        for i in xrange(avg_times):
            print 'avg_time: %d' % (i + 1)
            max_Q_Q2[i, :], reward_Q2[i, :] = QLearning(
                iterations, alpha=alphas[i_alpha])
            max_Q_Double_Q2[i, :], reward_Double_Q2[
                i, :] = Double_QLearning(iterations, alpha=alphas[i_alpha])

        avg_max_Q_Q2 = np.mean(max_Q_Q2, axis=0)
        avg_reward_Q2 = np.mean(reward_Q2, axis=0)

        avg_max_Q_Double_Q2 = np.mean(max_Q_Double_Q2, axis=0)
        avg_reward_Double_Q2 = np.mean(reward_Double_Q2, axis=0)

        plt.figure(3)
        plt.subplot(1, 2, (i_alpha + 1))
        plt.plot(avg_max_Q_Q2, label='QLearning')
        plt.plot(avg_max_Q_Double_Q2, label='Double_QLearning')
        plt.legend(loc='best')
        plt.xlabel('Iterations')
        plt.title('%d experiments: Average of Max. Q @ alpha:' %
                  avg_times + str(alphas[i_alpha]))

        plt.figure(4)
        plt.subplot(1, 2, (i_alpha + 1))
        plt.plot(avg_reward_Q2, label='QLearning')
        plt.plot(avg_reward_Double_Q2, label='Double_QLearning')
        plt.legend(loc='best')
        plt.xlabel('Iterations')
        plt.title('%d experiments: Average Reward @ alpha:' %
                  avg_times + str(alphas[i_alpha]))

    plt.show()
