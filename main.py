from fastapi import FastAPI
from routes import classify
from fastapi.middleware.cors import CORSMiddleware
app= FastAPI(title="Genderize API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],     
    allow_credentials=True,
    allow_methods=["*"],           
    allow_headers=["*"],     
)

app.include_router(classify.router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)