

def winner(teamA, teamB, scoreA, scoreB, handicap):
    if scoreA + handicap > scoreB:
        return teamA
    elif scoreA + handicap < scoreB:
        return teamB
    else:
        return None

def process(players, teams, match_data, bet_data, pond):
    winners = []
    winners.append(winner(match_data["teamA"],
                          match_data["teamB"],
                          match_data["scoreA"],
                          match_data["scoreB"],
                          match_data["HandicapA"]))
    winners.append(winner(match_data["teamA"],
                          match_data["teamB"],
                          match_data["scoreA"],
                          match_data["scoreB"],
                          match_data["HandicapB"]))
    for player in players:
        for winner_name in winners:
            if winner_name is not None:
                stack = match_data["weight"] / 2
                if bet_data[player] == winner_name:
                    players[player] += stack
                    if teams[winner_name] == player:
                        players[player] += stack
                        pond["sum"] -= stack
                else:
                    players[player] -= stack
