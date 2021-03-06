import loader
import core
import time
import plot
import copy

def generate_markdown(players, players_stat, pond, matches, teams, bets, filename="README.md"):
    md = u'''# E cup guess competition report
## real-time ranking
'''
    ISOTIMEFORMAT='%Y-%m-%d %X'
    md += time.strftime( ISOTIMEFORMAT, time.localtime()) + '\n'

    md += "\n|rank|name|score|win|loss|\n|:---:|:---:|:---:|:---:|:---:|\n"
    rank = 0
    matches_sum = len(matches)
    for player_name in sorted(players, key=lambda p: players[p], reverse=True):
        rank += 1
        md += '|' + str(rank) + '|' + player_name + '|' + "%.2f" % players[player_name] + '|' \
            + "%.0f%%" % (players_stat[player_name]["win"] / matches_sum * 100) + '|' \
            + "%.0f%%" % (players_stat[player_name]["loss"] / matches_sum * 100) + '|\n'

    md += "\n## Pond\n" + "%.2f" % pond["sum"] + '\n'

    md += "\n## History\n"

    md += "![image](https://github.com/Anserw/E_Cup/blob/master/plot.jpg)"

    for a_match in sorted(matches, cmp=lambda a, b: cmp(a["date"], b["date"]), reverse=True):
        if a_match["weight"] > 0:
            md += "\n### " + str(a_match["date"]) + ' ' + a_match["teamA"] + ' ' + str(a_match["scoreA"]) + \
                  " : " + str(a_match["scoreB"]) + ' ' + a_match["teamB"] + '\n'

            if a_match["HandicapA"] == a_match["HandicapB"]:
                md += "- handicap: " + str(a_match["HandicapA"]) + '\n'
            else:
                md += "- handicap: " + str(a_match["HandicapA"]) + ' / ' + str(a_match["HandicapB"]) + '\n'
            md += "- scorer: " + a_match["scorer"] + '\n'
            md += "- owners:\n"
            md += " - " + a_match["teamA"] + ": "
            for a_team in teams:
                if a_team == a_match["teamA"]:
                    md += teams[a_team] + "\n"
            md += " - " + a_match["teamB"] + ": "
            for a_team in teams:
                if a_team == a_match["teamB"]:
                    md += teams[a_team] + "\n\n"
            md += "\n|name|guess|score change|\n|:---:|:---:|:---:|\n"
            report = dict()
            pond_report = {"sum": 0}
            for player_name in players:
                report[player_name] = 0
            core.process(report, teams, a_match, bets[a_match["ID"]], pond_report)
            for player_name in report:
                md += '|' + player_name + '|' + bets[a_match["ID"]][player_name] + '|' + "%.2f" % report[player_name] + '|\n'
            md += '|' + "Pond" + '|' + '..' + '|' + "%.2f" % pond_report["sum"] + '|\n'

    f = open(filename, 'w')
    f.write(md)
    f.close()


if __name__ == "__main__":
    players = loader.loadPlayers()
    teams = loader.loadTeam()
    matches = loader.loadMatch()
    bets = loader.loadBet()
    pond = loader.loadPond()
    players_stat = copy.deepcopy(players)
    for a_player in players_stat:
        players_stat[a_player] = {"win": 0.0, "loss": 0.0}
    # reports = dict()
    for a_match in matches:
        core.process(players, teams, a_match, bets[a_match["ID"]], pond, players_stat)
        # report = dict()
        # pond_report = {"sum": 0}
        # for player_name in players:
        #     report[player_name] = 0
        # core.process(report, teams, a_match, bets[a_match["ID"]], pond_report)
        # report["ID"] = a_match["ID"]
        # report["pond"] = pond_report["sum"]
        # reports["ID"] = report
    # print "result", players
    # print "report", report
    try:
        plot.generate_plot(players, pond, matches, teams, bets)
    except:
        print "Error: cannot draw a plot!"
    generate_markdown(players, players_stat, pond, matches, teams, bets)
    print "all done."


