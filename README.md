# AI Chat Demo

一个基于 DeepSeek API 的 AI 聊天应用，包含 Web 前端和 Python 后端。

## 功能

- 多轮对话（AI 能记住上下文）
- Web 聊天界面
- API Key 通过环境变量管理

## 技术栈

- 前端：HTML / CSS / JavaScript
- 后端：Python + FastAPI
- AI：DeepSeek API（OpenAI 兼容接口）

## 本地运行

1. 安装依赖
   pip install fastapi uvicorn openai python-dotenv

2. 创建 `.env` 文件，内容：
   DEEPSEEK_API_KEY=你的key

3. 启动后端
   uvicorn server:app --reload

4. 浏览器打开 index.html

## 项目结构

- `server.py`：FastAPI 后端，转发请求给 DeepSeek
- `index.html`：聊天界面
- `.env`：存放 API Key（已 gitignore）
