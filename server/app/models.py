from pydantic import BaseModel

class Student(BaseModel):
    studentID: str
    studentName: str
    course: str
    presentDate: str