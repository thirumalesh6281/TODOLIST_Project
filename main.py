from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import snowflake.connector
import os

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # allow frontend (Netlify)
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class Task(BaseModel):
    task: str

def get_db_connection():
    conn = snowflake.connector.connect(
        user=os.getenv("SNOWFLAKE_USER"),
        password=os.getenv("SNOWFLAKE_PASSWORD"),
        account=os.getenv("SNOWFLAKE_ACCOUNT"),
        warehouse='COMPUTE_WH',
        database='TODO_APP',
        schema='TODO_APP_S'
    )
    return conn

@app.get("/tasks")
def get_tasks():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT ID, TASK FROM TODOS")
    rows = cursor.fetchall()
    cursor.close()
    conn.close()
    return [{"id": row[0], "task": row[1]} for row in rows]

@app.post("/tasks")
def add_task(new_task: Task):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO TODOS (TASK) VALUES (?)", (new_task.task,))
    conn.commit()
    cursor.close()
    conn.close()
    return {"message": "Task added successfully!"}

@app.delete("/tasks/{task_id}")
def delete_task(task_id: int):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM TODOS WHERE ID = ?", (task_id,))
    conn.commit()
    cursor.close()
    conn.close()
    return {"message": "Task deleted successfully!"}
