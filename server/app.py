import os

from starlette.applications import Starlette
from starlette.requests import Request
from starlette.responses import Response
from starlette.templating import Jinja2Templates
from starlette.staticfiles import StaticFiles

from .utils import bytecode

app = Starlette(debug=True)
app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")


@app.route("/")
async def homepage(request: Request) -> Response:
    context = {"request": request, "code": bytecode(os.path.join("frontend", "app.py"))}
    return templates.TemplateResponse("index.html", context)
