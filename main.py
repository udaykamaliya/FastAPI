from fastapi import FastAPI , Path, HTTPException
import json

app = FastAPI()

def load_data():
    with open("patients.json",'r') as f :
          data = json.load(f)
          
    return data      
    

@app.get("/")
def hello() :
    return {"message": "Hello, World!"}


@app.get("/view")
def pateints_data() :
    data = load_data()
    return data

@app.get("/patients/{patient_id}")
def view_patient(patient_id: str = Path(... , description ='ID of the patient in DB', example='P001') ):
    data = load_data()
    
    if patient_id in data:
        return data[patient_id]
    raise HTTPException(status_code=404, detail="Patient not found")