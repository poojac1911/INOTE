from typing import Union
from fastapi import APIRouter
from models.note import Note
from config.db import conn
from schemas.schemas import noteEntity, notesEntity
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

note = APIRouter()
templates = Jinja2Templates(directory="templates")


@note.get("/", response_class=HTMLResponse)
async def read_item(request: Request):
    docs = conn.notes.note.find()
    newDocs = []
    for doc in docs:
        newDocs.append({
            "id": doc["_id"],
            "title": doc["title"],
            "desc": doc["desc"],
            "important": doc["important"]
        })
    return templates.TemplateResponse("index.html", {"request": request, "newDocs": newDocs})


@note.post("/")
async def create_item(request: Request):
    form = await request.form()
    formDict = dict(form)
    formDict["important"] = True if formDict.get("important") == "on" else False
    note = conn.notes.note.insert_one(dict(formDict))
    return {"Success" : True}

# @note.post("/")
# def add_note(note: Note):
#     print(note)
#     inserted_note = conn.notes.note.insert_one(dict(note))
#     return noteEntity(inserted_note)
