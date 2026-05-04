from fastapi import FastAPI
app =FastAPI()

@app.get("/service2")

def read_service2():
     return {"service2": "THIS RESPONSE COMES FROM SERVICE 2"}        