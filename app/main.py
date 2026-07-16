from fastapi import FastAPI
app=FastAPI(title="My API")

@app.get("/")
async def root():
    return {"message": "Hello World"}
@app.get("/hello")
async def hello():
    return {"message": "Hello"}