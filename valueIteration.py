from episode import Episode
from info import Info

info = Info()
stateMap = info.getInfo()
prevEpisode = stateMap
status = 100
total = 0
iteration = 1
print("\n****************************************** Value Iteration MDP ******************************************")
while iteration < status:
    print("\n****************************************** Iternation", iteration,"******************************************")
    currEpisode = Episode(iteration, prevEpisode, stateMap)
    currEpisode.valueIterate()
    status = currEpisode.getStatus()
    changes = currEpisode.getChanges()
    for list in changes:
        print(list)
    iteration += 1
    # prevEpisode = currEpisode.iterationUpdate()

print("\n************************************ Value Iteration Statistics ************************************")
for state in prevEpisode:
    print("State:", prevEpisode[state].getState(), f"\tValue: {prevEpisode[state].getValue():.2f}")

# currEpisode.optimalPolicy()
# print(currEpisode.getPolicy())
