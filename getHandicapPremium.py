# -*- coding: utf-8 -*-

import requests
import re


def getHandicapPage(url = 'http://odds.sports.sina.com.cn/odds'):
    r = requests.get(url)
    r.encoding = 'GBK'
    return r.text

def parseMatchdata(page, league_filter):
    result = list()
    res_table = r'<caption>(.*?)</tbody></table>'
    m_table = re.findall(res_table,page,re.S|re.M)
    for line in m_table:
        res_date = r'^(.*?)</caption>'
        m_date = re.findall(res_date,line,re.S|re.M)
        res_matchtable = r'<tr><td style=(.*?)</td><td><a'
        m_matchtable = re.findall(res_matchtable,line,re.S|re.M)
        for matchtable in m_matchtable:
            matchinfo = [m_date[0]]
            league = re.findall(r'FFFFFF">(.*?)</strong>',matchtable,re.S|re.M)[0]
            if league == league_filter:
                m_matchinfo = re.findall('<td>(.*?)(</strong>&nbsp|&nbsp|$)', matchtable, re.S|re.M)
                team_str = m_matchinfo[1][0]
                matchinfo.append(re.findall('</span>(.*?)(vs|</b></td>)', team_str, re.S | re.M)[0][0])
                matchinfo.append(re.findall('</span>(.*?)(vs|</b></td>)', team_str, re.S | re.M)[1][0])
                m_matchinfo = m_matchinfo[2:]
                for stat in m_matchinfo:
                    matchinfo.append(stat[0])
                if matchinfo[-1] == "":
                    return result
                result.append(matchinfo)
    return result

if __name__ == "__main__":
    ## print match data that
    ## Match Date, Team A, Team B, Premium A, Handicap, Premium B, ...
    print(parseMatchdata(getHandicapPage(), '英超'))
