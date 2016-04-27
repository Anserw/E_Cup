import loader
import core


if __name__ == "__main__":
    players = loader.loadPlayers()
    teams = loader.loadTeam()
    matches = loader.loadMatch()
    bets = loader.loadBet()
    pond = loader.loadPond()
    for a_match in matches:
        core.process(players, teams, a_match, bets[a_match["ID"]], pond)
    print players
    print pond