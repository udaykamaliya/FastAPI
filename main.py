from fastapi import FastAPI , Path, HTTPException , Query
import json

app = FastAPI()

def load_data():
    with open("patients.json",'r') as f :
          data = json.load(f)
          
    return data      
    

@app.get("/")
def hello() :
    return {"message": "Hello, World!"}

@app.get("/about")
def about():
    return {"app": "Patient Data API", "version": "1.0.0"}


@app.get("/view")
def pateints_data() :
    data = load_data()
    return data

# Path Parameter
@app.get("/patients/{patient_id}") 
def view_patient(patient_id: str = Path(... , description ='ID of the patient in DB', example='P001') ):
    data = load_data()
    
    if patient_id in data:
        return data[patient_id]
    raise HTTPException(status_code=404, detail="Patient not found")

# QUERY PARAMETER

@app.get("/sort")
def sort_patients(sort_by: str = Query(..., description='sort on the basis of Height , Weight Or bmi'),
                  order : str = Query('asc', description = "sort in asc or desc order")):
    valid_fields = ['height', 'weight', 'bmi']
    if sort_by not in valid_fields:
        raise HTTPException(status_code = 400 , detail=f'invalid field select from {valid_fields}')
    if order not in ['asc','desc']:
        raise HTTPException(status_code = 400, detail = 'Order must be asc or desc')
    data = load_data()
    sort_order = True if order =='desc' else False
    sorted_data = sorted(data.values(), key = lambda x : x.get(sort_by,0), reverse= sort_order)
    return sorted_data