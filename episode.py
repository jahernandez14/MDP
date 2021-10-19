from state import State


class Episode:
  reward = 0
  currEpisode = {} 
  sequence = []
  actions = []
  rewards = []
  alpha = .5
  status = False
  stop = False
  learningRate = .99

  changes = []

  def __init__(self, episodeNum, prevEpisode, episode):
    self.episodeNumber = episodeNum
    self.prevEpisode = prevEpisode
    self.updatedEpisode = episode

  def iterate(self):
    self.sequence = []
    self.actions = []
    self.rewards = []
    state = "RU8p"

    while state != "end":
      self.sequence.append(state)
      self.prevEpisode[state].nextState()
      self.actions.append(self.prevEpisode[state].getAction())
      self.rewards.append(self.prevEpisode[state].getReward())
      state = str(self.prevEpisode[state].getNext())
      if state == "end":
        self.sequence.append(state)
  
  def monteCarloUpdate(self):

    for state in self.updatedEpisode:
      self.updatedEpisode[state].setValue(self.prevEpisode[state].getValue())
    
    total = self.getTotalReward()

    for state in self.sequence:
      if state == "end":
        return self.updatedEpisode
      self.updatedEpisode[state].monteCarlo(total)

    return self.updatedEpisode

  def qLearning(self):
    path = self.sequence

    for state in range(len(path)-2):
      val = self.prevEpisode[path[state]].qLearnFormula(self.alpha, self.prevEpisode[path[state+1]].getValue())
      
      if val - self.prevEpisode[path[state]].getValue() > .001:
        print("State:", self.prevEpisode[path[state]].getState(), "New Value:", val, "Old Value", self.prevEpisode[path[state]].getValue(), "Reward:",  self.prevEpisode[path[state+1]].getValue()) 
        self.prevEpisode[path[state]].setValue(val)

        if val - self.prevEpisode[path[state+1]].getValue() < .001:
          self.stop = True

    val = self.prevEpisode[path[len(path)-2]].qLearnFormula(self.alpha, 0)
    self.prevEpisode[path[len(path)-2]].setValue(val)
    print("State:", self.prevEpisode[path[len(path)-2]].getState(), "New Value:", val, "Old Value", self.prevEpisode[path[len(path)-2]].getValue(), "Reward:",  self.prevEpisode[path[len(path)-2]].getValue())

  def iterationUpdate(self):
    self.updatedEpisode = self.prevEpisode
    return self.updatedEpisode

  def valueIterateFormula(self, prob, reward, val):
    q = prob * (reward + self.learningRate * val)
    return q

  def valueIteration(self, actions):
    values = {}
    actionsMap = {}

    for action in actions:
      ans = []
      reward = actions[action]["reward"]
      probability = 1/len(actions)
      selectedState = actions[action]["next"]
      name = actions[action]["name"]

      if type(selectedState) is dict :
        for nestAction in selectedState:
          a = self.prevEpisode[selectedState[nestAction]].getValue()
          nestProb = probability/2
          values[selectedState[nestAction]] = self.valueIterateFormula(nestProb,reward, a)
          actionsMap[selectedState[nestAction]] = name
      else:
        if selectedState == "end":
          a = 0
          values[selectedState] = self.valueIterateFormula(probability,reward, a)
          actionsMap[selectedState] = name
          
        else:
          a = self.prevEpisode[selectedState].getValue()
          values[selectedState] = self.valueIterateFormula(probability,reward, a)
          actionsMap[selectedState] = name

    ans.append(max(values))
    ans.append(values[max(values)])
    ans.append(actionsMap[str(max(values))])

    return ans

  def valueIterate(self):
    self.changes = []
    for state in self.prevEpisode:
      actions = self.prevEpisode[state].getActions()
      maxNext = self.valueIteration(actions)

      if(maxNext[1] > self.prevEpisode[state].getValue()):
        actionOptions = ""
        for a in actions:
          actionOptions += f"{a} "

        self.changes.append(f"State:\t{self.prevEpisode[state].getState()}\tOld Value:\t{self.prevEpisode[state].getValue():.2f}\tNew Value:\t{maxNext[1]:.2f}\tActions Considered:\t{actionOptions}\tAction Selected:\t{maxNext[2]}")
        self.prevEpisode[state].setValue(maxNext[1])

  def getEpisodeNumber(self):
    return self.episodeNumber

  def getRewards(self):
    return self.rewards
  
  def getSequence(self):
    return self.sequence

  def getActions(self):
    return self.actions

  def getTotalReward(self):
    return sum(self.rewards)
  
  def getStatus(self):
    return 4
  
  def getChanges(self):
    return self.changes
  
  def setStatus(self,status):
    self.status = status

  def setAlpha(self, alpha):
    self.alpha = self.alpha * alpha 
  
  def getMap(self):
    return self.prevEpisode

  def getStop(self):
    return self.stop
