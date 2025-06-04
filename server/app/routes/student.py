from fastapi import APIRouter, HTTPException
from server.app.models import Student
from server.app.crud.student import create_student_record
from psycopg2.errors import UniqueViolation

router = APIRouter()

@router.post("/student")
def create_student(student: Student):
    try:
        create_student_record(student)
        return {"message": "Student created successfully"}
    except UniqueViolation:
        raise HTTPException(status_code=409, detail="Student already exists")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
