from fastapi import FastAPI
from server.app import database
from server.app.routes import student

app = FastAPI()



database.init_db()
app.include_router(student.router)
