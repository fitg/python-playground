from fastapi import status, APIRouter
from fastapi.responses import JSONResponse

from src.service.lesson_selector import execute_lesson
from src.api.models import LessonRequest, LessonResponseText  # type: ignore

router = APIRouter()


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
async def return_lesson(lesson: LessonRequest):
    """returns lessons"""
    return {"response_text": execute_lesson(lesson.lesson_number, str(lesson.action), str(lesson.data_url))}
