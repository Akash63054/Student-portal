
import os

from dotenv import load_dotenv
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from starlette.middleware.sessions import SessionMiddleware
from fastapi.templating import Jinja2Templates

from database import engine, Base
import models


load_dotenv()

app = FastAPI()
@app.get("/")
def home(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="home.html",
        context={}
    )

app.add_middleware(
    SessionMiddleware,
    secret_key=os.getenv("SESSION_SECRET"),
    https_only=False
)

Base.metadata.create_all(bind=engine)

templates = Jinja2Templates(directory="templates")


@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="home.html",
        context={}
    )


