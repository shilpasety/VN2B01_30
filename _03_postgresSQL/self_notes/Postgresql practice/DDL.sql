create table stud(
name varchar,
id int,
mobile varchar,
marks int,
fname varchar,
place varchar
);

select * from stud;

insert into stud values('Pranaya',1,'6303895274',75,'Kishor','Banglore'),
                        ('Shilpa',2,'7659092425',89,'Ramisetty','Chagalamarri'),
                        ('Kishor',3,'9010073009',40,'Narayana','Chagalamarri'),
                        ('Asha',4,'8466962736',67,'Ramisetty','Banglore')
                     
     /*Altering the data (adding column) & updating the data */
 alter table stud add column email varchar,
 update stud set email='shilpasetycse@gmail.com' where name='Shilpa';
 update stud set email='ashasety123@gmail.com' where place='Banglore';
update stud set email='pranayababy@hotmail.com' where email='ashasety123@gmail.com';
 
/* Deleting the rows & columns*/

delete from stud where name='Asha';
alter table stud drop column marks;
 
/* Copying the table  (with & without data)*/
create table stud_copy as table stud;
select * from stud_copy;

create table stud_copy2 as table stud
with no data;
select * from stud_copy2;

/* deleting the data(only data not the table) */
truncate table stud_copy;

/* deleting the table*/

drop table stud_copy2;
select * from stud_copy2;


