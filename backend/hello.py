from flask import Flask
from flask_cors import CORS
import random
import requests
import sqlite3
from bs4 import BeautifulSoup

soup = BeautifulSoup(html_doc, 'html.parser')


# app = Flask(__name__)
# CORS(app)

# # connection_obj = sqlite3.connect('geek.db')
# # cursor_obj = connection_obj.cursor()
# # cursor_obj.execute("DROP TABLE IF EXISTS GEEK")

# # table = """ CREATE TABLE GEEK (
# #             Name VARCHAR(255) NOT NULL,
# #             Price VARCHAR(255) NOT NULL,
# #             OneHr VARCHAR(255) NOT NULL,
# #             TwentyFourHr VARCHAR(255) NOT NULL,
# #             SevenDay VARCHAR(255) NOT NULL,
# #             MarketCap VARCHAR(255) NOT NULL,
# #             Volume VARCHAR(255) NOT NULL,
# #             CS VARCHAR(255) NOT NULL
# #         ); """
# # cursor_obj.execute(table)

# sqlite_select_query = """SELECT Name from GEEK;"""
# sqlite_select_all_query = """SELECT * from GEEK;"""
# sqlite_insert_with_param = """INSERT INTO GEEK (Name, Price, OneHr, TwentyFourHr, SevenDay, MarketCap, Volume, CS) VALUES (?, ?, ?, ?, ?, ?, ?, ?)"""
# sql_update_query = """Update GEEK SET Price = ?, OneHr = ?, TwentyFourHr = ?, SevenDay = ?, MarketCap = ?, Volume = ?, CS = ? where Name = ?"""

# # cursor_obj.close()
# # def set


# @app.route('/insert_once')
# def hello():
#     connection_obj = sqlite3.connect('geek.db')
#     cursor_obj = connection_obj.cursor()

#     # first select
#     cursor_obj.execute(sqlite_select_query)
#     records = cursor_obj.fetchall()
#     print(records[0][0])
#     if (len(records) == 0):
#         cursor_obj.execute(sqlite_insert_with_param, ("ABV", "DEF",
#                            "GHI", "GDFH", "SHGSFH", "SDHH", "SRHSFH", "SHSH"))
#     else:
#         cursor_obj.execute(sql_update_query, ("qwe",
#                            "GHI", "GDFH", "SHGSFH", "SDHH", "SRHSFH", "SHSH", records[0][0]))
    
#     connection_obj.commit()
#     cursor_obj.close()
#     return 'Hello, World!'


# @app.route('/api/v1/data')
# def get_data():
#     connection_obj = sqlite3.connect('geek.db')
#     cursor_obj = connection_obj.cursor()
#     cursor_obj.execute(sqlite_select_all_query)
#     records = cursor_obj.fetchall()
#     print(records)
#     cursor_obj.close()
#     return records

# if __name__ == "__main__":
#     app.run(debug=True)