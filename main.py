

from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse

from pymongo import MongoClient

app = FastAPI()


conn = MongoClient("mongodb+srv://Puri:TODOAPP@todo.l3uoyra.mongodb.net")


