import os
from dotenv import load_dotenv
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from openai import OpenAI

load_dotenv()   # 读取 .env 文件

# 创建 FastAPI 应用
app = FastAPI()

# 允许前端跨域访问（不然后面浏览器会拦截）
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# 创建 AI 客户端
client = OpenAI(
    api_key=os.getenv("DEEPSEEK_API_KEY"),
    base_url="https://api.deepseek.com"
)

# 定义接收的数据格式
class ChatRequest(BaseModel):
    message: str

# 全局保存对话历史（简单版，多个用户会串，后面再优化）
messages = [
    {"role": "system", "content": "你是一个乐于助人的助手，回答简洁。"}
]

# 定义接口
@app.post("/chat")
def chat(req: ChatRequest):
    messages.append({"role": "user", "content": req.message})

    response = client.chat.completions.create(
        model="deepseek-chat",
        messages=messages
    )

    ai_reply = response.choices[0].message.content
    messages.append({"role": "assistant", "content": ai_reply})

    return {"reply": ai_reply}