from fastapi import status, HTTPException
import pytest

import src.service.lesson_selector as lesson_selector


@pytest.mark.unittest
def test_default():
    expected_text = "ERROR: This lesson does not exist yet."
    expected_code = status.HTTP_422_UNPROCESSABLE_ENTITY

    with pytest.raises(HTTPException) as exc_info:
        lesson_selector.factory._default()

    assert expected_text == exc_info.value.detail
    assert expected_code == exc_info.value.status_code


@pytest.mark.unittest
def test_select_lesson_not_exists():
    expected_text = "ERROR: This lesson does not exist yet."
    expected_code = status.HTTP_422_UNPROCESSABLE_ENTITY

    with pytest.raises(HTTPException) as exc_info:
        lesson_selector.execute_lesson(-222, "run", "")

    assert expected_text == exc_info.value.detail
    assert expected_code == exc_info.value.status_code


@pytest.mark.unittest
def test_select_lesson_exists():
    error = "ERROR: This lesson does not exist yet."
    actual = lesson_selector.execute_lesson(1, "run", "")

    assert actual != ""
    assert actual != error
