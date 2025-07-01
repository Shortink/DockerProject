from fastapi import APIRouter, HTTPException
from server.app.models import Student
from server.app.crud.student import create_student_record, update_student_record
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

@router.put("/student/{student_id}")
def update_student( student_id: str, student: Student):
    try:
        update_student_record(student_id, student)
        return {"message": "Student updated successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
