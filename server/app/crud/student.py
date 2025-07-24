from server.app.database import get_db
from server.app.models import Student
from fastapi import HTTPException

def create_student_record(student):
    conn = get_db()
    cur = conn.cursor()
    cur.execute("""
        INSERT INTO students (student_id, student_name, course, present_date)
        VALUES (%s, %s, %s, %s)
    """, (student.studentID, student.studentName, student.course, student.presentDate))
    conn.commit()
    cur.close()
    conn.close()

def update_student_record(student_id: str, updated: Student):
    conn = get_db()
    cur = conn.cursor()

    # Check if student exists
    cur.execute("SELECT * FROM students WHERE student_id = %s", (student_id,))
    if cur.fetchone() is None:
        cur.close()
        conn.close()
        raise HTTPException(status_code=404, detail="Student not found")

    #update student
    cur.execute("""
            UPDATE students SET
                student_name = %s,
                course = %s,
                present_date = %s
            WHERE student_id = %s
        """, (updated.studentName, updated.course, updated.presentDate, student_id))

    conn.commit()
    cur.close()
    conn.close()
    return {"message": "Student updated"}

def delete_student_record(student_id: str):
    conn = get_db()
    cur = conn.cursor()

    cur.execute("SELECT * FROM students WHERE student_id = %s", (student_id,))
    if cur.fetchone() is None:
        cur.close()
        conn.close()
        raise HTTPException(status_code=404, detail="Student does not exist")

    cur.execute("DELETE FROM students WHERE student_id = %s", (student_id,))
    conn.commit()
    cur.close()
    conn.close()
    return {"message": "Student deleted successfully"}
