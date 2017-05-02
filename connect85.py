#conding=utf-8
import psycopg2
print "*** This is coonect test ***"
print "test start..."
##连接到一个存在的数据库
##connect（）建立一个新的数据库会话，并返回一个connect实例
conn = psycopg2.connect("dbname=zkeco_db20141126 user=postgres password=q1w2e3 host=172.16.17.85 port=5432")
print 'connect successful!'

##打开一个光标，用来执行数据库操作
cur = conn.cursor()
print 'cursor successful!'

cur.execute("select tablename from pg_tables where schemaname='public'")
print "rowcount =",cur.rowcount
'''
rows = cur.fetchone()
print rows	##打印一条结果：('tablename',)
'''
#############################################
'''
rows2 = cur.fetchone()
while rows2:
	for tablename in rows2:
		print tablename	##打印全部结果：tablename
	rows2 = cur.fetchone()
'''
#############################################
'''
for i in xrange(cur.rowcount):
	tablename=cur.fetchone()
	print tablename	##打印全部结果：('tablename',)
'''
#############################################
'''
rows3 = cur.fetchmany()
while rows3:
	for tablename in rows3:
		print tablename	##打印全部结果：('tablename',)
	rows3 = cur.fetchmany()
'''
'''
rows4 = cur.fetchall()
for tablename in rows4:
	print tablename	##打印全部结果：('tablename',)
'''
#############################################

cur.execute("select count(*) from INFORMATION_SCHEMA.COLUMNS   WHERE table_name = 'zemp_info'")
result = cur.fetchone()
while result:
	for colcount in result:
		print "colcount =",colcount	##打印指定表列数
	result = cur.fetchone()

cur.execute("select * from zemp_info where pernr='10000138'")
rows5 = cur.fetchall()
for row in rows5:
	print 'oid=',row[7], ',server_id=',row[8],',pernr=',row[9],',area=',row[10],'\n'


##关闭到数据库的通信
cur.close()
print 'cursor close!'
conn.close()
print 'connect close!'
print "test end..."