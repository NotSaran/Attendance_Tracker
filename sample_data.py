from app.database import SessionLocal, engine, Base
import app.models  # IMPORTANT: this registers the models
from app import crud, schemas
from datetime import date, timedelta
import random

# Create database tables
Base.metadata.create_all(bind=engine)

def create_sample_data():
    db = SessionLocal()
    try:
        # Create sample courses
        courses = [
            ("Mathematics", "Basic Math Course"),
            ("Physics", "Introduction to Physics"),
            ("Computer Science", "Programming Fundamentals"),
            ("Chemistry", "General Chemistry"),
            ("Biology", "Introduction to Biology"),
            ("History", "World History"),
            ("English Literature", "Classic Literature"),
            ("Statistics", "Applied Statistics"),
            ("Economics", "Micro and Macro Economics"),
            ("Psychology", "Introduction to Psychology"),
            ("Art History", "Western Art History"),
            ("Music Theory", "Fundamentals of Music Theory")
        ]

        created_courses = []
        for name, desc in courses:
            course = crud.create_course(db, schemas.CourseCreate(name=name, description=desc))
            created_courses.append(course)

        # Create sample students
        students_data = [
            ("Alice Johnson", "alice@example.com"),
            ("Bob Smith", "bob@example.com"),
            ("Charlie Brown", "charlie@example.com"),
            ("Diana Prince", "diana@example.com"),
            ("Edward Norton", "edward@example.com"),
            ("Fiona Green", "fiona@example.com"),
            ("George Wilson", "george@example.com"),
            ("Helen Troy", "helen@example.com"),
            ("Ian McGregor", "ian@example.com"),
            ("Julia Roberts", "julia@example.com"),
            ("Kevin Hart", "kevin@example.com"),
            ("Laura Palmer", "laura@example.com"),
            ("Michael Scott", "michael@example.com"),
            ("Nancy Drew", "nancy@example.com"),
            ("Oliver Twist", "oliver@example.com"),
            ("Pam Beesly", "pam@example.com"),
            ("Quincy Jones", "quincy@example.com"),
            ("Rachel Green", "rachel@example.com")
        ]

        created_students = []
        for name, email in students_data:
            student = crud.create_student(db, schemas.StudentCreate(name=name, email=email))
            created_students.append(student)

        # Create sample enrollments (more varied enrollments)
        enrollments = []
        enrollment_data = [
            (0, 0), (0, 1), (0, 2), (0, 3),  # Alice in Math, Physics, CS, Chemistry
            (1, 1), (1, 2), (1, 4),           # Bob in Physics, CS, Biology
            (2, 2), (2, 5), (2, 6),           # Charlie in CS, History, English
            (3, 3), (3, 4), (3, 7),           # Diana in Chemistry, Biology, Statistics
            (4, 0), (4, 1), (4, 7),           # Edward in Math, Physics, Statistics
            (5, 5), (5, 6), (5, 8),           # Fiona in History, English, Economics
            (6, 2), (6, 7), (6, 9),           # George in CS, Statistics, Psychology
            (7, 8), (7, 9), (7, 10),          # Helen in Economics, Psychology, Art History
            (8, 0), (8, 3), (8, 4),           # Ian in Math, Chemistry, Biology
            (9, 1), (9, 2), (9, 5),           # Julia in Physics, CS, History
            (10, 6), (10, 8), (10, 11),       # Kevin in English, Economics, Music Theory
            (11, 7), (11, 9), (11, 10),       # Laura in Statistics, Psychology, Art History
            (12, 0), (12, 2), (12, 4),        # Michael in Math, CS, Biology
            (13, 1), (13, 3), (13, 6),        # Nancy in Physics, Chemistry, English
            (14, 5), (14, 7), (14, 8),        # Oliver in History, Statistics, Economics
            (15, 9), (15, 10), (15, 11),      # Pam in Psychology, Art History, Music Theory
            (16, 0), (16, 1), (16, 2),        # Quincy in Math, Physics, CS
            (17, 3), (17, 4), (17, 5)         # Rachel in Chemistry, Biology, History
        ]

        for student_idx, course_idx in enrollment_data:
            enrollment = crud.create_enrollment(db, schemas.EnrollmentCreate(
                student_id=created_students[student_idx].id,
                course_id=created_courses[course_idx].id
            ))
            enrollments.append(enrollment)

        # Create sample attendance records
        attendance_records = []
        start_date = date.today() - timedelta(days=30)  # Last 30 days

        for enrollment in enrollments:
            # Generate attendance for the last 30 days
            for i in range(30):
                attendance_date = start_date + timedelta(days=i)
                # Randomly decide if present or absent (80% present rate)
                status = 'present' if random.random() < 0.8 else 'absent'
                attendance = crud.create_attendance(db, schemas.AttendanceCreate(
                    enrollment_id=enrollment.id,
                    date=attendance_date,
                    status=status
                ))
                attendance_records.append(attendance)

        print(f"Sample data created successfully! Created {len(created_courses)} courses, {len(created_students)} students, {len(enrollments)} enrollments, and {len(attendance_records)} attendance records.")
    finally:
        db.close()

if __name__ == "__main__":
    create_sample_data()
