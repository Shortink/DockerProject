from server.app.database import get_db

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
