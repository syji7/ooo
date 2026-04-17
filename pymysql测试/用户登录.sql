create database jd_user;
create table jd_users(
    id int primary key auto_increment,
    name varchar(100),
    password varchar(100)
);
insert into jd_users(name,password) values ('张三',123456);
insert into jd_users(name,password) values ('李四','abc');

select * from jd_users where name='张三'and password=123456;
select * from jd_users where name='李四'and password='abc';



