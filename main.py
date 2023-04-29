import csv

def get_input(path):
    csv_input = []

    with open(path, 'r', newline='') as file:
        reader = csv.reader(file)
        for row in reader:
            csv_input.append(row)

    return csv_input

def check(timeslot):
    global assigned_slots
    n = []

    for i in range(len(assigned_slots)):
        if assigned_slots[i] == timeslot:
            n.append(i)

    return n


def allocate_rooms(assigned_slots):
    global room_list

    rooms = []

    for i in range(len(assigned_slots)):
        rooms.append(room_list[assigned_slots[:i].count(assigned_slots[i])])

    return rooms

def backtrack():
    global domains, compulsory, assigned_slots, num_rooms, done

    if 0 not in assigned_slots:
        assigned_rooms = allocate_rooms(assigned_slots)
        output(assigned_slots, assigned_rooms)

        done = True
        return

    for i in range(len(assigned_slots)):
        if not assigned_slots[i]: n = i

    for timeslot in domains[n]:
        assigned_slots[n] = timeslot
        ok = True

        same_time_subjects = check(timeslot)

        if len(same_time_subjects) > num_rooms:
            ok = False

        if compulsory[n]:
            for subject in same_time_subjects:
                if compulsory[subject] and subject != n:
                    ok = False

        if ok:
            backtrack()

        if done:
            break

        assigned_slots[n] = 0

    return

def output(assigned_slots, assigned_rooms):
    global subjects

    for i in range(len(assigned_slots)):
        print("%s gets timeslot %s in Room %s" % (subjects[i], assigned_slots[i], assigned_rooms[i]))

done = False
subjects = []
assigned_slots = []
compulsory = []
domains = []
room_list = []
assigned_rooms = []

input_path = "data.csv"

csv_input = get_input(input_path)

for row in csv_input:
    subjects.append(row[0])

    c = 1 if row[1] == 'c' else 0
    compulsory.append(c)

    domains.append(row[2:])

subjects = subjects[:-1]
domains = domains[:-1]
compulsory = compulsory[:-1]

room_list = csv_input[-1]

num_rooms = len(room_list)
assigned_slots = [0 for i in subjects]

backtrack()

if not done:
    print("Problem impossible")