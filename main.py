from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

app = FastAPI()
app.mount("/", StaticFiles(directory="public", html = True), name="static")

@app.get("/hello")
def read_root():
    return{"Hello":"고운님 어서오세요!"}

app.mount("/", StaticFiles(directory="Public",html =True),name="static")
