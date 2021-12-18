drop table if exists shoppers;
drop table if exists orders;

/* creating the first table (parent) */
create table shoppers(
shoppers_id serial primary key,
shopper_name varchar
);

select * from shoppers;

/* Inserting the data into first table */

insert into shoppers(shopper_name) values('Bluebird'),
                                          ('Dolphin');
                                          
 /* creating the second table (child)  */ 
  create table orders(
  order_id int generated always as identity,
  name varchar,
  phone varchar,
  email varchar,
  shoppers_id int,
  primary key (order_id),
  constraint fk
  foreign key(shoppers_id)
  references shoppers(shoppers_id)
  on delete set null
  );  
  
 select * from orders;
 
insert into orders(shoppers_id,name,phone,email) 
values(1,'John Doe','(408)-111-1234','john.doe@bluebird.dev'),
      (1,'Jane Doe','(408)-111-1235','jane.doe@bluebird.dev'),
      (2,'David Wright','(408)-222-1234','david.wright@dolphin.dev');
      
      /* we cannot insert the id's into the child table that are not present in parent table*/ 
      insert into orders (shoppers_id,name,phone,email)
        values(3,'Kishor','9010073009','nandakishor@hotmail.ocm'); /*SQL error*/
      
     delete from shoppers where shoppers_id=1; 
     delete from shoppers where shopper_name='Dolphin'; 