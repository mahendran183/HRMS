from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel
from typing import List, Annotated

import models
from database import engine, SessionLocal
from sqlalchemy.orm import Session

app = FastAPI()
models.Base.metadata.create_all(bind=engine)

class Employeebase(BaseModel):
    EmpId: int
    EmpName: str
    EmpDes: str
    EmpDob: str
    EmpDoj: str

# class QuestionBase(BaseModel):
#     question_text: str
#     choices: List[ChoiceBase]
    
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
    
db_dependency = Annotated[Session, Depends(get_db)]

# 1.Get method
# 2.URL=http://localhost:8000/questions/id1
# 3.this api will get the question by question id
@app.get("/questions/{question_id}")
async def read_question(question_id: int, db:db_dependency):
    result = "success"
    return result

# 1.Post method
# 2.URL=http://localhost:8000/questions/
# 3.this api will get the question by question id
@app.post("/getall-employees/")
async def create_employees(input: Employeebase, db: db_dependency):
    db_create_employees = models.Employees(EmpId=input.EmpId, EmpName=input.EmpName, EmpDes=input.EmpDes, EmpDob=input.EmpDob, EmpDoj=input.EmpDoj)
    db.add(db_create_employees)
    db.commit()
    db.refresh(db_create_employees)