create database crudapplication;
use crudapplication;
create table users(
id int not null auto_increment primary key,
NAME VARCHAR(50),
AGE int,
CITY varchar(50)
);
select * from users;
insert into users(NAME,AGE,CITY) VALUES ('GK',21,'CBE');
select * from users;