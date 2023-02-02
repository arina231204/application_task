create or replace function get_course_id_by(x VARCHAR(254))
returns table(courses_id bigint) as $$
	SELECT c.id FROM users_student as s
	inner join users_courses as c
	ON c.student_id = s.id
	where email = x
$$ LANGUAGE SQL;

select  * from get_course_id_by('spencer@microsoft.com')

select * from users_courses

create table payments
(
	Id SERIAL PRIMARY KEY,
	Amount integer NOT NULL,
	Pay_date date,
	Courses_id bigint,
	FOREIGN KEY(Courses_id) REFERENCES users_courses (id) ON DELETE SET DEFAULT 
);


insert into payments
(amount,pay_date,Courses_id)
values
-- ('15000','2022-08-15',  get_course_id_by('aman@mail.ru'));
-- ('55000','2022-08-05',get_course_id_by('aapina@bk.ru'));
-- ('5000','2022-08-25',get_course_id_by('spencer@microsoft.com'));

select * from payments

select c.name, c.date_started, s.name, m.name, c.language
from users_student as s
inner join users_courses as c
ON c.id = s.Id 
inner join users_mentor as m 
ON s.id = m.Id 
inner join users_language as l 
ON s.id = l.id;

select c.language, sum(p.Amount) from users_courses as c
inner join payments as p
on  c.id = p.courses_id
group by  c.language;









