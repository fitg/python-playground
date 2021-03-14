from fastapi import status, HTTPException
import pandas

from src.service.lesson_interface import LessonsInterface

DEFAULT_SEPARATOR = ";"


class LessonTwoInterface(LessonsInterface):
    white_wine: None

    def execute(self, action: str, url: str) -> str:
        """Overrides LessonsInterface.execute()"""
        if action == "describe":
            return self._run_lesson_two(url)
        else:
            # following fast api choice of 422 over 400 --> https://github.com/tiangolo/fastapi/issues/643
            raise HTTPException(
                status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, detail=f"ERROR: Action not allowed: {action} for lesson 2"
            )

    def _load_data(self, url: str) -> pandas.Series:
        white_wine = pandas.read_csv(url, sep=DEFAULT_SEPARATOR)
        return white_wine
        # red_wine =
        # pandas.read_csv("http://archive.ics.uci.edu/ml/machine-learning-databases/wine-quality/winequality-red.csv", sep=';')

    def _run_lesson_two(self, url: str) -> str:
        return str(self._load_data(url).describe())
