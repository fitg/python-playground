import src.lessons.lesson_one as lesson_one


def run():
    run_lesson_one()


def run_lesson_one():
    print("1. Simple Hello World")
    print(lesson_one.hello_world())
    print("#######################################")
    print("")
    print("2. Why Python?")
    print(lesson_one.why_python())
    print("#######################################")
    print("")
    print(
        """3. Mutable default attributes - what do you get after calling
    a method with _add_elements(element=[]) more than once?"""
    )
    print(lesson_one.mutable_default_attributes())
    print("#######################################")
    print("")
    print("Is Enumerator better optimized than range?")
    print(lesson_one.enumerator_over_range())
    print("Yes, but if you dont need that index just use in <collection> syntax")
    print("#######################################")
    print("")
