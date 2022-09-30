import requests
import sqlite3
from bs4 import BeautifulSoup
import re
import time

sqlite_select_name_query = """SELECT * from GEEK where Name = """
sqlite_delete_name_query = """DELETE from GEEK where Name = """
sqlite_select_all_query = """SELECT * from GEEK;"""
sqlite_insert_with_param = """INSERT INTO GEEK (Name, Price, OneHr, TwentyFourHr, SevenDay, MarketCap, Volume, CS) VALUES (?, ?, ?, ?, ?, ?, ?, ?)"""
sql_update_query = """Update GEEK SET Price = ?, OneHr = ?, TwentyFourHr = ?, SevenDay = ?, MarketCap = ?, Volume = ?, CS = ? where Name = ?"""

connection_obj = sqlite3.connect('geek.db')
cursor_obj = connection_obj.cursor()
cursor_obj.execute("DROP TABLE IF EXISTS GEEK")

table = """ CREATE TABLE GEEK (
            Name VARCHAR(255) NOT NULL,
            Price VARCHAR(255) NOT NULL,
            OneHr VARCHAR(255) NOT NULL,
            TwentyFourHr VARCHAR(255) NOT NULL,
            SevenDay VARCHAR(255) NOT NULL,
            MarketCap VARCHAR(255) NOT NULL,
            Volume VARCHAR(255) NOT NULL,
            CS VARCHAR(255) NOT NULL
        ); """
cursor_obj.execute(table)
cursor_obj.close()

while(True):
    html_doc = requests.get(url = 'https://coinmarketcap.com/')
    soup = BeautifulSoup(html_doc.text, 'html.parser')

    table = soup.find_all('table')[0]
    rows = table.find_all('tr')

    bigarr = []
    for each in rows:
        arr = []
        row = each.find_all('td')
        for every in row:
            if(every.get_text()):
                arr.append(every.get_text())
        # row = each.find_all('span')
        # for every in row:
        #     arr.append(every.get_text())

        if len(arr) == 9:
            # print(arr)
            match = re.match(r"([a-z]+)([0-9]+)", arr[1], re.I)
            if match:
                items = match.groups()
                arr[1] = items[0] 
            match = arr[6].split('$')
            arr[6] = '$' + match[1]
            # print(arr)
            bigarr.append(arr[1:])
    

    for each in bigarr:
        row = tuple(each)
        # print(tuple(each))

        connection_obj = sqlite3.connect('geek.db')
        cursor_obj = connection_obj.cursor()

        # first select
        a = sqlite_select_name_query + "'" + row[0] + "'"
        # print(a)
        cursor_obj.execute(a)
        records = cursor_obj.fetchall()
        # print(records)
        if (len(records) != 0):
            a = sqlite_delete_name_query + "'" + row[0] + "'"
            cursor_obj.execute(a)

        
            
        cursor_obj.execute(sqlite_insert_with_param, row)
        connection_obj.commit()
        cursor_obj.close()
        
        

    time.sleep(5)