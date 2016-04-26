import loader
import core


if __name__ == "__main__":
    players = loader.loadPlayers()
    teams = loader.loadTeam()
    matches = loader.loadMatch()
    bets = loader.loadBet()
    for a_match in matches:
        core.process(players, teams, a_match, bets[a_match["ID"]])
    print players