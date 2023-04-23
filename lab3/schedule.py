import random as rnd
import numpy as np
from definitions import *

# Class representing a schedule
class Schedule:
    def __init__(self, data):
        self._data = data
        self._classes = []
        self._num_of_conflicts = 0
        self._fitness = -1
        self._class_num = 0
        # Whether the fitness value needs to be recalculated
        self._fitness_changed = True

    def get_classes(self):
        self._fitness_changed = True
        return self._classes

    def get_num_of_conflicts(self):
        return self._num_of_conflicts

    def get_fitness(self):
        # If the fitness value needs to be recalculated, calculate it
        if self._fitness_changed is True:
            self._fitness = self.calculate_fitness()
            self._fitness_changed = False
        return self._fitness

    def initialize(self):  # Define the classes objects Data
        depts = self._data.get_depts()
        for i in range(0, len(depts)):
            courses = depts[i].get_subjects()
            # Randomly assign subjects to classes
            for j in range(0, len(courses)):
                new_class = Class(self._class_num, depts[i], courses[j])
                self._class_num += 1
                new_class.set_meeting_time(
                    self._data.get_class_times()[rnd.randrange(0, len(self._data.get_class_times()))])
                new_class.set_day(self._data.get_days()[
                                  rnd.randrange(0, len(self._data.get_days()))])
                new_class.set_room(self._data.get_rooms()[
                                   rnd.randrange(0, len(self._data.get_rooms()))])
                new_class.set_instructor(
                    courses[j].get_teachers()[rnd.randrange(0, len(courses[j].get_teachers()))])
                self._classes.append(new_class)
        return self

    # Calculate the fitness value of the schedule.
    # The higher the fitness value, the better the schedule.
    # The fitness value is calculated as 1 / (1.0 * _num_of_conflicts + 1), i.e. the maximal fitness value is 1.0.
    def calculate_fitness(self):
        self._num_of_conflicts = 0
        classes = self.get_classes()
        for i in range(0, len(classes)):
            # Check if the number of students in a class is greater than the capacity of the room
            if classes[i].get_room().get_capacity() < classes[i].get_course().get_max_num_of_students():
                self._num_of_conflicts += 1
            # Check if there are two classes at the same time in the same room
            for j in range(i, len(classes)):
                if (classes[i].get_meeting_time() == classes[j].get_meeting_time()
                        and classes[i].get_id() != classes[j].get_id()
                        and classes[i].get_course().get_grade() == classes[j].get_course().get_grade()
                        and classes[i].get_day() == classes[j].get_day()):
                    if (np.any(np.in1d(classes[j].get_dept().get_name(),
                                       classes[i].get_dept().get_name()))
                        ):
                        self._num_of_conflicts += 1
                if classes[i].get_meeting_time() == classes[j].get_meeting_time() \
                    and classes[i].get_day() == classes[
                        j].get_day() and classes[i].get_id() != classes[j].get_id():
                    if classes[i].get_teacher().get_name() == classes[j].get_teacher().get_name():
                        self._num_of_conflicts += 1

                if (classes[i].get_meeting_time() == classes[j].get_meeting_time()
                        and classes[i].get_id() != classes[j].get_id()
                        and classes[i].get_day() == classes[j].get_day()):
                    if classes[i].get_room() == classes[j].get_room():
                        self._num_of_conflicts += 1
                
        return 1 / (1.0 * self._num_of_conflicts + 1)

    def __str__(self):
        value = ""
        for i in range(0, len(self._classes) - 1):
            value += str(self._classes[i]) + ", "
        value += str(self._classes[len(self._classes) - 1])
        return value
