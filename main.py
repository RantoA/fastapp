from typing import List
from fastapi import FastAPI,  HTTPException
from pydantic import BaseModel


app = FastAPI()

#BASEMODEL/ DEFAULT MODEL
class base(BaseModel):
    nom : str
    age : int
    pays : str
    mail : str

#FAKE DATABSE, ONLY USE FOR THE EXAMPLE
bd_test = []

#HOME PAGE ON THE API
@app.get("/home/")
async def home_page():
    return {"welcom" : "welcome to the home page"}

#SCRIPT USE TO UPTADE A NEW DATABSE LIST 
@app.post("/ajooutDB/")
async def ajour_db(base:base):
    bd_test.append(base)
    return bd_test

# SCRIPT BUT WE USE TO DISLAY THE ELEMENT ONE THE DATABASE
@app.get("/fetch-all/")
async def db_fetch_all():
    return bd_test

#DISPLAY ONE ELEMENT ON THE DATABASE, ONLY USE THE ID OF THE ELEMENT ON THE LIST
@app.get("/fetch-one/{id}", response_model=base)
async def db_fetch(id:int):
    try :
        dbonce = bd_test[id]
        return dbonce
    except:
        raise HTTPException(status_code=401, detail="Id not found")
    
#USED TO MODIFY ONE ELEMENT ON THE LIST 
@app.put("/update_data/{id}")
async def update(id:int, update_db:base):
    try :
        bd_test[id]=update_db
        return update_db
    except:
        raise HTTPException(status_code=401, detail="Id not found")

#THIS SCRIT DELETE ONE ELEMENT OF THE LIST
@app.delete("/delete/{id}")
async def delet_list(id:int):
    try :
        delet_id= bd_test[id]
        bd_test.pop(id)
        return delet_id
    except:
        raise HTTPException(status_code=401, detail="Id not found")
