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
      if action == 'any': # Exit
            return

      reward = int(actionInfo['reward'])  #reward for taking action
      probability = 1/ len(actionInfo)  #probability of taking action
      nextStateName = actionInfo['next']  #state transitioned to as result of action

      if isinstance(nextStateName, str):
        nextStateValue = prevEpisode[nextStateName].getValue()
        name = str(actionInfo['name'])

        Q[name] = probability * (reward + (.99 * nextStateValue)) # Append to options

      elif isinstance(nextStateName, dict):
        for nestedAction, nestedActionInfo in nextStateName.items(): #check actions in nested dictionary
          nextStateName = nestedActionInfo
          nextStateValue = prevEpisode[nextStateName].getValue() # Get value of state
          name = nestedAction

          Q[name] = round(probability * (reward + (.99 * nextStateValue)), 4) # Append to options
        
    actionMax = max(Q.values()) # Take max of options
    
    if(self.value < actionMax and (actionMax - self.value) > .001):  #update value
      print("Value Updated!")
      print("Previous Value: ", round(self.value, 4))
      self.setValue(actionMax)
      print("Updated Value: ", round(self.value,4))

      print("Action Considerations: ", Q)

      for key in Q:
        if Q[key] == actionMax:
          print("Action Selected: ", key)
          break 
          
    elif (actionMax - self.value) < .001 : # not large enough change
      print("Change less than .001 at state")
      return
      
      

    print("-------------------------------------")

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




