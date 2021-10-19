from episode import Episode
from info import Info
'''
Julio A Hernandez
Alex Vasquez
'''
info = Info()
stateMap = info.getInfo()
prevEpisode = stateMap
status = False
episode = 1
total = 0

print("\n****************************************** Q learning MDP ******************************************")
while status is False:
    currEpisode = Episode(episode, prevEpisode, stateMap)
    print("\n********************************************* Episode",currEpisode.getEpisodeNumber(),"*********************************************")
    currEpisode.iterate()
    currEpisode.qLearning()
    currEpisode.setAlpha(.995)
    status = currEpisode.getStop()
    episode += 1



    # total += currEpisode.getTotalReward()
    prevEpisode = currEpisode.getMap()

    # print("State Actions:\t", currEpisode.getActions())
    # print("State Rewards:\t", currEpisode.getRewards())
    # print("Total Rewards:\t", currEpisode.getTotalReward())

print("\n************************************ Q Learning Statistics ************************************")
for state in prevEpisode:
    print("State:", prevEpisode[state].getState(), f"\tQ Value: {prevEpisode[state].getValue():.2f}")
print("\nEpisodes Required:", currEpisode.getEpisodeNumber())
print("Optimal Policy:\t", currEpisode.getSequence())

