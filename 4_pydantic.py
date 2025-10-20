from pydantic import BaseModel, EmailStr
from typing import Optional

class Student(BaseModel):
    # defining schema setup for name
    name: str = 'Raju'
    age: int

new_student = {'name': 'Mary', 'age': 21}
student = Student(**new_student)
print(student, type(student))

# new_student = {'name': 55, 'age': '44'} - this will raise error as name should be string
# pydantic will validate the data

''' Pydantic performs type coercion - it automatically converts compatible types. 
So when you pass '44' (string) for an int field, Pydantic converts it to 44 (integer).
'''
new_student = {'name': 'John', 'age': '44'}

student = Student(**new_student)
print(student, type(student))

# setting optional value - have to use None
class Person(BaseModel):
    name: str
    age: Optional[int] = None

new_person = {'name': 'Mike'}
person = Person(**new_person)
print(person, type(person))

# email validation

class Person(BaseModel):
    name: str
    email: Optional[EmailStr] = None

# validates email - if email is not valid, it will raise error
new_person = {'name': 'Jake', 'email': 'j9YHsex@amplec.om'}
person = Person(**new_person)
print(person, type(person))