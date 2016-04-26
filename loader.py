import json
import os

def loadJson(filename):
    return json.load(open(filename))

def loadJsonsFromDir(dir):
    filelist = os.listdir(dir)
    ret = []
    for filename in filelist:
        try:
            ret.append(loadJson(dir + '/' + filename))
        except:
            print filename + " is not a json data!"
    return ret


def loadPlayers(filename="players.json"):
    return loadJson(filename)

def loadTeam(filename="team.json"):
    return loadJson(filename)

def loadMatch(dir="match_data"):
    return loadJsonsFromDir(dir)

def loadBet(dir="bet_data"):
    ret = dict()
    bets_data = loadJsonsFromDir(dir)
    for a_bet in bets_data:
        ret[a_bet["ID"]] = a_bet
    return ret


if __name__ == "__main__":
    print loadPlayers()
    print loadTeam()
    print loadMatch()
    print loadBet()