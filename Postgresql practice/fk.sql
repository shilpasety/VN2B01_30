create table customers(
cid int generated always as identity,
cname varchar not null,
primary key(cid)
);

select * from customers;


insert into customers(cname) values('Pranaya'),
                                    ('Advaitha');

create table orders(
orderid int generated always as identity,
cid int,
name varchar not null,
phone varchar(20),
email varchar,
primary key(orderid),
constraint fk
foreign key(cid)
references customers(cid)
);

select * from orders;

insert into orders(cid,name,phone,email) values(1,'bpl',9989874004,'bplcompany@hotstgator.com'),
                                           (2,'infosys',7659092425,'infosystechsol@info.com'),
                                           (2,'Wipro',9010073009,'wiprotechnologies@wip.com');