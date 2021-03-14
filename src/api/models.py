from typing import Optional

from pydantic import BaseModel, Field

MINIMAL_LESSON_NUMBER = 1
MAXIMUM_LESSON_NUMBER = 3
MAX_STR_LEN = 255
MIN_URL_LEN = 15
MAX_URL_LEN = MAX_STR_LEN


class LessonRequest(BaseModel):
    """Represents the lesson to be called"""

    lesson_number: int = Field(
        ...,
        description="lesson number request",
        example="lesson_number: 1",
        ge=MINIMAL_LESSON_NUMBER,
        le=MAXIMUM_LESSON_NUMBER,
    )
    data_url: Optional[str] = Field(
        description="URL from which data will be pulled from",
        example="data_url: http://archive.ics.uci.edu/ml/machine-learning-databases/wine-quality/winequality-white.csv",
        min_length=MIN_URL_LEN,
        max_length=MAX_URL_LEN,
        regex="((http|https)://)(www.)?[a-zA-Z0-9@:%._\\+~#?&//=]{2,256}\\.[a-z]{2,6}\\b([-a-zA-Z0-9@:%._\\+~#?&//=]*)",
    )
    action: Optional[str] = Field(
        description="Actions possible to be executed on an uploaded data set",
        example="action: describe",
        max_length=MAX_STR_LEN,
        regex="(describe|run)",
    )


class LessonResponseText(BaseModel):
    """Represents a text stream response"""

    response_text: str = Field(
        ...,
        description="raw lessons text",
        example="results of a lesson text",
    )
