show databases;
use world;
show tables;
select * from country;
select * from country where continent = "Asia";
select * from country where continent = "Asia" order by population desc;
select name,population,continent from country where continent = "Asia" order by population desc;
