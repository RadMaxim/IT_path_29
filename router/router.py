from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates


from shemas.shemas import Data, Android

persons = []
androids = []
router = APIRouter(tags=["Persons"])

templates = Jinja2Templates(directory="D:/pythonProject1/templates")

@router.get("/", response_class=HTMLResponse)
async def root(request: Request):
    return templates.TemplateResponse(name='index.html',request=request)


@router.post("/person_add")
def addPerson(person: Data):
    print(person)
    persons.append(person)
    return persons

@router.get("/info")
def info():
    return {"name": "Maxim"}

@router.get("/persons")
def persons_page():
    return {"name": "Maxim"}

@router.get("/lessons")
def lessons():
    return {"name": "Maxim"}

@router.get("/getAllPersons")
def getPersons():
    return persons

@router.post("/add_android")
def addAndroid(android: Android):
    androids.append(android)
    return androids