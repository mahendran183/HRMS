from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from database import Base

class Employees(Base):
    __tablename__ = 'employees'
 
    EmpId = Column(Integer, primary_key=True, index=True)
    EmpName = Column(String, index=True)
    EmpDes = Column(String, index=True)
    EmpDob = Column(String, index=True)
    EmpDoj = Column(String, index=True)
 
# class Choices(Base):
#     __tablename__ = 'choices'
   
#     id = Column(Integer, primary_key=True, index=True)
#     choice_text = Column(String, index=True)
#     is_correct = Column(Boolean, default=False)
#     question_id = Column(Integer, ForeignKey('questions.id'))
