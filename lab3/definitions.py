class Room:
    def __init__(self, number, capacity):
        self._number = number
        self._capacity = capacity

    def get_number(self): return self._number

    def get_capacity(self): return self._capacity

class Teacher:
    def __init__(self, id, name):
        self._id = id
        self._name = name

    def get_id(self): return self._id

    def get_name(self): return self._name

    def __str__(self): return self._name

class Day:
    def __init__(self, day):
        self._day = day

    def get_day(self): return self._day

class Department:
    def __init__(self, name, courses):
        self._name = name
        self._courses = courses

    def get_name(self): return self._name

    def get_subjects(self): return self._courses

class Class:
    def __init__(self, id, dept, course):
        self._id = id
        self._dept = dept
        self._course = course
        self._teacher = None
        self._meeting_time = None
        self._day = None
        self._room = None

    def get_id(self): return self._id

    def get_dept(self): return self._dept

    def get_course(self): return self._course

    def get_teacher(self): return self._teacher

    def get_meeting_time(self): return self._meeting_time

    def get_room(self): return self._room

    def get_day(self): return self._day

    def set_instructor(self, instructor): self._teacher = instructor

    def set_meeting_time(self, meetingTime): self._meeting_time = meetingTime

    def set_day(self, day): self._day = day

    def set_room(self, room): self._room = room

    def __str__(self):
        return str(self._dept.get_name()) + "," + str(self._course.get_number()) + "," + \
               str(self._room.get_number()) + "," + str(self._teacher.get_id()) + "," + str(
            self._meeting_time.get_time()) + "," + str(self._day.get_day())

class Subject:
    def __init__(self, number, name, teachers, max_num_of_students, grade, is_lab=False):
        self._number = number
        self._name = name
        self._max_num_of_students = max_num_of_students
        self._teachers = teachers
        self._grade = grade
        self._isLab = is_lab

    def get_number(self): return self._number

    def get_name(self): return self._name

    def get_teachers(self): return self._teachers

    def get_max_num_of_students(self): return self._max_num_of_students

    def get_grade(self): return self._grade

    def get_is_lab(self): return self._isLab

    def __str__(self): return self._name

class ClassTime:
    def __init__(self, time):
        self._time = time

    def get_time(self): return self._time
