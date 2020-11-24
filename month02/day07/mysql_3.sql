--聚合练习
--1. 统计每位作家出版图书的平均价格
select author,avg(price) from book group by author;

--2. 统计每个出版社出版图书数量
select publish,count(*) from book group by publish;

--3. 查看总共有多少个出版社
select count(distinct publish) from book;

--4. 筛选出那些出版过超过50元图书的出版社，
--并按照其出版图书的平均价格降序排序
select publish,avg(price) from book
group by publish
having max(price) > 50
order by avg(price) desc;

--5. 统计同一时间出版图书的最高价格和最低价格
select publish_time,max(price),min(price)
from book group by publish_time;


--部门和员工表数据
insert into dept values (1,"技术部"),(2,"销售部"),(3,"市场部"),(4,"行政部"),(5,'财务部'),(6,'总裁办公室');

insert into person values
(1,"Lily",29,'w',20000,'2017-4-3',2),
(2,"Tom",27,'m',16000,'2019-10-3',1),
(3,"Joy",30,'m',28000,'2016-4-3',1),
(4,"Emma",24,'w',8000,'2019-5-8',4),
(5,"Abby",28,'w',17000,'2018-11-3',3),
(6,"Jame",32,'m',22000,'2017-4-7',3);

--级联动作
alter table person add
constraint dept_fk
foreign key(dept_id)
references dept(id)
on delete cascade on update cascade;

alter table person add
constraint dept_fk
foreign key(dept_id)
references dept(id)
on delete set null on update set null;


--练习: 根据所学表关系设计,重新设计用户朋友圈数据表,使之合理
用户表
create table user(
id int primary key auto_increment,
name varchar(30),
passwd char(16)
);

朋友圈
create table pyq(
id int primary key auto_increment,
image char(128),
content text,
time datetime,
address varchar(50),
user_id int,
foreign key (user_id) references user(id)
);

点赞评论
create table user_pyq(
id int primary key auto_increment,
uid int,
pid int,
`like` bit,
comment text,
foreign key (uid) references user(id),
foreign key (pid) references pyq(id)
);


连接查询示例

统计每个部门员工数量
select d.dname,count(dept_id) from dept as d left join person as p on d.id = p.dept_id group by d.dname;

select p.name,d.dname,p.salary from dept as d right join person as p on d.id = p.dept_id where p.salary>=20000;



