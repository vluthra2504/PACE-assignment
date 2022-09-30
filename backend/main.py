from flask import Flask
from flask_cors import CORS
import random
import requests
import sqlite3
from bs4 import BeautifulSoup
import re
import time
import os

app = Flask(__name__)
CORS(app)

sqlite_select_name_query = """SELECT * from GEEK where Name = ?;"""
sqlite_select_all_query = """SELECT * from GEEK;"""
sqlite_insert_with_param = """INSERT INTO GEEK (Name, Price, OneHr, TwentyFourHr, SevenDay, MarketCap, Volume, CS) VALUES (?, ?, ?, ?, ?, ?, ?, ?)"""
sql_update_query = """Update GEEK SET Price = ?, OneHr = ?, TwentyFourHr = ?, SevenDay = ?, MarketCap = ?, Volume = ?, CS = ? where Name = ?"""

# cursor_obj.close()
# def set

@app.route('/api/v1/data')
def get_data():
    connection_obj = sqlite3.connect('geek.db')
    cursor_obj = connection_obj.cursor()
    cursor_obj.execute(sqlite_select_all_query)
    records = cursor_obj.fetchall()
    # for each in records:
    #     print(each)
    cursor_obj.close()
    return records

if __name__ == "__main__":
    # os.system('python3 data_fetcher.py &')
    app.run(debug=True, port=5004)