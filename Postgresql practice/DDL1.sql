create table emp_d(
name varchar(25),
eid integer,
designation varchar(25),
salary integer
);

insert into emp_d values('Surya',11250,'manager',15000);
insert into emp_d values('Varma',11251,'manager',15500);
insert into emp_d values('kalyan',11252,'manager',15500);
insert into emp_d values('Sharma',11253,'manager',15560);
insert into emp_d values('Vihan',10256,'engineer',12000);
insert into emp_d values('vikram',10258,'engineer',12500);
insert into emp_d values('Vaishali',10259,'hr',10000);
INSERT INTO emp_d VALUES('sreekanth',10267,'hr',10200);
INSERT INTO emp_d VALUES('ishaan',10268,'supervisor',8500);
INSERT INTO emp_d VALUES('kiran',10269,'supervisor',8000);

delete from emp_d where eid=10268;
delete from emp_d where name='kiran';

select * from emp_d;