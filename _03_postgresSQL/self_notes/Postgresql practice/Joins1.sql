create table custmrs(
cid int primary key,
storeid int,
email varchar,
address varchar
);
select * from custmrs;
insert into custmrs values(1,2,'kishor@gmail.com','USA'),
                           (2,4,'shilpa@hotmail.com','Australia');
                           
create table payment(
payid int,
amount varchar,
paydate varchar
);

select * from payment;
insert into payment values(1,2000,'2003-02-14'),
                           (2,4000,'2004-05-10'),
                            (5,5000,'2007-09-08');
                            
                           select email, address,payid 
                           from custmrs
                           cross join payment;
                           
                          select paydate,amount,email
                          from custmrs as c
                          inner join payment as p
                          on p.payid=c.cid;
                          
                         select paydate,amount,email
                          from custmrs as c
                          inner join payment as p
                          on p.payid=c.storeid;
                          
                         select paydate,amount,address
                         from custmrs
                         right outer join payment
                         on payment.payid=custmrs.storeid;
                         
                        select paydate,amount,email
                        from custmrs
                        left outer join payment 
                        on payment.payid=custmrs.cid;
                        
                       select email,payid,paydate
                       from custmrs
                       full outer join payment 
                       on payment.payid=custmrs.storeid;