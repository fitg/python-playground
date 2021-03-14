from fastapi import status, HTTPException

from src.service.lessons.lesson_one import LessonOneInterface
from src.service.lessons.lesson_two import LessonTwoInterface


class LessonFactory:
    def get_lesson(self, lesson_number: int):
        if lesson_number == 1:
            return LessonOneInterface()
        elif lesson_number == 2:
            return LessonTwoInterface()
        else:
            self._default(lesson_number)

    # If user enters invalid option then this method will be called
    def _default(self, lesson_number: int):
        # following fast api choice of 422 over 400 --> https://github.com/tiangolo/fastapi/issues/643
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            detail=f"ERROR: This lesson does not exist yet lesson: {lesson_number}.",
        )


factory = LessonFactory()


def execute_lesson(lesson_number: int, action: str, url: str):
    interface = factory.get_lesson(lesson_number)
    return interface.execute(action, url)
