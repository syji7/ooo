# 1.导包
import streamlit as st
from chat_utils.ollama_tiaoyon_yunxing import get_ollama_response

# 2.构建页面
# 标题
st.title('黑马智聊机器人')
# 分割线
st.divider()
# 构建聊天窗口
# ①ai开场白
st.chat_message('assistant').write('你好,我是黑马智聊机器人,有什么可以帮您的?')
# ②用户输入问题
prompt = st.chat_input('请您输入问题:')
if prompt:
    st.chat_message('user').write(prompt)
    # ③ TODO AI根据用户的问题,调用大模型获取答案
    # 封装消息列表
    messages = [{'role': 'user', 'content': prompt}]
    # 调用大模型获取答案
    response = get_ollama_response(messages)
    # 把答案显示到页面中
    st.chat_message('assistant').write(response)
