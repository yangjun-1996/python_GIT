--创建hobby数据表
create table hobby (
id int primary key auto_increment,
name varchar(30) not null,
hobby set('sing','dance','draw'),
level char,
price decimal(7,2),
remark text comment "备注信息"
);

--插入操作 hobby 表
insert into hobby
(name,hobby,level,price,remark) values
("Joy","sing,dance",'A',54800.005,"练舞奇才"),
("Abby","sing",'B',28800.00,"天籁之音");

insert into hobby
(name,hobby,level,price) values
("Lucy",'draw','C',12800),
("Tom",'dance','B',20000),
("Ale",'draw,sing','B',46000);








