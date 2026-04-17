import ollama

client = ollama.Client(host="127.0.0.1:11434")


# 封装api
def get_ollama_response(prompt):
    response = client.chat(
        model='qwen2:0.5b',
        messages=[{'role': 'user',
                   'content': prompt}
                  ],
        stream=False)
    return response.message.content


if __name__ == '__main__':
    messages = [{'role': 'user', 'content': '你是谁'}]
    res = get_ollama_response(messages)
    messages.append({'role': 'assistant', 'content': res})
    print(messages)

# # 导包
# import ollama
#
# # 连接本地的ollama软件
# client = ollama.Client(host='http://127.0.0.1:11434')
#
#
# # 封装api函数
# def get_ollama_response(messages):
#     # 选择模型以及角色,然后开始聊天
#     result = client.chat(
#         model='qwen2.5:7b',
#         # 此处建议给模型最近n条历史消息,比如下面的代表最近10条
#         messages=messages[-10:],
#         stream=False
#     )
#     return result.message.content
#
#
# if __name__ == '__main__':
#     messages = [{'role': 'user', 'content': '你是谁'}]
#     res = get_ollama_response(messages)
#     messages.append({'role': 'assistant', 'content': res})
#     print(messages)