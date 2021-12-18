create table emp2(
emp2_name varchar(25),
emp2_marks integer,
emp2_age integer,
emp2_email varchar(25)
);
insert into emp2 values('shilpa','89','26','shilpasetycse@gmail.com');
insert into emp2 values('Asha','98','24','ashasety123@gmail.com');
insert into emp2 values('Pranaya','100','2','pranayababy@gmail.com');
delete from emp2 where emp2_age = '26';
alter table emp2 add column emp_occupation varchar(30);
select emp_occupation from emp2;
select * from emp2;