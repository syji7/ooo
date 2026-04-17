-- 1. 创建数据库 # todo 创建库是create database 库名;
CREATE DATABASE IF NOT EXISTS sql_train;
USE sql_train;

-- 2. 创建学生表
--     #todo 表的设置是表名(字段名和字段类型)
CREATE TABLE student
(
    id     INT PRIMARY KEY AUTO_INCREMENT,
--     todo  NOT NULL/不能为空,为空就报错 汉字用varchar,数字用int,还有一个是啥?答:还有一个小数float 带数字的小数是decimal(5)是指3位小数前,两位小数后
    name   VARCHAR(20) NOT NULL,
    age    INT,
-- char(1)是输入一个字符?
    gender CHAR(1),
    class  VARCHAR(20)
);
-- todo create table 表名 (字段名,字段特性)
-- 3. 创建成绩表
CREATE TABLE score
(
    id         INT PRIMARY KEY AUTO_INCREMENT,
    student_id INT,
    subject    VARCHAR(20),
    score      INT,
    FOREIGN KEY (student_id) REFERENCES student (id)
);

-- 4. 插入测试数据
-- todo 格式:insert into 表名 (列字段,列字段..) values (值_需要一一对应);
INSERT INTO student(name, age, gender, class)
VALUES ('张三', 18, '男', '高一1班'),
       ('李四', 17, '女', '高一1班'),
       ('王五', 19, '男', '高一2班'),
       ('赵六', 18, '女', '高一2班'),
       ('钱七', 17, '男', '高一1班');
#todo 因为加了primary key 是逐步增加,所以这个不用增加数据
INSERT INTO score(student_id, subject, score)
VALUES (1, '语文', 85),
       (1, '数学', 92),
       (2, '语文', 90),
       (2, '数学', 88),
       (3, '语文', 78),
       (3, '数学', 95),
       (4, '语文', 93),
       (4, '数学', 89),
       (5, '语文', 80),
       (5, '数学', 85);

-- 第一题:查询表中所有的学生的姓名\年龄\班级
select *
from student;
# 要从两个表里面并出来学生的所有信息?
# 3.查询成绩表中的所有科目?
select *
from score;
# todo distinct 去重

# 第二题 查询(where)
# 查询高一1班所有的学生
select *
from student
where class = '高一1班';
# 年龄大于18岁的学生
select *
from student
where age > 18;
# 女生而且等于18 /用两个条件筛选
# todo order by 是用来排序的
# todo 多条件的判断应该是 and/ or /not /bewteen and 这些
select *
from student
where gender = '女'
  and age = 18;
#数学成绩大于90分的记录
select *
from score
where subject = '数学'
  and score > 90;
# 查询姓名为张三或者李四的学生(#todo 用IN是什么意思?)
select *
from student
where name = '张三'
   or name = '李四';
#第三题
#从年龄小到大查询所有学生
select *
from student
order by age;
#正序不要添加asc
#按数学成绩从高到低查询成绩表
select *
from score
order by score desc;
# 按班级排序,班级相同按照年龄降序
select *
from student
order by class;
#todo 怎么调用另外一个?
# 第四题
# 添加一位新元素
insert into student(name, age, gender, class)
values ('孙八', '18', '男', '高一2班');

#修改张三的年龄
# todo 更新是怎么更新去了
# insert/delete/update
# update 表名 set 字段名=值 where 条件(独特的标识符)
# delete from xxx where 条件
update student
set age=19
where name = '张三';
delete
from student
where name = '钱七';
update student
set age=age + 1
where class = '高一1班';
select *
from student;
# 第五题
# 1.查询学生总人数
select count(*)
from student;
# 查询数学成绩的平均分,最高分,最低分
select max(score)
from score
where subject = '数学';
select min(score)
from score
where subject = '数学';
select ROUND(AVG(score), 2)
from score
where subject = '数学';
#todo 保留两位小数 round(xx(),2)
select *
from student;
# 查询高一2班的学生数量
select count(*)
from student
where class = '高一2班';
# 第六题
# 1.统计人数,按照班级分组
# group by 的用处是能够总的看出来数据的情况
#这里要区分count(*)和count(class)的区别,
#如因为*表示的这一行,只要这一行存在,count就会给你加1,不管里面是不是有null,就算里面全是null也不影响这一行的存在
#如果是class,就是查询class这一行,如果里面有空值,这一行就不存在了, 就不会统计这一行
select class, count(class) from student
group by class;
# 按科目分组,计算平均分
select subject,round(avg(score),2) from score group by subject;
#todo group by "这里是分组的依据,即按这个来划分"

# 3.按班级分组,查询平均年龄大于17的班级
select * from student;
#应该没写错
select class,count(class) from student group by class having avg(age)>17;

