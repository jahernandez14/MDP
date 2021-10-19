from episode import Episode
from info import Info

info = Info()
stateMap = info.getInfo()
prevEpisode = stateMap

iterations = 1
status = False
print("\n**************************************** Value Iteration MDP ****************************************")
while status == False:
    print("\n**************************************** Iteration", iterations,"****************************************")

    currentEpisode = Episode(iterations, prevEpisode, stateMap)
    prevEpisode = currentEpisode.valueIterationUpdate()
    status = currentEpisode.getStatus()
    iterations += 1



    # probability * (reward + .99 * nextState Value)
    # 1 *(1 + .99 * 0)
    
    # iterations = episode

# print("Iterations Required: ", iterations)
# print("\nFinal State Values")

# for state in prevEpisode:
#     print("State:", prevEpisode[state].getState(), f"\tValue: {prevEpisode[state].getValue():.2f}")

# print("\nFinal Optimal Policy: ")
