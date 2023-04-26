import numpy as np
import time
import random
from tabulate import tabulate

DAYS = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]

GROUPS = ["IPS", "DO", "TTP"]

SUBJECTS = [
    # "Numerical methods", 
    # "Computer networks", 
    # "Algebraic structures", 
    # "Operational systems",
    # "Discrete Math",
    # "Theory of programming",
    # "Scientific image of the world",
    # "Probability theory",
    # "Programming paradigms",
    # "WEB technologies",
    # "Philosophy",
    # "Theory of quantum computing",
    # "Data Analysis",
    # "System optimization",
    # "Theory of functions of a complex variable",
    # "Basics of calculation methods",
    "Equations of mathematical physics",
    "Management theory",
    "AI models and algorithms",
    "Databases and information systems",
    "Ecological and economic processes",
    "Ruby programming"
]

TEACHERS = [
    # "Golubeva K.M.",
    # "Marynych O.V.",
    # "Chentsov O.I.",
    # "Shishatska O.V.",
    # "Cholyi V.Y.",
    # "Livinska G.V.",
    # "Karnaukh T.O.",
    # "Panchenko T.V.",
    # "Petrushchenkov S.P.",
    "Zavadsky I.O.",
    "Slabospytskyi O.S.",
    "Dolenko G.O.",
    "Veres M.M.",
    "Kashpur O.F.",
    "Pichkur V.V.",
    "Mostovy V.S.",
    "Korobova M.V.",
    "Veres M.M."
]

CLASS_TIMES = ["08:40 - 10:15", "10:35 - 12:10", "12:20 - 13:55", "14:05 - 15:40"]

ROOMS = ["101", "102", "103", "1", "7"]


class Schedule:
    n_days = len(DAYS)
    n_lessons = len(CLASS_TIMES)
    total_lessons = n_days * n_lessons

    n_teachers = len(TEACHERS)
    n_groups = len(GROUPS)
    n_rooms = len(ROOMS)
    n_subjects = len(SUBJECTS)

    # Used for random generation
    subs_per_teacher = 4  # number of subjects per teacher
    subs_per_group = 3  # number of subjects per group

    def __init__(self):
        self.rooms = ROOMS
        self.groups = GROUPS[:self.n_groups]
        self.subjects = SUBJECTS[:self.n_subjects]
        self.teachers = TEACHERS[:self.n_teachers]

        # Every second room will be called a laboratory
        self.rooms_dests = ["lec"] * self.n_rooms
        for i in range(0, self.n_rooms, 2):
            self.rooms_dests[i] = "lab"

        # subjects teacher cat teach
        self.teacher_skills = []
        for ti in range(self.n_teachers):
            self.teacher_skills.append(set())
            for si in range(self.subs_per_teacher):
                # Semi-random distribution
                self.teacher_skills[ti].add((si ** 2 + ti ** 2) % self.n_subjects)
        
        # The subjects to be taught to each group
        self.subs_for_groups = []        
        for gi in range(self.n_groups):
            self.subs_for_groups.append(set())
            for si in range(self.subs_per_group):
                self.subs_for_groups[gi].add((si ** 2 + gi) % self.n_subjects)

        # room per lesson per group
        self.rpl = [[None] * self.n_groups for _ in range(self.total_lessons)]

        # subject per lesson per group
        self.spl = [[None] * self.n_groups for _ in range(self.total_lessons)]

        # teacher per lesson per group
        self.tpl = [[None] * self.n_groups for _ in range(self.total_lessons)]

        self.cnt = 0

    def is_complete(self):
        for l in self.rpl:
            if any(r is None for r in l):
                return False
        return True

    def check_constraints(self):
        self.cnt += 1

        if self.cnt > 1e6:
            return False
    
        # Constraint 1: Check if each class has both labs and lectures
        if self.is_complete():
            for group in range(self.n_groups):
                classes_per_subjects = {subject: set() for subject in self.subs_for_groups[group]}
                for lesson in range(self.total_lessons):
                    classes_per_subjects[self.spl[lesson][group]].add(self.rooms_dests[self.rpl[lesson][group]])
                if any([len(classes) != 2 for classes in classes_per_subjects.values()]):
                    return False
                
        # Constraint 2: Check if each teacher can teach only 1 group at a time
        for teacher_group in self.tpl:
            for i in range(self.n_groups - 1):
                if teacher_group[i] is not None and teacher_group[i] in teacher_group[i + 1:]:
                    return False
        
        # Constraint 3: Check if each room can be used only by 1 group at a time
        for room_group in self.rpl:
            for i in range(self.n_groups - 1):
                if room_group[i] is not None and room_group[i] in room_group[i + 1:]:
                    return False
        
        # Constraints 4 and 5 are already specified in the backtracking method
        
        # Constraint 6: Check if each group can only visit 1 class at a time
        # This constraint is already maintained by the code structure

        return True

    def setter(self, lesson, group, teacher, room, subject):
        self.tpl[lesson][group] = teacher
        self.rpl[lesson][group] = room
        self.spl[lesson][group] = subject

    def select_unassigned_var(self):
        for lesson in range(self.total_lessons):
            for group in range(self.n_groups):
                if self.tpl[lesson][group] is None:
                    return lesson, group

    def degree_heuristic(self):
        none_count = []
        for lesson in range(self.total_lessons):
            count = sum([self.tpl[lesson][group] is None for group in range(self.n_groups)])
            none_count.append(count)
        lesson_index = none_count.index(max(none_count))
        for group in range(self.n_groups):
            if self.tpl[lesson_index][group] is None:
                return lesson_index, group
    
    def mrv(self):
        for day in range(self.n_days):
            for lesson in range(self.n_lessons):
                lesson_index = day * self.n_lessons + lesson
                for group in range(self.n_groups):
                    if self.tpl[lesson_index][group] is None:
                        return lesson_index, group

    def order_domain_vals(self, group):
        for teacher in random.sample(range(self.n_teachers), self.n_teachers):
            available_subjects = list(self.subs_for_groups[group].intersection(self.teacher_skills[teacher]))
            for room in random.sample(range(self.n_rooms), self.n_rooms):
                for subject in random.sample(available_subjects, len(available_subjects)):
                    yield teacher, room, subject

    def lcv(self, group):
        teacher_scores = []
        for teacher in range(self.n_teachers):
            score = 0
            for other_group in range(self.n_groups):
                if other_group != group:
                    score += len(self.teacher_skills[teacher].intersection(self.subs_for_groups[other_group]))
            teacher_scores.append([score, teacher])
        for _, teacher in sorted(teacher_scores):
            available_subjects = list(self.subs_for_groups[group].intersection(self.teacher_skills[teacher]))
            for room in random.sample(range(self.n_rooms), self.n_rooms):
                for subject in random.sample(available_subjects, len(available_subjects)):
                    yield teacher, room, subject

    def forward_check(self, lesson, group):
        for teacher in random.sample(range(self.n_teachers), self.n_teachers):
            if teacher not in self.tpl[lesson]:
                available_subjects = list(self.subs_for_groups[group].intersection(self.teacher_skills[teacher]))
                for room in random.sample(range(self.n_rooms), self.n_rooms):
                    if room not in self.rpl[lesson]:
                        for subject in random.sample(available_subjects, len(available_subjects)):
                            yield teacher, room, subject

    def backtracking(self):
        unassigned_var = self.select_unassigned_var()  # self.mrv()  # self.degree_heuristic() 
        if unassigned_var is None:
            return True

        lesson, group = unassigned_var

        for teacher, room, subject in self.order_domain_vals(group):  # self.forward_check(lesson, group): # self.lcv(group):
            self.setter(lesson, group, teacher, room, subject)
            if self.check_constraints():
                result = self.backtracking()
                if result:
                    return True
            self.setter(lesson, group, None, None, None)
        return False

    def print_timetable(self):
        table = {"indices": ["Day", "Group"] + list(range(1, self.n_lessons + 1))}
        for day in range(self.n_days):
            table[(day, 0)] = [DAYS[day]]
            for group in range(1, self.n_groups):
                table[(day, group)] = [""]
            for group in range(self.n_groups):
                table[(day, group)].append(GROUPS[group])
                for lesson in range(self.n_lessons):
                    lesson_index = day * self.n_lessons + lesson
                    lesson_desc = (f"{self.subjects[self.spl[lesson_index][group]]}\n"
                                f"({self.rooms_dests[self.rpl[lesson_index][group]]})\n"
                                f"Room: {self.rooms[self.rpl[lesson_index][group]]}\n"
                                f"Prof.: {self.teachers[self.tpl[lesson_index][group]]}")
                    table[(day, group)].append(lesson_desc)
            table[(day, -1)] = [""] * (2 + self.n_lessons)
        print(tabulate(table, tablefmt="fancy_grid"))

# not_finished = 0
# total = 0
# for i in range(100):
#     print(i)
#     csp = Schedule()
#     start = time.time()
#     csp.backtracking()
#     spent = time.time() - start
#     if csp.cnt <= 1e6:
#         total += spent
#     else:
#         not_finished += 1
# print(total)
# print(not_finished)
# quit()
csp = Schedule()

print("Start!")
start = time.time()
csp.backtracking()
print(f"Success! Time spent: {time.time() - start} s.")
print(f"Constraints checked {csp.cnt} times!")
csp.print_timetable()
