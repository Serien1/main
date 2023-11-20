import uvicorn
from typing import Union
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
app = FastAPI()
# 跨域资源共享
app.add_middleware(
 CORSMiddleware,
 allow_origins=['*'],
 allow_credentials=True,
 allow_methods=["*"],
 allow_headers=["*"],
)
class User(BaseModel):
 username: str
 password: str
# 创建账号密码的字典
user_password = {}
# 创建路由
@app.post("/login")
def login(data:User):
 # 获取数据
 username = data.username
 password = data.password

 if username not in user_password:
     return "用户名不存在"
 elif password == user_password[username]:
    return '登录成功'
 else:
    return '密码错误'



@app.post("/register")
def enroll(data:User):
 # 获取数据
 username = data.username
 password = data.password
 user_password[username] = password
 if password == user_password[username]:
       return '注册成功'

 else:
       return '注册错误'
