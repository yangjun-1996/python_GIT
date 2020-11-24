"""
数据库查询操作示例
"""
import pymysql

# 连接数据库
args = {
    "host":"localhost",
    "port":3306,
    "user":"root",
    "password":"123456",
    "database":"stu",
    "charset":"utf8"
}

db = pymysql.connect(**args)

# 创建游标  操作数据库数据，获取操作结果的对象
cur = db.cursor()

# 数据库读操作
sql = "select name,age,score from cls;"
cur.execute(sql)

# 迭代获取查询结果
# for row in cur:
#     print(row)

# 获取查询结果
print("one:",cur.fetchone())
print("many:",cur.fetchmany(3))
print("all:",cur.fetchall())

# 关闭游标和数据库连接
cur.close()
db.close()







