class Episode:
  reward = 0
  currEpisode = {} 
  sequence = []
  actions = []
  rewards = []

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
 
  def valueIterationUpdate(self):
        
        print("yes")

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

