# Sql lesson 2
Была использована бд из урока 3.

```sql

CREATE TABLE authors (
	id SERIAL PRIMARY KEY,
	name VARCHAR(200) NOT NULL DEFAULT 'lore',
	year DATE NOT NULL DEFAULT '1970-01-01'
);

CREATE TABLE books (
	id SERIAL PRIMARY KEY,
	title VARCHAR(200) NOT NULL DEFAULT 'noname',
	genre_id INT NOT NULL DEFAULT 0
);

CREATE TABLE genres (
	id SERIAL PRIMARY KEY,
	genre VARCHAR(100) NOT NULL DEFAULT 'unknown'
);

CREATE TABLE authors_books (
	author_id INT NOT NULL DEFAULT 0,
	book_id INT NOT NULL DEFAULT 0
);

Далее нужно заполнить таблицы, также возьму пример с урока

INSERT INTO genres (genre) VALUES
	('SF'),
	('novel'),
	('story'),
	('horror');

INSERT INTO books(title, genre_id) VALUES
	('Майстер і Маргарита', 2),
	('Фауст', 0),
	('Білий клик', 3),
	('Дюна', 1),
	('Війна і мир', 2);

INSERT INTO authors (name) VALUES
	('Френк Герберт'),
	('Михайло Булгаков'), 
	('Джек Лондон'), 
	('Йоган Ґете'), 
	('Роберт Хайнлайн');

INSERT INTO authors_books (author_id, book_id) VALUES 
	(1, 4),
	(2, 1),
	(3, 3),
	(4, 2);

```

**Вивчаємо UPDATE та DELETE**
```sql
UPDATE books             
set title= 'Faust in english'
where id = 2;

UPDATE books
set title= 'Duna'
where genre_id = 1;

UPDATE books
set genre_id = 4
where title = 'Duna';

delete from authors where id = 3;
delete from authors where id <4;
```


**Знайомимося з FETCH (аналог LIMIT) та TRUNCATE (аналог DROP TABLE + CREATE TABLE)**
```sql
select book_id from authors_books where author_id>0 and author_id <5 order by book_id  desc fetch next 2 rows only;
select book_id from authors_books where author_id>0 and author_id <5 order by book_id  desc fetch first 2 rows only;
Эти зпросы выводят мне одинаковый результат, хотя чат гпт говорит что всё ок, я думаю это из-за специфики данных в таблице authors_books

truncate table authors_books;
ЧатГПТ сказал что только так эта команда и используется, чистит таблицу от данных без возможности восстановления.

Также проработал примеры с DELETE
DELETE FROM authors_books WHERE author_id>2;
```


# Sql lesson 3

Создал бд с машинами, дамп загрузил в репозиторий.

Запросы для этой бд
```sql
select cars.car_id, models.name from cars inner join models on cars.model_id = models.model_id; - даёт айди машины и её название
select cars.car_id, creators.creator, creators.brand from cars left join creators on cars.creator_id = creators.creator_id; - даёт айди машины и её создателя
select cars.car_id, models.name, creators.creator, creators.brand from cars inner join models ON cars.model_id = models.model_id inner join creators ON cars.creator_id = creators.creator_id; - даёт всё ':)'
```
# Sql module 2
```sql
select concat('This is ', name, ',', case when gender = 'm' then 'he' else 'she' end,' has emeil ', email) as info from users;
```
**result**               

 This is Vasya,he has emeil mmm@mmail.com
 
 This is Alex,he has emeil mmm@gmail.com
 
 This is Alexey,he has emeil alexey@gmail.com
 
 This is Helen,she has emeil hell@gmail.com
 
 This is Jenny,she has emeil eachup@gmail.com
 
 This is Lora,she has emeil tpicks@gmail.com

```sql
SELECT 'We have ' || COUNT(*) || ' boys!' AS "Gender information:" FROM users WHERE gender = 'm'                                                                                      
UNION                          
SELECT 'We have ' || COUNT(*) || ' girls!' AS "Gender information:" FROM users WHERE gender = 'f';
```
**result** 

Gender information: 

---------------------
 We have 3 boys!
 
 We have 3 girls!
 
```sql
select name, count(word.id) as words from vocabulary left join word on vocabulary.id = word.vocabulary_id group by vocabulary.name, vocabulary.id order by vocabulary.id;
```
**result**

name   | words 

---------+-------

 animals |    10

 school  |    10

 nature  |    10

 human   |    10

 SF      |    10






