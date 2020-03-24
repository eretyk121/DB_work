from pprint import pprint
import psycopg2 as ps

students = [{'id': 7, 'name': 'Petr Gorin', 'gpa': 4.26, 'birth': '1969-01-10'},
            {'id': 8, 'name': 'Evgeny Gorin', 'gpa': 3.67, 'birth': '1974-04-19'}
            ]

def add_student(file):
    for one in file:
        with  ps.connect(dbname='studing', user='igor1', password='1234') as conn:
            with conn.cursor() as cur:
                cur.execute(f"insert into student values(%s, %s, %s, %s);", (one['id'], one['name'], one['gpa'], one['birth']))

def add_students(course_id, student_id):
    id = 3
    for one in student_id:
        with  ps.connect(dbname='studing', user='igor1', password='1234') as conn:
            with conn.cursor() as cur:
                cur.execute(f"insert into student values(%s, %s, %s, %s);", (one['id'], one['name'], one['gpa'], one['birth']))
                cur.execute(f'insert into student_course values(%s, %s, %s);', (id, one['id'], course_id))
        id +=1

def get_course_students(course_id):
    with  ps.connect(dbname='studing', user='igor1', password='1234') as conn:
        with conn.cursor() as cur:
            cur.execute(f'select * from student where id in (select student_id from student_course where course_id = {course_id});')
            result = cur.fetchall()
            pprint(result)

def get_student(student_id):
    with  ps.connect(dbname='studing', user='igor1', password='1234') as conn:
        with conn.cursor() as cur:
            cur.execute(f'select * from student where id = {student_id};')
            result = cur.fetchall()
            pprint(result)

def create_db(name, *args):
    list_fild = ''
    for one in args:
        if list_fild == '':
            list_fild = one
        else:
            list_fild = f'{list_fild}, {one}'
    with  ps.connect(dbname='bd_test', user='igor1', password='1234') as conn:
        with conn.cursor() as cur:
            cur.execute(f'create table if not exists {name} ({list_fild});')


# create_db('test4', 'id integer', 'name varchar(100)')
# get_student(8)
# add_student(students)
# add_students(1, students)
# get_course_students(2)