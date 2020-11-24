--homework 解析
--创建数据库 books  使用utf8格式
create database books charset=utf8;

--在该数据库中创建一个数据表  book 字段如下
--id  书名  作者  出版社  价格  备注
use books;
create table book (
id int primary key auto_increment,
bname varchar(50) not null,
author varchar(30) not null,
publish varchar(50),
price float,
`comment` text
);


--向该表中从插入若干数据 >8条,数据类型和约束自定
--
--作者: 老舍  鲁迅  冰心
--价格: 30-120
--出版社: 中国文学  人民教育  机械工业

insert into book (bname,author,publish,price,comment)
values
("边城","沈从文","机械工业出版社",36,"小城故事多"),
("骆驼祥子","老舍","机械工业出版社",43,"你是祥子么？"),
("茶馆","老舍","中国文学出版社",55,"老北京"),
("呐喊","鲁迅","人民教育出版社",71,"最后的声音"),
("朝花夕拾","鲁迅","中国文学出版社",53,"好时光"),
("围城","钱钟书","中国文学出版社",44,"你心中的围城是什么");

insert into book (bname,author,publish,price)
values
("林家铺子","茅盾","机械工业出版社",51),
("巨人传","忘了","人名教育出版社",47);

--1. 查找30多元的图书
select * from book where price>=30 and price<40;
--２．查找人民教育出版社出版的图书　
select * from book where publish="人民教育出版社";
--３．查找老舍写的，中国文学出版社出版的图书　
select * from book where author="老舍" and
publish="中国文学出版社";
--４．查找备注不为空的图书
select * from book where comment is not null;
--５．查找价格超过６０元的图书，只看书名和价格
select bname,price from book where price>60;
--６．查找鲁迅写的或者茅盾写的图书
select * from book where author="鲁迅" or
author = "茅盾";
select * from book where author in ("鲁迅","茅盾");

--马拉松表数据插入
insert into marathon
(athlete,birthday,registration_time,performance) values
("尼古拉斯","1996-10-1","2020/8/16 10:23:34","2:36:42"),
("曹操","1999-10-1","2020/10/16 18:33:5","2:28:56");

--练习 使用book表
--1. 将呐喊的价格修改为45元
update book set price=45 where bname="呐喊";
--2. 增加一个字段出版时间 类型为 date 放在价格后面
alter table book add publish_time date after price;
--3. 修改所有老舍的作品出版时间为 2018-10-1
update book set publish_time="2018-10-1" where author="老舍";
--4. 修改所有中国文学出版社出版的作品出版时间为 2020-1-1,但是不要改老舍的
update book set publish_time="2020-1-1"
where publish="中国文学出版社" and author!="老舍";
--5. 修改所有出版时间为Null的图书 出版时间为 2019-10-1
update book set publish_time="2019-10-1"
where pubbblish_time is null;
--6. 所有鲁迅的图书价格增加5元
update book set price=price+5
where author="鲁迅";
--7. 删除所有价格超过70元或者不到40元的图书
delete from book where price not between 40 and 70;

--高级查询练习
--
--1. 查找所有蜀国人信息，按照攻击力排名
select * from sanguo where country="蜀"
order by attack desc;
--2. 将赵云攻击力设置为360，防御设置为70
update sanguo set attack=360,defense=70
where name="赵云";
--3. 吴国英雄攻击力超过300的改为300，最多改2个
update sanguo set attack=300
where country="吴" and attack > 300
limit 2;
--4. 查找攻击力超过200的魏国英雄名字和攻击力并显示为姓名， 攻击力
select name as 姓名,attack as 攻击力 from sanguo
where country="魏" and attack > 200;
--5. 所有英雄按照攻击力降序排序，如果相同则按照防御生序排序
select * from sanguo
order by attack desc,defense;

--6. 查找名字为3字的
select * from sanguo where name like "___";

--7. 查找攻击力比魏国最高攻击力的人还要高的蜀国英雄
select *
from (select * from sanguo where country="蜀") as s
where attack >
(select attack from sanguo
where country="魏"
order by attack desc
limit 1);

--8. 找到魏国防御排名2-3名的英雄
select * from sanguo
where country="魏"
order by defense desc
limit 2 offset 1;
--9. 查找所有女性角色中攻击力大于180的和男性中攻击力小于250的
select * from sanguo where gender="女" and attack > 180
union
select * from sanguo where gender="男" and attack < 250;






