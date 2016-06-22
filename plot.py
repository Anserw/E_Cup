from matplotlib.pyplot import savefig
import pylab as pl
import core


def generate_plot(players, pond, matches, teams, bets):
    report = dict()
    player_score_list = dict()
    for player_name in players:
        report[player_name] = 0
        player_score_list[player_name] = [0]
    for a_match in sorted(matches, cmp=lambda a, b: cmp(a["date"], b["date"]), reverse=False):
        if a_match["weight"] > 0:
            pond_report = {"sum": 0}
            core.process(report, teams, a_match, bets[a_match["ID"]], pond_report)
            for player_name in players:
                player_score_list[player_name].append(report[player_name])
    player_plot_list = []
    style_list = ['b->', 'y-d', 'k-x', 'm-o', 'c-^', 'r-1', 'g-s', 'b-p']
    for player_name in players:
        player_plot_list.append(pl.plot(
                                    range(len(player_score_list[player_name])),
                                    player_score_list[player_name],
                                    style_list.pop(),
                                    label=player_name
                                ))

    pl.xlabel('x axis')# make axis labels
    pl.ylabel('y axis')
    pl.legend(loc=2, fontsize='10')
    savefig("plot.jpg")
    # pl.show()