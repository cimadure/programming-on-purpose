#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  get_links.py
#  
#  Copyright 2018 user <user@plitor>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#  

import bs4
import requests
import pandas as pd


def extract_data(response, df):
    for i, link in enumerate(response.select('p a[href^="/tfn"]')):
        df.loc[i] = [link.getText(), link.get('href')]

def main(args):
    # res = requests.get("http://allevents.in/lahore/")
    # soup = bs4.BeautifulSoup(res.text)
    # for link in soup.select('a[property="schema:url"]'):
    #	print link.get('href')
    df = pd.DataFrame(columns=['text', 'href'])

    response = requests.get(
        "https://www.kiplinger.com/slideshow/investing/T052-S001-the-50-best-stocks-of-all-time/index.html")
    soup = bs4.BeautifulSoup(response.text)
    extract_data(response=soup, df=df)
    df.to_excel('50_stock_of_all_time.xlsx')

    df = pd.DataFrame(columns=['text', 'href'])
    response = requests.get(
        "https://www.kiplinger.com/slideshow/investing/T018-S001-53-best-dividend-stocks-for-2018-and-beyond/index.html")
    soup = bs4.BeautifulSoup(response.text)
    extract_data(response=soup, df=df)
    df.to_excel('50_stock_dividend.xlsx')

    #         'strong+ a'):  # 'strong+ a , #kip-slide3 p:nth-child(6)'  (get the first link in the 3th paragraph)
    #     # for link in soup.select('/p[(((count(preceding-sibling::*) + 1) = 6) and parent::*)]'):

    return 0


if __name__ == '__main__':
    import sys

    sys.exit(main(sys.argv))
