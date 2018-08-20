from util import db_util

connectObj = db_util.ConnectToMysql()
connect    = connectObj.getConnect()
cursor  = connect.cursor()

sql = "select table_name from information_schema.tables where table_schema= '%s'" % 'wyy'
print(sql)
cursor.execute('use information_schema')
cursor.execute(sql)
v = cursor.fetchall()
cursor.execute('use wyy')
for single in  v:
    # single = 'songtotal'
    sql = 'Describe %s  time'% single
    cursor.execute(sql)
    try:
        v = cursor.fetchone()

        v1 = v[0]
        # print(v1)
    except:
        sql = 'ALTER TABLE %s ADD  time varchar(255)' % single
        print(sql)


connect.commit()


