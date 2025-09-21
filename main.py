
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import snowflake.connector

app = FastAPI()

# Allow frontend (CORS)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Pydantic model for request body
class Task(BaseModel):
    task: str

# Database connection
def get_db_connection():
    conn = snowflake.connector.connect(
        user='thirumal',
        password='@Thirumalesh905',
        account='OAFQQFS-HAA39051',  # e.g., xy12345.east-us-2.azure
        warehouse='COMPUTE_WH',
        database='TODO_APP',
        schema='TODO_APP_S'
    )
    return conn

# Get all tasks
@app.get("/tasks")
def get_tasks():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT ID, TASK FROM TODOS")
    rows = cursor.fetchall()
    cursor.close()
    conn.close()
    return [{"id": row[0], "task": row[1]} for row in rows]

# Add a task
@app.post("/tasks")
def add_task(new_task: Task):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO TODOS (TASK) VALUES (%s)", (new_task.task,))
    cursor.close()
    conn.close()
    return {"message": "Task added successfully!"}

# Delete a task
@app.delete("/tasks/{task_id}")
def delete_task(task_id: int):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM TODOS WHERE ID = %s", (task_id,))
    cursor.close()
    conn.close()
    return {"message": "Task deleted successfully!"}
