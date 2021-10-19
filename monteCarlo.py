from episode import Episode
from info import Info
'''
Julio A Hernandez
Alex Vasquez
'''
info = Info()
stateMap = info.getInfo()
prevEpisode = stateMap

total = 0

print("\n****************************************** Monte Carlo MDP ******************************************")
for episode in range(1,51):
    currEpisode = Episode(episode, prevEpisode, stateMap)
    print("\n********************************************* Episode",currEpisode.getEpisodeNumber(),"*********************************************")
    currEpisode.iterate()
    total += currEpisode.getTotalReward()
    prevEpisode = currEpisode.monteCarloUpdate()

    print("State Sequence:\t", currEpisode.getSequence())
    print("State Actions:\t", currEpisode.getActions())
    print("State Rewards:\t", currEpisode.getRewards())
    print("Total Rewards:\t", currEpisode.getTotalReward())

print("\n************************************ Total Monte Carlo Statistics ************************************")
for state in prevEpisode:
    print("State:", prevEpisode[state].getState(), f"\tValue: {prevEpisode[state].getValue():.2f}")
print("\nAverage Episode Reward:\t", total/50)
