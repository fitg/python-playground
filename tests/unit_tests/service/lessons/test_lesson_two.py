from pathlib import Path

from fastapi import status, HTTPException
import pytest

import src.service.lessons.lesson_two as lesson_two


@pytest.mark.unittest
def test_execute_method_fails():
    expected_text = "ERROR: Action not allowed: run for lesson 2"
    expected_code = status.HTTP_422_UNPROCESSABLE_ENTITY

    interface = lesson_two.LessonTwoInterface()

    with pytest.raises(HTTPException) as exc_info:
        interface.execute("run", "")

    assert expected_text == exc_info.value.detail
    assert expected_code == exc_info.value.status_code


@pytest.mark.unittest
def test_execute_load_data_success():

    interface = lesson_two.LessonTwoInterface()

    actual = interface._load_data(str(Path(__file__).parent / "test_files/winequality-white.csv"))

    assert actual.empty == False  # noqa: E712
    assert len(actual) == 15
