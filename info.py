from state import State

class Info:
    def __init__(self):
        self.states = {
        "RU8p":{
        "name": "RU8p",
        "actions":{
        "P":{"name": "P","reward":2, "next": "TU10p"}, 
        "R":{"name": "R","reward":0, "next": "RU10p"},
        "S":{"name": "S","reward":-1, "next": "RD10p"}} 
        },
        "TU10p":{
        "name": "TU10P",
        "actions":{ 
        "P":{"name": "P","reward":2, "next": "RU10a"}, 
        "R":{"name": "R","reward":0, "next": "RU8a"}}
        },
        "RU10p":{
        "name": "RU10p",
        "actions":{
        "R":{"name": "R","reward":0, "next": "RU8a"},
        "S":{"name": "S","reward":-1, "next": "RD8a"},
        "P":{"name": "P","reward":2, "next": {"P1":"RU8a","P2":"RU10a"}}},
        },
        "RD10p":{
        "name": "RD10p",
        "actions":{
        "P":{"name": "P","reward":2, "next": {"P1":"RD8a","P2":"RD10a"}}, 
        "R":{"name": "R","reward":0, "next": "RU10p"}}
        },
        "RU8a":{
        "name": "RU8a",
        "actions":{
        "P":{"name": "P","reward":2, "next": "TU10a"}, 
        "R":{"name": "R","reward":0, "next": "RU10a"},
        "S":{"name": "S","reward":-1, "next": "RD10a"}}
        },
        "RD8a":{
        "name": "RD8a",
        "actions":{
        "P":{"name": "P","reward":2, "next": "TD10a"}, 
        "R":{"name": "R","reward":0, "next": "RD10a"}}
        },
        "TU10a":{
        "name": "TU10a",
        "actions":{
        "any":{"name": "any","reward":-1, "next": "end"}}
        },
        "RU10a":{
        "name": "RU10a",
        "actions":{
        "any":{"name": "any","reward":0, "next": "end"}}
        },
        "RD10a":{
        "name": "RD10a",
        "actions":{
        "any":{"name": "any","reward":4, "next": "end"}}
        },
        "TD10a":{
        "name": "TD10a",
        "actions":{
        "any":{"name": "any","reward":3, "next": "end"}}
        }}

    def getInfo(self):
        stateInfoMap = {}
        for a in self.states:
            stateInfoMap[a] = State(self.states[a]["name"], self.states[a]["actions"], 0)
        return stateInfoMap