#!/usr/bin/python
# -*- coding: UTF-8 -*-
import sys
import cx_Oracle
import time

rows = int(sys.argv[1])
con = cx_Oracle.connect('test/test@sampledb')
cur = con.cursor()
cur.execute("SELECT MAX(ID) FROM PTTEST")
max_id = cur.fetchone()[0] or 0

start_id = max_id + 1
for i in xrange(rows):
    cur.execute("INSERT INTO PTTEST (ID, NAME, AGE, GENDER, SALARY)VALUES(%d, 'pt', 15, 'male', 50000)" % int(i + start_id))
    if i % 100 == 0:
        time.sleep(3)
        print 'Insert rows [%d]:%d' % (int(time.time()), i)
        con.commit()
cur.close()
con.close()
