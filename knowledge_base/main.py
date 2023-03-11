from database import *


def guess_professor():
    demanding_professor = is_demanding_professor()
    lecturer = is_lecturer()
    if demanding_professor is True and lecturer is True:  # Return Ihor Zavadskiy or Iryna Verhunova
        is_professor_working_with_quantum_fact = is_professor_working_with_quantum()
        return list(fact_dictionary['works_with_quantum_male'].keys())[
            list(fact_dictionary['works_with_quantum_male'].values()).index(is_professor_working_with_quantum_fact)]
    if demanding_professor is False and lecturer is True:
        professor_department_fact = get_professor_department()
        if professor_department_fact != "MI":
            gender_male_fact = gender_male()
        if professor_department_fact == "TTP":  # return Stepan Shkilniak or Liudmyla Omelchuk
            return list(fact_dictionary['lecturers_ttp_male'].keys())[
                list(fact_dictionary['lecturers_ttp_male'].values()).index(gender_male_fact)]
        if professor_department_fact == "TC":  # return Andrii Stavrovskiy ir Tetiana Karnaukh
            return list(fact_dictionary['lecturers_tc_male'].keys())[
                list(fact_dictionary['lecturers_tc_male'].values()).index(gender_male_fact)]
        if professor_department_fact == "MI":  # return Bohdan Bobyl
            less_than_forty_fact = is_professor_less_than_forty()
            return list(fact_dictionary['lecturer_less_than_forty'].keys())[
                list(fact_dictionary['lecturer_less_than_forty'].values()).index(less_than_forty_fact)]
    if demanding_professor is False and lecturer is False:
        prof_works_with_ml_fact = is_professor_working_with_ml()  # return Serhii Kondratiuk or Nataliia Polishchuk
        return list(fact_dictionary['non_lecturer_is_working_with_ml'].keys())[
                list(fact_dictionary['non_lecturer_is_working_with_ml'].values()).index(prof_works_with_ml_fact)]
    return "Such professor does not exist"



if __name__ == "__main__":
    print("----------------------------------------------------------------------------------------")
    print("Let's play a game. I will try to guess the professor's name and surname from this list:")
    print("Ihor Zavadskyi, Iryna Vergunova, Stepan Shkilniak, Liudmyla Omelchuk, Andrii Stavrovskyi")
    print("Tetiana Karnaukh, Bohdan Bobyl, Serhii Kondratiuk, Nataliia Polishchuk")
    print("----------------------------------------------------------------------------------------")
    professor = guess_professor()
    print("----------------------------------------------------------------------------------------")
    print(f"This is {professor}.")
    print("----------------------------------------------------------------------------------------")