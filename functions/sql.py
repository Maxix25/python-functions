import sqlite3
import mysql.connector
def init_sqlite(name:str, flask:bool):
	if flask == True:
		db = sqlite3.connect(name, check_same_thread = False)
	else:
		db = sqlite3.connect(name)
	return db
def init_mysql(host, user, password, database):
	return mysql.connector.connect(
		host = host,
		user = user,
		password = password,
		database = database
	)
