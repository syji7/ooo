import redis

# host是本机,prot是端口号,decode是转码
r = redis.Redis(host='localhost', port=6379, decode_responses=True)
r.set('name', '张三')
print(r.get('name'))
# 单个键值对的设置和获取
r.set('姓名', '江源')
print(r.get('姓名'))
# 多个字符串的设置和获取
r.mset({'姓名': 'syj', '性别': '男'})
print(r.mget(['姓名', '性别']))
# 会将之前的江源覆盖..
# 设置超时时间,就是说如果设置了超时的时间,缓存过了这个时间这一段就会消失不见
r.setex('姓名', 2, '曾伟节')
print(r.get('姓名'))

# 2.哈希list的操作,哈希表是在hmset中有一个主键,可以传入更多的内容,像key, field, value, field, value...这样配对,而传统的set键只能传入一个键名一个值
# 方法1：单个传入哈希表和取哈希值
r.hset('user:1001', 'name', '李四')
r.hset('user:1001', 'age', '30')
r.hset('user:1001', 'city', '上海')
# 查询哈希表里面的值
r1 = r.hget('user:1001', 'name')
print(r1)
# 多个传入哈希表里的值#todo hmset已经要被淘汰了,找一下能替代的
r.hmset('user:1002', {'age': '18', 'name': '李四'})
values = r.hmget('user:1002', ['age', 'name'])
print(values)
# 查询哈希所有的字段名:
key1 = r.hkeys('user:1002')
print(key1)
# 查询哈希表中所有的值名:
value1 = r.hvals('user:1002')

# 3.从列表操作
# 列表的增加操作不一样,不是用set,而是用push
# r.lpush('关键词', '要加入的values'),push可以重复输入,反复加载就会重新添加?
r.lpush('task', 'task1', 'task2', 'task3')
r.rpush('task', 'task4', 'task5')
# 查询列表里面所有的元素
all_tasks = r.lrange('task', 0, -1)
print(all_tasks)
# 从左侧弹出元素
left_task = r.lpop('task')
print(f'左侧弹出:{left_task}')
# Redis 的 List 是「追加型」结构 ——rpush/lpush 的逻辑是 “在现有列表末尾 / 开头加元素”，而不是 “清空后重新加”

# 集合的添加
r.sadd('tag', 'python', 'redis', 'database', 'cache')
# 获取所有的元素
r.smembers('tags')
# 判断元素是否存在
is_memeber = r.sismember('tags', 'python')
# 随机弹出一个元素
random_tag = r.spop('tags')
# 移除指定的元素
r.srem('tag', 'database')
