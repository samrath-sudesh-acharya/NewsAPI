from fastapi import FastAPI 
import requests
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

@app.get('/news')
def html():
    response = requests.request('GET','https://newsapi.org/v2/everything?q=education&from=2022-11-06&sortBy=publishedAt&apiKey=da9d1c5a4e954cdfbb770d05c4a571fc')
    return response.json()

origins = ["*"]

app = CORSMiddleware(
    app=app,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)