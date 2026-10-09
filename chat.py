from openai import OpenAI

client = OpenAI(
    api_key="sk-b4ba22c7568f4c96ba3bb06424842d2d",
    base_url="https://api.deepseek.com"
)

# 历史消息列表：保存整段对话
messages = [
    {"role": "system", "content": "你是一个乐于助人的助手，回答简洁。"}
]

print("开始聊天（输入 exit 退出）：")

while True:
    # 1. 读用户输入
    user_input = input("\n你: ")

    if user_input == "exit":
        print("再见！")
        break

    # 2. 把用户消息加入历史
    messages.append({"role": "user", "content": user_input})

    # 3. 发给 AI
    response = client.chat.completions.create(
        model="deepseek-chat",
        messages=messages
    )

    # 4. 取出 AI 回复
    ai_reply = response.choices[0].message.content
    print(f"\nAI: {ai_reply}")

    # 5. 把 AI 回复也加入历史
    messages.append({"role": "assistant", "content": ai_reply})