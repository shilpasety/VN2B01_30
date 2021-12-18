create table emp_d3(
name varchar(25),
eid integer,
designation varchar(25),
salary integer
);
select * from emp_d3;

insert into emp_d3 values('Surya',11250,'manager',15000);
insert into emp_d3 values('Varma',11251,'manager',15500);
insert into emp_d3 values('kalyan',11252,'manager',15500);
insert into emp_d3 values('Sharma',11253,'manager',15560);
insert into emp_d3 values('Vihan',10256,'engineer',12000);
insert into emp_d3 values('vikram',10258,'engineer',12500);
insert into emp_d3 values('Vaishali',10259,'hr',10000);
INSERT INTO emp_d3 VALUES('sreekanth',10267,'hr',10200);
INSERT INTO emp_d3 VALUES('ishaan',10268,'supervisor',8500);
INSERT INTO emp_d3 VALUES('kiran',10269,'supervisor',8000);

alter table emp_d3 add column place varchar(20);

create table emp_d3_copy as select * from emp_d3;
ALTER TABLE emp_d3_copy ADD COLUMN branch varchar(50);
select * from emp_d3_copy;

drop table emp_d3_copy;