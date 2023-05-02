class Course:
    def __init__(self, number, name, max_number_of_students, instructors):
        self.number = number
        self.name = name
        self.max_number_of_students = max_number_of_students
        self.instructors = instructors

    def __str__(self):
        return self.name

class Class:
    def __init__(self, id, group, course):
        self.id = id
        self.group = group
        self.course = course
        self.room = None
        self.instructor = None
        self.meeting_time = None

    def __str__(self):
        _fmt = '[{group},{course},{room},{instructor},{meeting_time}]'
        args = {
            'group': str(self.group),
            'course': str(self.course),
            'room': str(self.room),
            'instructor': str(self.instructor),
            'meeting_time': str(self.meeting_time)
        }
        return _fmt.format(**args)

class MeetingTime:
    def __init__(self, id, time):
        self.id = id
        self.time = time

    def __str__(self):
        return self.time

class Room:
    def __init__(self, number, seating_capacity):
        self.number = number
        self.seating_capacity = seating_capacity

    def __str__(self):
        return self.number

    def __eq__(self, other):
        if isinstance(other, Room):
            return self.number == other.number

        return self == other

class Instructor:
    def __init__(self, id, name):
        self.id = id
        self.name = name

    def __str__(self):
        return self.name

    def __eq__(self, other):
        if isinstance(other, Instructor):
            return self.id == other.id

        return self == other

class Group:
    def __init__(self, name, courses):
        self.name = name
        self.courses = courses

    def __str__(self):
        return self.name

