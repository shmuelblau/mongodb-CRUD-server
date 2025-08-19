





from fastapi import FastAPI, Form, HTTPException ,Request
from fastapi.responses import JSONResponse , HTMLResponse , RedirectResponse
from fastapi.templating import Jinja2Templates
from starlette import status
import uvicorn

from DAL.Eagle_DAL import Eagle_DAL
from Models.Person import Person
from Models.PersonType import PersonType
import jinja2

import os
from dotenv import load_dotenv

load_dotenv(dotenv_path=".env")
host = os.getenv("HOST")
user = os.getenv("USER")
password = os.getenv("PASSWORD")
dbname = os.getenv("DATABASE")
collecsion_name = os.getenv("COLLECSION_NAME")




app = FastAPI()

dal = Eagle_DAL(host,user,password, dbname ,collecsion_name)

templates = Jinja2Templates(directory="templates")


@app.get('/get') 
def get():
    
    data = dal.Select()
    print(data)
    return data

@app.get("/", response_class=HTMLResponse)
def home(request: Request):

    data = dal.Select()
    
    return templates.TemplateResponse(
        "index.html",
        {"request": request, "data": data}
    )





@app.post("/add")
def add_form(id: int = Form(...), first_name: str = Form(...), last_name: str = Form(...),):
   
    person = PersonType(id=id, first_name=first_name, last_name=last_name)
    dal.add(person)
    return RedirectResponse(url="/", status_code=status.HTTP_303_SEE_OTHER)
    

@app.post('/edit' ) 
def edit(id: int = Form(...), first_name: str = Form(...), last_name: str = Form(...),):

    person = PersonType(id=id, first_name=first_name, last_name=last_name)
    
    dal.edit(person)
    
    return RedirectResponse(url="/", status_code=status.HTTP_303_SEE_OTHER)



@app.post("/delete")
def delete_form(id: int = Form(...)):
    try:
        person = Person(id=id)
        dal.delete(person)
        return RedirectResponse(url="/", status_code=status.HTTP_303_SEE_OTHER)
    except Exception:
        raise HTTPException(status_code=500, detail="Failed to delete record")



if __name__ == "__main__":
    
    uvicorn.run("main:app", host="0.0.0.0", port=5000, reload=True)