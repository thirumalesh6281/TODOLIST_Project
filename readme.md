✅ To-Do List App (FastAPI + Snowflake + HTML/JS)

A simple To-Do List application built with:

Frontend → HTML, CSS, JavaScript (Vanilla JS)

Backend → FastAPI (Python)

Database → Snowflake Cloud Database

This project allows users to add, view, and delete tasks stored in Snowflake.

🛠 Tools & Technologies
Frontend

HTML, CSS, JavaScript → UI for managing tasks

Fetch API → calls backend endpoints

Backend

FastAPI → Python framework for REST APIs

Uvicorn → ASGI server to run FastAPI

Pydantic → request validation (task model)

CORS Middleware → allows frontend to access backend

Database

Snowflake Cloud Data Warehouse

Snowflake Python Connector → connects FastAPI backend to Snowflake

📦 Installation
1. Clone Repository

git clone https://github.com/your-username/todo-list-snowflake.git
cd todo-list-snowflake


2. Create Virtual Environment

python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate


3. Install Dependencies

pip install fastapi uvicorn snowflake-connector-python


🗄 Snowflake Setup

1 . Log in to Snowflake Web UI.

2 . Create a database:

CREATE DATABASE TODO_APP;

3 . Create a schema:

CREATE SCHEMA TODO_APP_S;

4 . Create a warehouse:

CREATE WAREHOUSE TODO_WH
  WITH WAREHOUSE_SIZE = 'XSMALL'
  AUTO_SUSPEND = 300
  AUTO_RESUME = TRUE;

5 . Create a table:

CREATE TABLE TODO_APP.TODO_APP_S.TODOS (
    ID INT AUTOINCREMENT PRIMARY KEY,
    TASK STRING NOT NULL
);


Run Backend

uvicorn main:app --reload


Backend will start at:
👉 http://127.0.0.1:8000

👉 API Docs: http://127.0.0.1:8000/docs

🚀 How It Works

User opens frontend (index.html)

Types a task → clicks "Add List".

Frontend sends request

POST /tasks with JSON { "task": "Buy milk" }.

Backend (FastAPI)

Receives request → validates with Task model.

Connects to Snowflake → inserts into TODOS table.

Fetching tasks

GET /tasks runs SELECT ID, TASK FROM TODOS.

Returns all tasks as JSON.

Deleting tasks

DELETE /tasks/{id} removes row from Snowflake.

✅ Now you have a full-stack To-Do List app with FastAPI backend, Snowflake database, and a HTML/JS frontend.
