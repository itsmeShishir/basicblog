create table category(
	id int AUTO_INCREMENT PRIMARY KEY,
    name varchar(100) not null,=    created_at DATETIME DEFAULT CURRENT_TIMESTAMP
);

create table Blog(
	id int AUTO_INCREMENT PRIMARY KEY,
    title varchar(100) not null,
    content text not null,
    category_id int,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (category_id) REFERENCES
    category(id)
);

insert into category(name) VALUES( "technology"),("lifestyle"),("international news"), ("travels");

# blog ma pani vlaues
insert into Blog(title, content, category_id) 
values("news 1", "this is news 1", 1),
("news2","this is about the news 2", 2),
("news3", "this is nnews 3 description", 3),("news34", "this is nnews 4 description", 1),("news5", "this is nnews 5description", 1);

# *
   SELECT * from Blog;

# title 
   SELECT title from Blog;

# join
  SELECT Blog.id, Blog.title, category.name As categorys
  from blog
  join category on Blog.category_id = category.id

# Where Clause
  select * from Blog 
  WHERE  id=2

# update Blog set title = "hero" where id = 2;
   select * from Blog

# how to delete the data in db
   DELETE from Blog WHERE id=2 ;
   select * from Blog

# serach the blog form its itle 
   select * from Blog where title Like "news 1";