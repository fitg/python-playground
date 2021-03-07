import pytest

import src.service.lesson_selector as lesson_selector


@pytest.mark.unittest
def test_default():
    expected = "ERROR: This lesson does not exist yet."
    actual = lesson_selector.default()

    assert expected == actual


@pytest.mark.unittest
def test_select_lesson_not_exists():
    expected = "ERROR: This lesson does not exist yet."
    actual = lesson_selector.select_lesson(-222)

    assert expected == actual


@pytest.mark.unittest
def test_select_lesson_exists():
    error = "ERROR: This lesson does not exist yet."
    actual = lesson_selector.select_lesson(1)

    assert actual != ""
    assert actual != error
