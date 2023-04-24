from definitions import *

class Data:
    # Available rooms, with number and capacity
    ROOMS = [["101", 120], ["102", 35], ["103", 120]]
    # Available days
    DAYS = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
    # Possible class times
    CLASS_TIMES = ["08:40 - 10:15", "10:35 - 12:10", "12:20 - 13:55"]
    # Available teachers, with id and name
    TEACHERS = [["1", "Golubeva K.M."], ["2", "Marynych O.V."],
                ["3", "Chentsov O.I."], ["4", "Shishatska O.V."], ["5", "Cholyi V.Y."],
                ["6", "Livinska G.V."], ["7", "Karnaukh T.O."], ["8", "Panchenko T.V."],
                ["9", "Petrushchenkov S.P."], ["10", "Zavadsky I.O."], ["11", "Slabospytskyi O.S."],
                ["12", "Dolenko G.O."], ["13", "Veres M.M."],
                ["14", "Kashpur O.F."], ["15", "Pichkur V.V."], ["16", "Mostovy V.S."], ["17", "Korobova M.V."], ["18", "Veres M.M."]]

    def __init__(self):
        self._rooms = []
        self._meeting_times = []
        self._teachers = []
        self._days = []
        self._courses = []

        # Loop through the indices of the ROOMS list and create a Room object for each room,
        # using the name and capacity values from the ROOMS list, and append the new object to the _rooms list.
        for i in range(0, len(self.ROOMS)):
            self._rooms.append(Room(self.ROOMS[i][0], self.ROOMS[i][1]))

        # Loop through the indices of the TEACHERS list and create a Teacher object for each teacher,
        # using the name and max_hours values from the TEACHERS list, and append the new object to the _teachers list.
        for i in range(0, len(self.TEACHERS)):
            self._teachers.append(Teacher(self.TEACHERS[i][0], self.TEACHERS[i][1]))

        # Loop through the indices of the CLASS_TIMES list and create a ClassTime object for each time,
        # using the time value from the CLASS_TIMES list, and append the new object to the _meeting_times list.
        for i in range(0, len(self.CLASS_TIMES)):
            self._meeting_times.append(ClassTime(self.CLASS_TIMES[i]))

        # Loop through the indices of the DAYS list and create a Day object for each day,
        # using the day value from the DAYS list, and append the new object to the _days list.
        for i in range(0, len(self.DAYS)):
            self._days.append(Day(self.DAYS[i]))

        # Fill in the courses array
        self._courses.append(Subject("1", "Numerical methods", [self._teachers[0]], 100, "IPS"))
        self._courses.append(Subject("2", "Computer networks", [self._teachers[0]], 35, "IPS", True))
        self._courses.append(Subject("3", "Algebraic structures", [self._teachers[1]], 35, "IPS", True))
        self._courses.append(Subject("4", "Operational systems", [self._teachers[2]], 100, "IPS"))
        self._courses.append(Subject("5", "Theory of programming", [self._teachers[3]], 35, "IPS", True))
        self._courses.append(Subject("6", "Scientific image of the world", [self._teachers[4]], 35, "IPS", True))
        self._courses.append(Subject("7", "Probability theory", [self._teachers[5]], 100, "IPS"))
        self._courses.append(Subject("8", "Programming paradigms", [self._teachers[6]], 100, "IPS"))
        self._courses.append(Subject("9", "WEB technologies", [self._teachers[7]], 100, "IPS"))
        self._courses.append(Subject("10", "Philosophy", [self._teachers[8]], 100, "IPS"))
        self._courses.append(Subject("11", "Theory of quantum computing", [self._teachers[9]], 35, "IPS", True))
        self._courses.append(Subject("12", "Data Analysis", [self._teachers[10]], 100, "DO"))
        self._courses.append(Subject("13", "System optimization", [self._teachers[11]], 35, "DO"))
        self._courses.append(Subject("14", "Theory of functions of a complex variable",
                                    [self._teachers[12]], 35, "DO", True))
        self._courses.append(Subject("15", "Basics of calculation methods", [self._teachers[0]], 35, "DO", True))
        self._courses.append(Subject("16", "Equations of mathematical physics", [self._teachers[13]], 35, "DO", True))
        self._courses.append(Subject("17", "Management theory", [self._teachers[14]], 35, "DO"))
        self._courses.append(Subject("18", "AI models and algorithms", [self._teachers[15]], 35, "DO", True))
        self._courses.append(Subject("19", "Databases and information systems", [self._teachers[16]], 35, "DO"))
        self._courses.append(Subject("20", "Ecological and economic processes", [self._teachers[17]], 35, "DO", True))
        self._courses.append(Subject("21", "Ruby programming", [self._teachers[17]], 35, "DO", True))

        FKNK = Department(["FKNK"], self._courses)
        self._depts = [FKNK]

        self._numberOfClasses = 0
        for i in range(0, len(self._depts)):
            self._numberOfClasses += len(self._depts[i].get_subjects())

    def get_rooms(self):
        return self._rooms

    def get_teachers(self):
        return self._teachers

    def get_subjects(self):
        return self._courses

    def get_depts(self):
        return self._depts

    def get_class_times(self):
        return self._meeting_times

    def get_days(self):
        return self._days

    def get_num_of_classes(self):
        return self._numberOfClasses
