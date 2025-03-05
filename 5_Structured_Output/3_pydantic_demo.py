from pydantic import BaseModel, EmailStr, Field
from typing import Optional

class Student(BaseModel):
    name: str = 'rakshitha'
    age: Optional[int] = None
    email: EmailStr
    cgpa: float = Field(gt=0, lt=10, default=5, description='Cumulative Grade Point Average')

new_student = { 'age': '20', 'email': 'rakshitha@example.com','cgpa': 9 } 

student = Student(**new_student)

student_dict = dict(student)

print(student_dict)
print(student_dict['age'])

student_json = student.model_dump_json()
print(student_json)