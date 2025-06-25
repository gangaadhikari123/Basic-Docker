from fastapi import FastAPI, HTTPException
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
import sqlite3
import os

# Setup database path
DB_PATH = "data/app.db"

# Initialize FastAPI app
app = FastAPI()

# Serve static files (CSS)
app.mount("/static", StaticFiles(directory="static"), name="static")

# Serve HTML frontend
@app.get("/", response_class=HTMLResponse)
async def get_index():
    with open("index.html") as f:
        return f.read()

# Ensure data directory exists
os.makedirs(os.path.dirname(DB_PATH), exist_ok=True)

# Initialize DB
def init_db():
    conn = sqlite3.connect(DB_PATH)
    with open("schema.sql", "r") as f:
        conn.executescript(f.read())
    conn.close()

init_db()

class User(BaseModel):
    name: str

@app.post("/users/")
def create_user(user: User):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("INSERT INTO users (name) VALUES (?)", (user.name,))
    conn.commit()
    conn.close()
    return {"message": "User created"}

@app.get("/users/")
def read_users():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("SELECT id, name FROM users")
    users = cursor.fetchall()
    conn.close()
    return {"users": users}
