# 1.导包
import pymysql

# 2.创建连接对象
conn = pymysql.connect(
    host='localhost',
    port=3306,
    user='root',
    password='root',
    database='sql_train'
)
# 3.获取游标
r = conn.cursor()
# 4.游标执行sql语句
# 输出是影响,不会直接输出表,需要你自己手动操作
# 1.
row = r.execute('select * from sql_train.score;')
print(f'影响{row}')
# 2.增加
r.execute('insert ')
# 3.删除
# 4.修改
try:
    r.execute('update sql_train.score set score=score-6 where id=3')
    r.execute('update sql_train.score set score=score+6 where id=4')
except:
    # todo 手动回滚
    conn.rollback()
else:
    # todo 手动提交
    conn.commit()
# 5.关闭游标
r.close()
# 6.关闭连接
conn.close()
