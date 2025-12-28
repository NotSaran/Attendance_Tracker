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
