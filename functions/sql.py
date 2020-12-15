import sqlite3
def init_sqlite(name:str, flask:bool):
	if flask == True:
		db = sqlite3.connect(name, check_same_thread = False)
	else:
		db = sqlite3.connect(name)
	return db
