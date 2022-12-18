import uvicorn
from fastapi import FastAPI
from datetime import datetime
from routers import eitaa, bale


app = FastAPI()
app.include_router(eitaa.router, tags=["eitaa"], prefix="/eitaa")
app.include_router(bale.router, tags=["bale"], prefix="/bale")

if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=8000,
        reload=True,
    )
