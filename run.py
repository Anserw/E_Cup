import loader
import core
import time

def generate_markdown(players, pond, matches, teams, bets, filename="README.md"):
    md = u'''## E cup guess competition report
### real-time ranking
'''
    ISOTIMEFORMAT='%Y-%m-%d %X'
    md += "time: " + time.strftime( ISOTIMEFORMAT, time.localtime()) + '\n'

    md += "\n|rank|name|score|\n|:---:|:---:|:---:|\n"
    rank = 0
    for player_name in sorted(players, key=lambda p: players[p], reverse=True):
        rank += 1
        md += '|' + str(rank) + '|' + player_name + '|' + str(players[player_name]) + '|\n'

    md += "\n### Pond\n" + str(pond["sum"]) + '\n'

    md += "\n### History\n"
    for a_match in sorted(matches, cmp=lambda a, b: a["ID"] < b["ID"]):
        md += "\n#### - " + str(a_match["date"]) + ' ' + a_match["teamA"] + ' ' + str(a_match["scoreA"]) + \
              " : " + str(a_match["scoreB"]) + ' ' + a_match["teamB"] + '\n'

        if a_match["HandicapA"] == a_match["HandicapB"]:
            md += "handicap: " + str(a_match["HandicapA"]) + '\n'
        else:
            md += "handicap: " + str(a_match["HandicapA"]) + ' / ' + str(a_match["HandicapB"]) + '\n'
        md += "scorer: " + a_match["scorer"] + '\n'
        md += "\n|name|guess|score change|\n|:---:|:---:|:---:|\n"
        report = dict()
        pond_report = {"sum": 0}
        for player_name in players:
            report[player_name] = 0
        core.process(report, teams, a_match, bets[a_match["ID"]], pond_report)
        for player_name in report:
            md += '|' + player_name + '|' + bets[a_match["ID"]][player_name] + '|' + str(report[player_name]) + '|\n'
        md += '|' + "Pond" + '|' + '..' + '|' + str(pond_report["sum"]) + '|\n'



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
    generate_markdown(players, pond, matches, teams, bets)