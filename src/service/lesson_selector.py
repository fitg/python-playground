from src.service.lessons.lesson_one import run_lesson_one

lessons_dict = {
    1: run_lesson_one,
}


def select_lesson(lesson_number: int):
    return lessons_dict.get(lesson_number, default)()


# If user enters invalid option then this method will be called
def default():
    return "ERROR: This lesson does not exist yet."
