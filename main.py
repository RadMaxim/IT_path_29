import fastapi, uvicorn
from router.router import router
app = fastapi.FastAPI()
app.include_router(router)

if __name__ == "__main__":
    uvicorn.run(app, port=8000)

