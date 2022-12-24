from fastapi import FastAPI
from routers import eitaa, bale


app = FastAPI()
app.include_router(eitaa.router, tags=["eitaa"], prefix="/eitaa")
app.include_router(bale.router, tags=["bale"], prefix="/bale")
