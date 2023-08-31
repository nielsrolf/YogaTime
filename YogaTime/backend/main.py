from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def read_root():
    return {'Hello': 'World'}
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import sqlite3

app = FastAPI()

# User model
class User(BaseModel):
    username: str
    password: str

# In-memory storage for users
users = {}

@app.post('/register')
def register(user: User):
    if user.username in users:
        raise HTTPException(status_code=400, detail='Username already exists')
    users[user.username] = user.password
    return {'success': True}

@app.post('/login')
def login(user: User):
    if user.username not in users or users[user.username] != user.password:
        raise HTTPException(status_code=400, detail='Invalid username or password')
    return {'success': True}
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import sqlite3

app = FastAPI()

# User model
class User(BaseModel):
    username: str
    password: str

# Session model
class Session(BaseModel):
    date: str
    time: str
    place: str
    max_participants: int

# In-memory storage for users and sessions
users = {}
sessions = []

@app.post('/register')
def register(user: User):
    if user.username in users:
        raise HTTPException(status_code=400, detail='Username already exists')
    users[user.username] = user.password
    return {'success': True}

@app.post('/login')
def login(user: User):
    if user.username not in users or users[user.username] != user.password:
        raise HTTPException(status_code=400, detail='Invalid username or password')
    return {'success': True}

@app.post('/session')
def create_session(session: Session):
    sessions.append(session)
    return {'success': True}
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import sqlite3

app = FastAPI()

# User model
class User(BaseModel):
    username: str
    password: str

# Session model
class Session(BaseModel):
    date: str
    time: str
    place: str
    max_participants: int
    booked_participants: int = 0

# In-memory storage for users and sessions
users = {}
sessions = []

@app.post('/register')
def register(user: User):
    if user.username in users:
        raise HTTPException(status_code=400, detail='Username already exists')
    users[user.username] = user.password
    return {'success': True}

@app.post('/login')
def login(user: User):
    if user.username not in users or users[user.username] != user.password:
        raise HTTPException(status_code=400, detail='Invalid username or password')
    return {'success': True}

@app.post('/session')
def create_session(session: Session):
    sessions.append(session)
    return {'success': True}

@app.get('/sessions')
def list_sessions():
    return sessions

@app.post('/book/{session_id}')
def book_session(session_id: int):
    if session_id < 0 or session_id >= len(sessions):
        raise HTTPException(status_code=400, detail='Invalid session ID')
    session = sessions[session_id]
    if session.booked_participants >= session.max_participants:
        raise HTTPException(status_code=400, detail='Session is full')
    session.booked_participants += 1
    return {'success': True}
