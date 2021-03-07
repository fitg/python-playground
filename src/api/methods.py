from fastapi import status, APIRouter
from fastapi.responses import JSONResponse
from pydantic import BaseModel, Field

from src.service.lesson_selector import select_lesson

router = APIRouter()


class LessonRequest(BaseModel):
    """Represents the lesson to be called"""

    lesson_number: int = Field(
        ...,
        description="lesson number request",
        example="example: 1",
    )


class LessonResponseText(BaseModel):
    """Represents a text stream response"""

    response_text: str = Field(
        ...,
        description="raw lessons text",
        example="results of a lesson text",
    )


@router.get(
    "/health",
    status_code=status.HTTP_200_OK,
    responses={
        status.HTTP_200_OK: {
            "model": str,
            "content": {"application/json": {"healthy": True}},
        }
    },
    response_class=JSONResponse,
)
async def check_health():
    """Healthcheck endpoint; returns 200 if all is ok."""
    return {"healthy": True}


@router.post(
    "/lesson",
    status_code=status.HTTP_200_OK,
    response_model=LessonResponseText,
    responses={
        status.HTTP_200_OK: {
            "model": LessonResponseText,
            "description": "return the text to the caller",
        }
    },
    response_class=JSONResponse,
)
async def return_lesson(lesson_number: LessonRequest):
    """returns lessons"""
    return {"response_text": select_lesson(lesson_number.lesson_number)}
