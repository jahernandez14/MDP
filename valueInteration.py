from episode import Episode
from info import Info

info = Info()
stateMap = info.getInfo()
prevEpisode = stateMap

iterations = 0

print("\n**************************************** Value Iteration MDP ****************************************")
for episode in range(1,51):
    iterations = episode

print("Iterations Required: ", iterations)
print("\nFinal State Values")

for state in prevEpisode:
    print("State:", prevEpisode[state].getState(), f"\tValue: {prevEpisode[state].getValue():.2f}")

print("\nFinal Optimal Policy: ")