import os
import json
import loader

def generate_default_match_data(teamA, teamB, date, time, handicap1, handicap2, players):
    ID = date + teamA + teamB
    a_match_data = dict()
    a_bet_data = dict()
    filelist = os.listdir("match_data")
    if not ID + ".json" in filelist:
        a_match_data["ID"] = ID
        a_match_data["teamA"] = teamA
        a_match_data["teamB"] = teamB
        a_match_data["date"] = date + time
        a_match_data["HandicapA"] = handicap1
        a_match_data["HandicapB"] = handicap2
        a_match_data["scoreA"] = 0
        a_match_data["scoreB"] = 0
        a_match_data["weight"] = 0
        a_match_data["scorer"] = "laotao"
        f = open("match_data/"+ID+".json", "w")
        json.dump(a_match_data, f, indent=4, sort_keys=True)
    filelist = os.listdir("bet_data")
    if not ID + "_bet.json" in filelist:
        a_bet_data["ID"] = ID
        for a_player in players:
            a_bet_data[a_player] = teamA
        f = open("bet_data/"+ID+"_bet.json", "w")
        json.dump(a_bet_data, f, indent=4, sort_keys=True)


if __name__ == "__main__":
    teamA = "France"
    teamB = "Portugal"
    date = "20160711"
    time = "03"
    handicap1 = -0.5
    handicap2 = -0.5
    players = loader.loadPlayers()
    generate_default_match_data(teamA, teamB, date, time, handicap1, handicap2, players)

# "France":"laotao",
# "Romania":"laopai",
# "Albania":"mother",
# "Switzerland":"laotao",
# "England":"mother",
# "Russia":"dazuan",
# "Slovakia":"laopai",
# "Welsh":"xiaobai",
# "Germany":"dazuan",
# "Ukraine":"dazuan",
# "Poland":"xiaobai",
# "NorthernIreland":"laopai",
# "Spain":"lc",
# "Czech":"lc",
# "Turkey":"laopai",
# "Croatia":"mother",
# "Belgium":"lc",
# "Italy":"xiaobai",
# "Ireland":"laopai",
# "Sweden":"wan",
# "Portugal":"laoda",
# "Iceland":"xiaobai",
# "Austria":"laopai",
# "Hungary":"laotao"