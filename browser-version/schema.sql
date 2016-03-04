drop table if exists names;
create table names( id integer primary key autoincrement, 
	name text not null, 
	year integer not null, 
	gender text not null, 
	count integer not null);