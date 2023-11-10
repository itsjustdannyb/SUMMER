
# imports
from fastapi import FastAPI, Request, Form
import uvicorn

# HTML
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

#CSS
from fastapi.staticfiles import StaticFiles

# the app
app = FastAPI()

# templates
templates = Jinja2Templates(directory="templates")

# mount the static files to the app
app.mount("/static", StaticFiles(directory="static"), name="static")


# test endpoint
@app.get('/')
async def test():
    return {'welcome':'user'}

# adder endpoint
@app.get('/summer', response_class=HTMLResponse)
async def summer(request:Request):
    return templates.TemplateResponse("index.html", {'request':request})

@app.post('/summer', response_class=HTMLResponse)
async def summer(request:Request, num1:int = Form(...), num2:int = Form(...)):
    summation = num1 + num2
    return templates.TemplateResponse("index.html", {'request':request, 'sum':summation})

if __name__ == "__main__":
    uvicorn.run(app)

# http://localhost:8000
