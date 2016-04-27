import loader
import core
import time

def generate_markdown(players, filename="README_test.md"):
    md = u'''## E cup guess competition report
### real-time ranking
'''
    ISOTIMEFORMAT='%Y-%m-%d %X'
    md += "time: " + time.strftime( ISOTIMEFORMAT, time.localtime()) + '\n'

    md += "|rank|name|score|\n|:---:|:---:|:---:|\n"
    rank = 0
    for player_name in sorted(players, key=lambda p: players[p], reverse=True):
        rank += 1
        md += '|' + str(rank) + '|' + player_name + '|' + str(players[player_name]) + '|\n'


    f = open(filename, 'w')
    f.write(md)
    f.close()


if __name__ == "__main__":
    players = loader.loadPlayers()
    teams = loader.loadTeam()
    matches = loader.loadMatch()
    bets = loader.loadBet()
    pond = loader.loadPond()
    reports = dict()
    for a_match in matches:
        core.process(players, teams, a_match, bets[a_match["ID"]], pond)
        report = dict()
        pond_report = {"sum": 0}
        for player_name in players:
            report[player_name] = 0
        core.process(report, teams, a_match, bets[a_match["ID"]], pond_report)
        report["ID"] = a_match["ID"]
        report["pond"] = pond_report["sum"]
        reports["ID"] = report
    print "result", players
    print "report", report
    generate_markdown(players)