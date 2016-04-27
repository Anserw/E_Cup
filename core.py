

def winner(teamA, teamB, scoreA, scoreB, handicap):
    if scoreA + handicap > scoreB:
        return teamA
    elif scoreA + handicap < scoreB:
        return teamB
    else:
        return None


def betReward(bet_data, winner_name, players):
    correct_count = 0
    wrong_count = 0
    for player in bet_data:
        if player in players:
            if bet_data[player] == winner_name:
                correct_count += 1
            else:
                wrong_count += 1
    if correct_count == 0:
        return 0
    return float(float(wrong_count) / correct_count)


def process(players, teams, match_data, bet_data, pond):
    winners = list()
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
                correct_reward = betReward(bet_data, winner_name, players) * stack
                if match_data["scorer"] is not None:
                    scorer_reward = float(correct_reward * 0.05)
                    correct_reward -= scorer_reward
                if bet_data[player] == winner_name:
                    players[player] += correct_reward
                    players[match_data["scorer"]] += scorer_reward

                    if teams[winner_name] == player:
                        players[player] += correct_reward
                        pond["sum"] -= correct_reward + scorer_reward
                        players[match_data["scorer"]] += scorer_reward

                else:
                    players[player] -= stack
    print players
