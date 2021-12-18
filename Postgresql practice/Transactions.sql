create table institute(
id serial primary key,
name varchar,
age int,
address varchar,
salary int
);

insert into institute(name,age,address,salary) 
      values('Paul',32,'California',20000),
      ('Allen',25,'Texas',15000),
      ('Teddy',23,'Norway',20000),
      ('Mark',25,'Rich-mond',65000),
      ('David',27,'Texas',85000),
      ('Kim',22,'South-Hall',45000),
      ('James',24,'Houston',10000)
      
      select * from institute;
      
     begin;
     delete from institute where salary=20000;
    rollback;
   
   begin;
  delete from institute where salary=20000;
 commit;
rollback;
     