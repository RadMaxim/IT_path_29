import fastapi, uvicorn
import pydentic
from shemas.shemas import Data, Android
persons = []
androids = []

app = fastapi.FastAPI()
@app.post("/person_add")
def addPerson(person:Data):
    print(person)
    persons.append(person)
    return persons
@app.get("/")
def main():
    return {"success":"true"}

@app.get("/info")
def info():
    return {"name":"Maxim"}

@app.get("/persons")
def persons():
    return {"name":"Maxim"}
@app.get("/lessons")
def lessons():
    return {"name":"Maxim"}
@app.get("/getAllPersons")
def getPersons():
    return persons
@app.post("/add_android")
def addAndroid(android:Android):
    androids.append(android)
    return androids

if __name__ == "__main__":
    uvicorn.run(app, port=8000)

