import random

class State:
  learningRate = .2
  reward = 0
  next = ""
  action = ""

  def __init__(self, state, actions, value):
    self.state = state
    self.actions = actions
    self.value = value

  def getState(self):
    return self.state
  
  def setValue(self, value):
    self.value = value
  
  def getActions(self):
    return self.actions

  def getAction(self):
    return self.action
  
  def getNext(self):
    return self.next

  def getValue(self):
    return self.value

  def getReward(self):
    return self.reward
  
  def monteCarlo(self, totalEpisodeReward):
    self.value = self.value + self.learningRate * (totalEpisodeReward - self.value)

  def valueIteration(self, prevEpisode):
        Q = {}

        for action, actionInfo in self.actions.items():
           reward = int(actionInfo['reward'])
           probability = 1/ len(self.action)
           name = str(actionInfo['name'])

           nextStateName = actionInfo['next']
           nextStateValue = prevEpisode[nextStateName].getValue()

           Q[name] = probability * (reward + (.99 * nextStateValue))
        
        actionMax = max(Q.values())

        if(self.value < actionMax): 
          print("Value Updated!")
          print("Previous Value: ", self.value)
          print("Updated Value: ", actionMax)

          print("Action Considerations: ", Q)

          for key in Q:
            if Q[key] == actionMax:
              print("Action Selected: ", key)

          self.setValue(actionMax)

  def probability(self):
    actions = self.actions
    rng = random.choice(list(actions.values()))
    self.reward = rng["reward"]
    self.action = rng["name"]

    if type(rng["next"]) is dict :
      rng2 = random.choice(list(rng["next"]))
      self.next = rng["next"][rng2]
    else:
      self.next = rng["next"]

  def nextState(self):
    self.probability()




