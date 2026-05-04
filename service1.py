from fastapi import FastAPI
import requests
app = FastAPI()

@app.get("/service1")
def service1():
 try:  
     response = requests.get("http://localhost:8001/service2")
     data = response.json()

     return {"Service 1": "Service 1 is running",
             "Service 2": data }
 except:
        return {"Service 1": "Service 1 is running",
                   "Service 2": "Service 2 is not available" }
