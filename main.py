# -*- coding: utf-8 -*-

from fastapi import FastAPI
from datetime import datetime, date, time
from fastapi.middleware.cors import CORSMiddleware
from models import models

app = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:3000"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

@app.get("/")
async def home():
   return {"data": "Hello World"}

@app.get("/articles")
async def getArticles():
   return {
       "posts": [{
            "id": 1,
            "title": "Test post",
            "body": "Some text",
            "createdAt": datetime.now(),
            "updatedAt": datetime.now(),
            "comments": [],
       }]
   }

@app.get("/article/{num}")
async def getArticle(num):
   return {
       "post": {
            "id": num,
            "title": "Test post",
            "body": "Some text",
            "createdAt": datetime.now(),
            "updatedAt": datetime.now(),
            "comments": []
       }
   }

@app.post("/article/")
async def getArticle():
   return {
       "post": {
            "id": 555,
            "title": "Test post",
            "body": "Some text",
            "createdAt": datetime.now(),
            "updatedAt": datetime.now(),
            "comments": []
       }
   }

# @app.get("/article")

#
# Команда запустить:
# uvicorn main:app --reload
#
#Модели в БД:
#
#Статьи:
# - ID
# - Название
# - Текст статьи
# - Дата создания
# - Дата модификации
#
#Комментарии:
# - ID
# - Текст комментария
# - ID Статьи
# - Дата создания
# - Дата модификации
#
#Реализовать CRUD для статьи (для body формата json)
# - C - POST /article/
# - R - GET /article/#ID#/, GET /articles/
# - U - PATCH /article/#ID#/
# - D - DELETE /article/#ID#/
#
#Реализовать CRUD для комментария
# - C - POST /article/#ID#/comment/
# - R - GET /article/#ID#/comment/#COMMENT_ID#/, GET /article/#ID#/comments/
# - U - PATCH /article/#ID#/comment/#COMMENT_ID#/
# - D - DELETE /article/#ID#/comment/#COMMENT_ID#/
#
#Реализовать метод получения комментариев за период с группировкой по статьям в которых они были оставлены
# - GET /analytic/comments/?dateFrom=#timestamp#&dateTo=#timestamp#
