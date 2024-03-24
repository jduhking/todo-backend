from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
import json
from uuid import uuid4

origins = [
    "http://localhost:5173"
]

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

"""
Todos will have the shape of 
{
    id: a unique id, use the uuid4 package
    message: what to do
    complete: whether the task has been completed or not
}
"""
todos = []

@app.get("/")
def read_root():
    return "Hello World"

@app.get("/todos")
def get_todos(): 
    """ return all the todos """

@app.get("/todos/{id}")
def get_todo(id: str):
    """ loop through all the todos and return the one which matches the id """

@app.post("/todo")
async def create_todo(request: Request):
    """ create a todo and append it to the end of the todos list """
    # make sure to convert the data to json

@app.post("/todo/toggle/{id}")
async def toggle_todo_completion(id: str):
    """ if the todo hasnt been marked as complete then check it else uncheck it """
    # search for the todo in the list with the matching id

    # toggle its complete status
        
    # could not find the task with the given id
