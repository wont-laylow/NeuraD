from pydantic import BaseModel

class Features(BaseModel):
    Glucose: float
    BMI: float        
    DiabetesPedigreeFunction: float
    Age: int 