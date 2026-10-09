from openai import OpenAI

# 创建客户端
client = OpenAI(
    api_key="sk-b4ba22c7568f4c96ba3bb06424842d2d",              # ← 换成你自己的
    base_url="https://api.deepseek.com"  # ← DeepSeek 的地址
)

# 发一条消息给 AI
response = client.chat.completions.create(
    model="deepseek-chat",              # ← 模型名
    messages=[
        {"role": "user", "content": "你好，请用一句话介绍你自己"}
    ]
)

# 打印 AI 的回复
print(response.choices[0].message.content)