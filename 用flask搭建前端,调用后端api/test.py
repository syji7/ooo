from openai import OpenAI


# 初始化提示词
def init_prompt():
    examples = {
        '相似': [
            ('公司ABC发布了季度财报，显示盈利增长。', '财报披露，公司ABC利润上升。'),
        ],
        '不相似': [
            ('黄金价格下跌，投资者抛售。', '外汇市场交易额创下新高。'),
            ('央行降息，刺激经济增长。', '新能源技术的创新。')
        ]
    }
    # 准备提示词:
    prompt = f"""你是一名专业的信息匹配系统，你需要判断提供的句子1和句子2是否相似。句子1和句子2的相似度越相似，则返回相似，否则返回不相似!不要胡编乱造!"""
    history_messages = [
        {"role": "system", "content": prompt}
    ]
    # 系统提示词拼接小样本提示词
    for ks, vs in examples.items():
        for v in vs:
            history_messages.append({"role": "user", "content": f'判断句子1:{v[0]}和句子2:{v[1]}是否相似?'})
            history_messages.append({"role": "assistant", "content": ks})
    return history_messages


# 2.调用大模型
llm = OpenAI(api_key="sk-f5d3982f6b0346a09641f6f2dd8768fa",
             base_url="https://dashscope.aliyuncs.com/compatible-mode/v1"
             )


# 定义api接口
def call_llm(texts):
    for text in texts:
        res = llm.chat.completions.create(
            model="qwen-plus",
            messages=init_prompt() + [
                {'role': 'user', 'content': f"句子1->{text[0]}和句子2->{text[1]}.它们是否相似?"}
            ]
        )
        result = res.choices[0].message.content
        # print(f'{text}的匹配结果是:{result}')
        return  result


if __name__ == '__main__':
    texts = [
           ('股票市场今日大涨，投资者乐观。', '持续上涨的市场让投资者感到满意。'),
        ('油价大幅下跌，能源公司面临挑战。', '未来智能城市的建设趋势愈发明显。'),
        ('利率上升，影响房地产市场。', '高利率对房地产有一定冲击。'),
        ('我爱你', '我恨你'),
        ('我爱你', '我喜欢你')
    ]
    print(call_llm(texts))
