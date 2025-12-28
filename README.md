📊 Attendance Tracker System

📌 Objectives

To design and implement a RESTful backend using FastAPI

To manage academic and attendance data using a relational database

To perform CRUD operations on students, courses, enrollments, and attendance

To analyze student attendance and performance using interactive dashboards

To demonstrate advanced programming, API design, and database concepts



🛠️ Technology Stack

Backend Framework: FastAPI

Programming Language: Python

Database: SQLite (easily extendable to PostgreSQL)

ORM: SQLAlchemy

Dashboard & Visualization: Dash, Plotly

API Documentation: Swagger UI (OpenAPI)



🚀 Features

🔹 Backend Features

Create, read, update, and delete students

Create, read, update, and delete courses

Manage student enrollments

Attendance management (CRUD operations)

Mark attendance (Present/Absent)

Update attendance records

Delete attendance entries

Retrieve attendance history

Track individual student attendance and performance

RESTful API architecture

Automatic API documentation using Swagger UI


🔹 Dashboard Features

Course-wise attendance visualization

Student-wise attendance progress tracking

Attendance percentage analytics

Interactive charts and graphs

Real-time data reflection from the database



🧱 Project Architecture

FastAPI

Handles backend logic and REST API endpoints

SQLAlchemy

Manages ORM-based database interactions

Dash

Fetches data from the backend/database

Renders interactive dashboards using Plotly

SQLite

Stores students, courses, enrollments, and attendance records

Modular Project Structure

Ensures maintainability, scalability, and clean separation of concerns



📂 Modules Overview

Student Module – Manages student information

Course Module – Handles course data

Enrollment Module – Maps students to courses

Attendance Module – Records and manages attendance data

Dashboard Module – Visual analytics and insights


# Course Tracker API

This is a FastAPI-based application for tracking courses, students, enrollments, attendance, and performance.

## Setup

1. Create a virtual environment:
   ```
   python -m venv .venv
   ```

2. Activate the virtual environment:
   - On Windows: `.venv\Scripts\activate`
   - On macOS/Linux: `source .venv/bin/activate`

3. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

## Running the Application

**Important:** You must run the command from the `course_tracker` directory, not from the parent directory.

1. Navigate to the `course_tracker` directory:
   ```
   cd course_tracker
   ```

2. Run the application:
   ```
   python -m uvicorn app.main:app
   ```

The server will start on `http://127.0.0.1:8000`.

**Alternative:** If you prefer to run from the parent directory, use:
```
python -m uvicorn course_tracker.app.main:app --app-dir .
```

## API Documentation

Once the server is running, visit `http://127.0.0.1:8000/docs` for interactive API documentation.

## Database

The application uses SQLite database (`attendance_tracker.db`) which is created automatically on first run.


