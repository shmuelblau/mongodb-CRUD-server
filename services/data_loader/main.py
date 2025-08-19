from fastapi import FastAPI, Form, HTTPException ,Request
from fastapi.responses import JSONResponse , HTMLResponse , RedirectResponse
from fastapi.templating import Jinja2Templates
from starlette import status
import uvicorn

from config import *
from DAL.Eagle_DAL import Eagle_DAL

from services.data_loader.Models.Soldier import Soldier
import jinja2

import os
from dotenv import load_dotenv





app = FastAPI()

dal = Eagle_DAL(host,user,password, dbname ,collecsion_name)

templates = Jinja2Templates(directory="templates")




@app.get("/", response_class=HTMLResponse)
def home(request: Request):

    data = dal.Select()
    
    return templates.TemplateResponse(
        "index.html",
        {"request": request, "data": data}
    )



@app.post("/add")
def add(id: int = Form(...), first_name: str = Form(...), last_name: str = Form(...),rank: str = Form(...),phone_number: int = Form(...),):
   
    person = Soldier(id=id, first_name=first_name, last_name=last_name , rank=rank , phone_number=phone_number)
    dal.add(person)
    return RedirectResponse(url="/", status_code=status.HTTP_303_SEE_OTHER)
    

@app.put('/edit' ) 
def edit(id: int = Form(...), first_name: str = Form(...), last_name: str = Form(...),rank: str = Form(...),phone_number: int = Form(...),):

    person = Soldier(id=id, first_name=first_name, last_name=last_name , rank=rank , phone_number=phone_number)
    
    dal.edit(person)
    
    return RedirectResponse(url="/", status_code=status.HTTP_303_SEE_OTHER)



@app.delete("/delete")
def delete_form(id: int = Form(...)):
    try:
        person = Soldier(id=id , first_name="" ,last_name="" , rank="" , phone_number=1)
        dal.delete(person)
        return RedirectResponse(url="/", status_code=status.HTTP_303_SEE_OTHER)
    except Exception:
        raise HTTPException(status_code=500, detail="Failed to delete record")



if __name__ == "__main__":
    
    uvicorn.run("main:app", host="0.0.0.0", port=5000, reload=True)