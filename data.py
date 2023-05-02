from model import (Course, Group, Instructor, MeetingTime, Room)

class Data:
    ROOMS = [["Room 1", 50], ["Room 2", 40], ["Room 3", 30]]

    INSTRUCTORS = [
        ["Ins1", "Ivan Ivanovych"],
        ["Ins2", "Vasyl Vasylyovych"],
        ["Ins3", "Bohdan Bohdanovych"],
        ["Ins4", "Mykola Mykolovych"],
        ["Ins5", "Petro Petrovych"],
        ["Ins6", "Oleksandr Oleksandrovych"],
        ["Ins7", "Dmytro Dmytrovych"]
    ]

    MEETING_TIMES = [
        [1, "Monday 08:40 - 10:20"],
        [2, "Monday 10:35 - 12:10"],
        [3, "Monday 12:20 - 13:55"],
        [4, "Tuesday 08:40 - 10:20"],
        [5, "Tuesday 10:35 - 12:10"],
        [6, "Tuesday 12:20 - 13:55"],
        [7, "Wednesday 08:40 - 10:20"],
        [8, "Wednesday 10:35 - 12:10"],
        [9, "Wednesday 12:20 - 13:55"]
    ]

    def __init__(self):
        self.rooms = []
        self.instructors = []
        self.meeting_times = []
        self.courses = []
        self.groups = []
        self.number_of_classes = []


        for room in self.ROOMS:
            self.rooms.append(Room(number=room[0], seating_capacity=room[1]))
        for meeting_time in self.MEETING_TIMES:
            self.meeting_times.append(MeetingTime(id=meeting_time[0], time=meeting_time[1]))
        for instructor in self.INSTRUCTORS:
            self.instructors.append(Instructor(id=instructor[0], name=instructor[1]))

        calculus = Course(
            number="L1",
            name="Calculus (lectures)",
            instructors=[self.instructors[0]],
            max_number_of_students=45
        )
        calculus_practice = Course(
            number="P1",
            name="Calculus (practice)",
            instructors=[self.instructors[0], self.instructors[1]],
            max_number_of_students=25
        )
        linear_algebra = Course(
            number="L2",
            name="Linear Algebra (lectures)",
            instructors=[self.instructors[2]],
            max_number_of_students=36
        )
        linear_algebra_practice = Course(
            number="P2",
            name="Linear Algebra (practice)",
            instructors=[self.instructors[2], self.instructors[3], self.instructors[4]],
            max_number_of_students=28
        )
        programming_lectures = Course(
            number="L3",
            name="Programming (lecture)",
            instructors=[self.instructors[5], self.instructors[6]],
            max_number_of_students=32
        )
        programming_practice = Course(
            number="P3",
            name="Programming (practice)",
            instructors=[self.instructors[1], self.instructors[5], self.instructors[6]],
            max_number_of_students=30
        )
        operations_research = Course(
            number="L4",
            name="Operations Research (lectures)",
            instructors=[self.instructors[6]],
            max_number_of_students=24
        )
        operation_research_practice = Course(
            number="P4",
            name="Operations Research (practice)",
            instructors=[self.instructors[6]],
            max_number_of_students=15
        )
        management = Course(
            number="L5",
            name="Management",
            instructors=[self.instructors[1]],
            max_number_of_students=27
        )
        cloud_technologies_lecture = Course(
            number="L6",
            name="Cloud (lectures)",
            instructors=[self.instructors[5]],
            max_number_of_students=35
        )
        algorithmic_complexity = Course(
            number="L7",
            name="Algorithmic complexity",
            instructors=[self.instructors[3]],
            max_number_of_students=45
        )
        quantum_computations = Course(
            number="L8",
            name="Quantum Computations (lectures)",
            instructors=[self.instructors[4]],
            max_number_of_students=50
        )

        self.courses = [
            calculus,
            calculus_practice,
            linear_algebra,
            linear_algebra_practice,
            programming_lectures,
            programming_practice,
            operations_research,
            operation_research_practice,
            management,
            cloud_technologies_lecture,
            algorithmic_complexity,
            quantum_computations
        ]

        group1 = Group(
            name="Group1",
            courses=[linear_algebra, linear_algebra_practice, operations_research, operation_research_practice,]
        )
        group2 = Group(
            name="Group2",
            courses=[linear_algebra, linear_algebra_practice, management]
        )
        group3 = Group(
            name="Group3",
            courses=[programming_lectures, programming_practice, algorithmic_complexity,]
        )
        group4 = Group(
            name="Group4",
            courses=[programming_lectures, programming_practice, management]
        )
        group5 = Group(
            name="Group5",
            courses=[calculus, calculus_practice, cloud_technologies_lecture, quantum_computations]
        )

        self.groups = [
            group1,
            group2,
            group3,
            group4,
            group5
        ]

        self.number_of_classes = sum([len(x.courses) for x in self.groups])
