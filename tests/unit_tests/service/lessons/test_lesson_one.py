from fastapi import status, HTTPException
import pytest

import src.service.lessons.lesson_one as lesson_one


@pytest.mark.unittest
def test_hello_world():
    expected = "Hello World!"
    actual = lesson_one.hello_world()

    assert expected == actual


@pytest.mark.unittest
def test_why_python():
    expected = """
        Tcl -- It is short (only three letters) and does a suprising
            amount given that it doesn't have a vowel.  It can be
            pronounced "Tickle", which is a command.

        Perl -- Bigger and has a vowel.  However you'll note that it isn't
            a common english word; you'll have to know what you're doing to
            use it, especially with spell-checkers which otherwise complain
            that it looks like noise.

        Python -- This is a Real English Word (honest, look it up!) that
            happens to refer to a type of snake, which you'll notice is an
            object.  With the two vowels, python is quite readable.
    """
    actual = lesson_one.why_python()

    assert expected == actual


@pytest.mark.unittest
def test_mutable_default_attributes():
    expected = ["New", "New", "New", "New"]

    actual = lesson_one.mutable_default_attributes()
    assert len(actual) == len(expected)
    assert all([a == b for a, b in zip(actual, expected)])


@pytest.mark.unittest
def test_enumerator_over_range():
    actual = lesson_one.enumerator_over_range()
    assert actual != ""


@pytest.mark.unittest
def test_execute_method_fails():
    expected_text = "ERROR: Action not allowed: describe for lesson 1"
    expected_code = status.HTTP_422_UNPROCESSABLE_ENTITY

    interface = lesson_one.LessonOneInterface()

    with pytest.raises(HTTPException) as exc_info:
        interface.execute("describe", "")

    assert expected_text == exc_info.value.detail
    assert expected_code == exc_info.value.status_code
