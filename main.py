import fastapi, uvicorn
from router.router import router
from fastapi.staticfiles import StaticFiles
app = fastapi.FastAPI(title="kkk")

app.mount("/templates", StaticFiles(directory="templates"), name="templates")


app.include_router(router)
if __name__ == "__main__":
    uvicorn.run(app, port=8000)

