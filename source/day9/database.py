import sqlite3,const,os
import threading as td

lock = td.Lock()

connect = sqlite3.connect(const.DATANAME["database"], check_same_thread=False)
cursor = connect.cursor()

def DBexec(sql_cmd,ext=0):
	try:
		lock.acquire(True)
		cursor.execute(sql_cmd,ext) if ext else cursor.execute(sql_cmd)
		connect.commit()
		return 1 
	finally:
		lock.release()

def DBexecRetID(sql_cmd,ext=0):
	try:
		lock.acquire(True)
		cursor.execute(sql_cmd,ext) if ext else cursor.execute(sql_cmd)
		connect.commit()
		rowID = cursor.lastrowid
		return rowID
	finally:
		lock.release()

def DBexecmulti(sql_cmds,exts=0):
	try:
		lock.acquire(True)
		clen = len(sql_cmds)
		for i in range(clen):
			cursor.execute(sql_cmds[i],exts[i]) if exts else cursor.execute(sql_cmds[i])
		connect.commit()
		return 1 
	finally:
		lock.release()

def DBqueryone(sql_cmd,ext=0):
	try:
		lock.acquire(True)
		res = cursor.execute(sql_cmd,ext) if ext else cursor.execute(sql_cmd)
		res = res.fetchone()
		return res
	finally:
		lock.release()

def DBqueryall(sql_cmd,ext=0):
	try:
		lock.acquire(True)
		res = cursor.execute(sql_cmd,ext) if ext else cursor.execute(sql_cmd)
		res = res.fetchall()
		return res
	finally:
		lock.release()

# scripts = [
# """
# CREATE TABLE GROUPET(
# 	groupID TEXT,
# 	groupTAG TEXT
# )
# """,
# """
# CREATE TABLE CONFIG(
# 	tag TEXT,
# 	value TEXT
# )
# """,
# """
# CREATE TABLE MASHINESTATUS(
# 	tag TEXT,
# 	status INTEGER
# )
# """,
# """
# CREATE TABLE USER(
# 	uid TEXT,
# 	nickname TEXT,
# 	admin INTEGER,
# 	points INTEGER DEFAULT 0 NOT NULL ,
# 	isBan INTEGER
# )
# """
# ]

# for script in scripts:
# 	cursor.execute(script)
# 	connect.commit()