from fastapi import APIRouter

router = APIRouter(tags=["Persons"])

from shemas.shemas import Data, Android
persons = []
androids = []

@router.post("/person_add")
def addPerson(person:Data):
    print(person)
    persons.append(person)
    return persons
@router.get("/")
def main():
    return {"success":"true"}

@router.get("/info")
def info():
    return {"name":"Maxim"}

@router.get("/persons")
def persons():
    return {"name":"Maxim"}
@router.get("/lessons")
def lessons():
    return {"name":"Maxim"}
@router.get("/getAllPersons")
def getPersons():
    return persons
@router.post("/add_android")
def addAndroid(android:Android):
    androids.append(android)
    return androids
