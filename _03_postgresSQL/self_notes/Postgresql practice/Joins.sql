create table company(
id integer,
name varchar,
age integer,
address varchar,
salary varchar,
join_date varchar
);

select * from company;

insert into company values(1,'Paul',32,'California',20000,'2001-07-13'),
                          (3,'Teddy',23,'Norway',20000,''),
                          (4,'Mark',25,'Rich-Mond',65000,'2007-12-13'),
                          (5,'David',27,'Texas',85000,'2007-12-13'),
                          (2,'Allwn',25,'Texas','','2007-12-13'),
                          (8,'Paul',24,'Houston',20000,'2005-07-13'),
                          (9,'James',44,'Norway',5000,'2005-07-13'),
                          (10,'James',45,'Texas',5000,'2005-07-13');
                          
                         truncate table company;
                         
  create table department(
  id int primary key not null,
  dept varchar not null,
  dept_id int not null
  ); 
  

 select * from department;
 
insert into department values(1,'IT billing',1),
                              (2,'Engineering',2),
                              (3,'Finance',7);
                              
                             select dept_id,name,dept,salary
                             from company
                             cross join department;
                             
                select  dept_id,name,dept 
                from company 
                inner join department
                on company.id=department.dept_id;
                
          select dept_id,name,salary
          from company
          left outer join department
          on company.id=department.dept_id;
         
         select dept_id,name,salary
         from company
         right outer join department
         on company.id=department.dept_id;
         
        select dept_id,name,age
        from company
        full outer join department
        on company.id=department.dept_id;