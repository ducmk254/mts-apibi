from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.config import settings
from app.routers import auth, user, bigquery,sap,transport,index

app = FastAPI()

origins = [
    settings.CLIENT_ORIGIN,
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(index.router)
app.include_router(auth.router, tags=['Auth'], prefix='/api/auth')
app.include_router(user.router, tags=['Users'], prefix='/api/users')
app.include_router(bigquery.router, tags=['Bigquery'], prefix='/api/bigquery')
app.include_router(sap.router, tags=['SAP'], prefix='/api/sap')
app.include_router(transport.router, tags=['transport'], prefix='/api/transport')


@app.get("/api/healthchecker")
def root():
    return {"message": "Welcome to API Mutosi"}
