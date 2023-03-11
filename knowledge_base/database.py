def gender_male():
    answer = input("Is professor male? (Enter yes or no): ")
    if answer == "yes":
        return True
    elif answer == "no":
        return False
    else:
        return None


def is_professor_working_with_ml():
    answer = input("Does professor work with ML? (enter yes or no): ")
    if answer == "yes":
        return True
    elif answer == "no":
        return False
    else:
        return None


def is_professor_working_with_quantum():
    answer = input("Does professor work with quantum computations? (Enter yes or no): ")
    if answer == "yes":
        return True
    elif answer == "no":
        return False
    else:
        return None



def is_demanding_professor():
    answer = input("Is professor demanding? (Enter yes or no): ")
    if answer == "yes":
        return True
    elif answer == "no":
        return False
    else:
        return None



def is_professor_less_than_forty():
    answer = input("Is professor less than forty? (Enter yes or no): ")
    if answer == "yes":
        return True
    elif answer == "no":
        return False
    else:
        return None


def get_professor_department():
    answer = input("Please enter professor\'s department: (MI, TTP or TC): ")
    if answer == "MI":
        return "MI"
    if answer == "TTP":
        return "TTP"
    else:
        return "TC"


def is_lecturer():
        answer = input("Is professor's position lecturer or assistant professor? (Enter yes if lecturer or no otherwise): ")
        if answer == "yes":
            return True
        else:
            return False


fact_dictionary = {
    'works_with_quantum_male': {'Ihor Zavadskyi': True,
                                 'Iryna Verhunova': False},
    'lecturers_ttp_male': {'Stepan Shkilniak': True,
                           'Luidmyla Omelchuk': False},
    'lecturers_tc_male': {'Andrii Stavrovskyi': True,
                          'Tetiana Karnaukh': False},
    'lecturer_less_than_forty': {'Bohdan Bobyl': True},
    'non_lecturer_is_working_with_ml': {'Serhii Kondratiuk': True,
                                        'Nataliia Polishchuk': False}
}
