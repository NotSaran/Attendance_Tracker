from sqlalchemy.orm import Session
from . import models, schemas

# Course CRUD
def create_course(db: Session, course: schemas.CourseCreate):
    # Check if course with this name already exists
    existing_course = get_course_by_name(db, course.name)
    if existing_course:
        return existing_course
    db_course = models.Course(**course.dict())
    db.add(db_course)
    db.commit()
    db.refresh(db_course)
    return db_course

def get_course(db: Session, course_id: int):
    return db.query(models.Course).filter(models.Course.id == course_id).first()

def get_course_by_name(db: Session, name: str):
    return db.query(models.Course).filter(models.Course.name == name).first()

def get_courses(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Course).offset(skip).limit(limit).all()

def update_course(db: Session, course_id: int, course: schemas.CourseCreate):
    db_course = db.query(models.Course).filter(models.Course.id == course_id).first()
    if db_course:
        for key, value in course.dict().items():
            setattr(db_course, key, value)
        db.commit()
        db.refresh(db_course)
    return db_course

def delete_course(db: Session, course_id: int):
    db_course = db.query(models.Course).filter(models.Course.id == course_id).first()
    if db_course:
        db.delete(db_course)
        db.commit()
    return db_course

# Student CRUD
def create_student(db: Session, student: schemas.StudentCreate):
    # Check if student with this email already exists
    existing_student = get_student_by_email(db, student.email)
    if existing_student:
        return existing_student
    db_student = models.Student(**student.dict())
    db.add(db_student)
    db.commit()
    db.refresh(db_student)
    return db_student

def get_student(db: Session, student_id: int):
    return db.query(models.Student).filter(models.Student.id == student_id).first()

def get_student_by_email(db: Session, email: str):
    return db.query(models.Student).filter(models.Student.email == email).first()

def get_students(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Student).offset(skip).limit(limit).all()

def update_student(db: Session, student_id: int, student: schemas.StudentCreate):
    db_student = db.query(models.Student).filter(models.Student.id == student_id).first()
    if db_student:
        for key, value in student.dict().items():
            setattr(db_student, key, value)
        db.commit()
        db.refresh(db_student)
    return db_student

def delete_student(db: Session, student_id: int):
    db_student = db.query(models.Student).filter(models.Student.id == student_id).first()
    if db_student:
        db.delete(db_student)
        db.commit()
    return db_student

# Enrollment CRUD
def create_enrollment(db: Session, enrollment: schemas.EnrollmentCreate):
    # Check if enrollment with this student_id and course_id already exists
    existing_enrollment = get_enrollment_by_student_course(db, enrollment.student_id, enrollment.course_id)
    if existing_enrollment:
        return existing_enrollment
    db_enrollment = models.Enrollment(**enrollment.dict())
    db.add(db_enrollment)
    db.commit()
    db.refresh(db_enrollment)
    return db_enrollment

def get_enrollment(db: Session, enrollment_id: int):
    return db.query(models.Enrollment).filter(models.Enrollment.id == enrollment_id).first()

def get_enrollment_by_student_course(db: Session, student_id: int, course_id: int):
    return db.query(models.Enrollment).filter(
        models.Enrollment.student_id == student_id,
        models.Enrollment.course_id == course_id
    ).first()

def get_enrollments(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Enrollment).offset(skip).limit(limit).all()

def update_enrollment(db: Session, enrollment_id: int, enrollment: schemas.EnrollmentCreate):
    db_enrollment = db.query(models.Enrollment).filter(models.Enrollment.id == enrollment_id).first()
    if db_enrollment:
        for key, value in enrollment.dict().items():
            setattr(db_enrollment, key, value)
        db.commit()
        db.refresh(db_enrollment)
    return db_enrollment

def delete_enrollment(db: Session, enrollment_id: int):
    db_enrollment = db.query(models.Enrollment).filter(models.Enrollment.id == enrollment_id).first()
    if db_enrollment:
        db.delete(db_enrollment)
        db.commit()
    return db_enrollment

# Performance CRUD
def create_performance(db: Session, performance: schemas.PerformanceCreate):
    # Check if performance with this enrollment_id already exists
    existing_performance = get_performance_by_enrollment(db, performance.enrollment_id)
    if existing_performance:
        return existing_performance
    db_performance = models.Performance(**performance.dict())
    db.add(db_performance)
    db.commit()
    db.refresh(db_performance)
    return db_performance

def get_performance(db: Session, performance_id: int):
    return db.query(models.Performance).filter(models.Performance.id == performance_id).first()

def get_performance_by_enrollment(db: Session, enrollment_id: int):
    return db.query(models.Performance).filter(models.Performance.enrollment_id == enrollment_id).first()

def get_performances(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Performance).offset(skip).limit(limit).all()

def update_performance(db: Session, performance_id: int, performance: schemas.PerformanceCreate):
    db_performance = db.query(models.Performance).filter(models.Performance.id == performance_id).first()
    if db_performance:
        for key, value in performance.dict().items():
            setattr(db_performance, key, value)
        db.commit()
        db.refresh(db_performance)
    return db_performance

def delete_performance(db: Session, performance_id: int):
    db_performance = db.query(models.Performance).filter(models.Performance.id == performance_id).first()
    if db_performance:
        db.delete(db_performance)
        db.commit()
    return db_performance

# Attendance CRUD
def create_attendance(db: Session, attendance: schemas.AttendanceCreate):
    # Check if attendance with this enrollment_id and date already exists
    existing_attendance = get_attendance_by_enrollment_date(db, attendance.enrollment_id, attendance.date)
    if existing_attendance:
        return existing_attendance
    db_attendance = models.Attendance(**attendance.dict())
    db.add(db_attendance)
    db.commit()
    db.refresh(db_attendance)
    return db_attendance

def get_attendance(db: Session, attendance_id: int):
    return db.query(models.Attendance).filter(models.Attendance.id == attendance_id).first()

def get_attendance_by_enrollment_date(db: Session, enrollment_id: int, date):
    return db.query(models.Attendance).filter(
        models.Attendance.enrollment_id == enrollment_id,
        models.Attendance.date == date
    ).first()

def get_attendances(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Attendance).offset(skip).limit(limit).all()

def update_attendance(db: Session, attendance_id: int, attendance: schemas.AttendanceCreate):
    db_attendance = db.query(models.Attendance).filter(models.Attendance.id == attendance_id).first()
    if db_attendance:
        for key, value in attendance.dict().items():
            setattr(db_attendance, key, value)
        db.commit()
        db.refresh(db_attendance)
    return db_attendance

def delete_attendance(db: Session, attendance_id: int):
    db_attendance = db.query(models.Attendance).filter(models.Attendance.id == attendance_id).first()
    if db_attendance:
        db.delete(db_attendance)
        db.commit()
    return db_attendance
