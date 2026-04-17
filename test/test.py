# # from datetime import datetime
# # import time
# # import dashscope
# # import os
# #
# #
# # # - 获取当前日期
# # def get_current_date():
# #     return datetime.now().month
# #
# #
# # # - 查询节假日
# # def search_holidays(month):
# #     holidays = {
# #         "1月": ["元旦: 1月1日-3日"],
# #         "2月": ["春节: 2月15日-23日"],
# #         "3月": [],
# #         "4月": ["清明节: 4月4日-6日"],
# #         "5月": ["劳动节: 5月1日-5日"],
# #         "6月": ["端午节: 6月19日-21日"],
# #         "7月": [],
# #         "8月": [],
# #         "9月": ["中秋节: 9月25日-27日"],
# #         "10月": ["国庆节: 10月1日-7日"],
# #         "11月": [],
# #         "12月": []
# #     }
# #     # 根据传入的月份获取对应节假日列表
# #     month_holidays = holidays.get(str(month) + "月")
# #     print(month_holidays)
# #
# #     if month_holidays:
# #         return f"2025年{month}有以下法定节假日：\n" + "".join(month_holidays)
# #     else:
# #         return f"2025年{month}没有法定节假日。"
# #
# #
# # print(search_holidays(5))
# #
# # # 注册工具(调用工具有什么用)
# # TOOlS={'get_current_date()': get_current_date,
# #        'search_holidays': search_holidays
# #        }
# # # 调用模型
# #
# # # 解析模型输出
# #
# # # 从文本中提取月份信息
# #
# # # ReAct主循环
# #
# # if __name__ == '__main__':
# #     # 运行
#
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from webdriver_manager.chrome import ChromeDriverManager
# import time
# import json
#
# # 目标URL
# TARGET_URL = "https://www.datatft.com/explorer?share=ABFAAAAA0FBLL2%7CF00"
#
#
# def init_driver():
#     options = webdriver.ChromeOptions()
#     # options.add_argument("--headless=new")  # 无头模式，需要可视化就注释掉
#     driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
#     driver.maximize_window()
#     return driver
#
#
# def crawl_tft_by_browser(driver):
#     driver.get(TARGET_URL)
#     # 等待页面加载
#     WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "comp-item")))
#
#     all_data = []
#     # 模拟筛选：比如选14.9版本
#     version_select = driver.find_element(By.XPATH, "//*[contains(text(), '14.9')]")
#     version_select.click()
#     time.sleep(3)  # 等待数据加载
#
#     # 爬取页面上的阵容数据
#     comp_items = driver.find_elements(By.CLASS_NAME, "comp-item")
#     for item in comp_items:
#         name = item.find_element(By.CLASS_NAME, "comp-name").text
#         win_rate = item.find_element(By.CLASS_NAME, "win-rate").text
#         play_rate = item.find_element(By.CLASS_NAME, "play-rate").text
#         all_data.append({
#             "name": name,
#             "win_rate": win_rate,
#             "play_rate": play_rate
#         })
#         print(f"爬取到: {name} | {win_rate} | {play_rate}")
#
#     return all_data
#
#
# if __name__ == "__main__":
#     driver = init_driver()
#     data = crawl_tft_by_browser(driver)
#     with open("tft_browser_data.json", "w", encoding="utf-8") as f:
#         json.dump(data, f, ensure_ascii=False, indent=2)
#     driver.quit()
#     print(f"\n爬取完成，共 {len(data)} 条数据")


# 练习
"""
核心思想
1.先调用模型的api
2.准备模型需要用到的工具(get_current_month,get_holiday)
3.开始准备ReAct的功能(思考->行动->观察)
"""
import json

# 0.导包
# import os
# from openai import OpenAI
# from datetime import datetime
#
# client = OpenAI(
#     api_key="sk-f5d3982f6b0346a09641f6f2dd8768fa",
#     base_url="https://dashscope.aliyuncs.com/compatible-mode/v1",
# )
#
#
# def get_current_month():
#     year = datetime.now().year
#     month = datetime.now().month
#     return f'{year}年{month}月'
#
#
# def get_holiday(month):
#     holidays = {
#         "2026年1月": ["元旦: 1月1日-3日"],
#         "2026年2月": ["春节: 2月15日-23日"],
#         "2026年3月": [],
#         "2026年4月": ["清明节: 4月4日-6日"],
#         "2026年5月": ["劳动节: 5月1日-5日"],
#         "2026年6月": ["端午节: 6月19日-21日"],
#         "2026年7月": [],
#         "2026年8月": [],
#         "2026年9月": ["中秋节: 9月25日-27日"],
#         "2026年10月": ["国庆节: 10月1日-7日"],
#         "2026年11月": [],
#         "2026年12月": []
#     }
#     # 根据年月获取对应节假日列表
#     month_holidays = holidays.get(month, [])
#     return month_holidays
#
#
# def model_react_pattern(prompt):
#     prompt = f"""
#     Thought:跟据输入的问题,输入的问题，请给出一个最合适的问题，给出对应的思考
#     Action:根据思考,调用工具，给出对应的工具调用结果
#     Action Input:得到输出的结果
#
#     {question}
#     """
#
#
# def call_llm(prompt):
#     res = client.chat.completions.create(
#         model="qwen-plus",
#         messages=[
#             {"role": "user", "content": prompt}
#         ]
#     )
#     return res.choices[0].message.content
#
#
# if __name__ == '__main__':
#     question = input('请输入问题:')  # "2026年的5月有哪几天是节假日"
#     print(call_llm(question))


# 练习,文本分类
# from openai import OpenAI
#
#
# # 初始化提示词
# def init_prompt():
#     examples = {
#         '新闻报道': '今日，股市经历了一轮震荡，受到宏观经济数据和全球贸易紧张局势的影响。投资者密切关注美联储可能的政策调整，以适应市场的不确定性。',
#         '财务报告': '本公司年度财务报告显示，去年公司实现了稳步增长的盈利，同时资产负债表呈现强劲的状况。经济环境的稳定和管理层的有效战略执行为公司的健康发展奠定了基础。',
#         '公司公告': '本公司高兴地宣布成功完成最新一轮并购交易，收购了一家在人工智能领域领先的公司。这一战略举措将有助于扩大我们的业务领域，提高市场竞争力',
#         '分析师报告': '最新的行业分析报告指出，科技公司的创新将成为未来增长的主要推动力。云计算、人工智能和数字化转型被认为是引领行业发展的关键因素，投资者应关注这些趋势'
#     }
#     # 准备提示词:
#     prompt = f"""
#     你是一名专业的文本分类模型，你需要根据输入的文本，优先判断输入的文本是否属于以下四种类别:{list(examples)},如果没有合适的,请你总结后根据{list(examples)}的格式给出最合适的类别。
#     """
#     history_messages = [
#         {"role": "system", "content": prompt}
#     ]
#     # 系统提示词拼接小样本提示词
#     for k, v in examples.items():
#         history_messages.append({"role": "user", "content": v})
#         history_messages.append({"role": "assistant", "content": k})
#     return history_messages
#
#
# # 2.调用大模型
# llm = OpenAI(api_key="sk-f5d3982f6b0346a09641f6f2dd8768fa",
#              base_url="https://dashscope.aliyuncs.com/compatible-mode/v1"
#              )
#
#
# # 定义api接口
# def call_llm(texts):
#     for text in texts:
#         res = llm.chat.completions.create(
#             model="qwen-plus",
#             messages=init_prompt() + [
#                 {"role": "user", "content": text}
#             ]
#         )
#         result = res.choices[0].message.content
#         print(f'{text}的分类结果是:{result}')
#
#
# if __name__ == '__main__':
#     prompt = init_prompt()
#     texts = [
#         "今日，央行发布宣布降低利率，以刺激经济增长。这一降息举措将影响贷款利率，并在未来几个季度内对金融市场产生影响。",
#         "ABC公司今日发布公告称，已成功完成对XYZ公司股权的收购交易。本次交易是ABC公司在扩大业务范围、加强市场竞争力方面的重要举措。据悉，此次收购将进一步巩固ABC公司在行业中的地位，并为未来业务发展提供更广阔的发展空间。详情请见公司官方网站公告栏",
#         "公司资产负债表显示，公司偿债能力强劲，现金流充足，为未来投资和扩张提供了坚实的财务基础。",
#         "最新的分析报告指出，可再生能源行业预计将在未来几年经历持续增长，投资者应该关注这一领域的投资机会", ]
#     call_llm(texts)
#
#
#
# 练习,文本分类
# from openai import OpenAI
#
#
# # 初始化提示词
# def init_prompt():
#     examples = [
#         {
#             'content': '2023-01-10，股市震荡。股票古哥-D[EOOE]美股今日开盘价100美元，一度飙升至105美元，随后回落至98美元，最终以102美元收盘，成交量达到520000。',
#             'answers': {
#                 '日期': ['2023-01-10'],
#                 '股票名称': ['古哥-D[EOOE]美股'],
#                 '开盘价': ['100美元'],
#                 '收盘价': ['102美元'],
#                 '成交量': ['520000'],
#             }
#         }
#     ]
#     schema = {'金融': ['日期', '股票名称', '开盘价', '收盘价', '成交量']}
#     # 准备提示词:
#     prompt = f"""
#     你是一名专业的信息抽取系统，你需要根据提供的文本内容，严格抽取出以下信息：{schema['金融']}!不要胡编乱造!"""
#     history_messages = [
#         {"role": "system", "content": prompt}
#     ]
#     # 系统提示词拼接小样本提示词
#     for example in examples:
#         history_messages.append({"role": "user", "content": example['content']})
#         history_messages.append({"role": "assistant", "content": json.dumps(example['answers'], ensure_ascii=False)})
#     return history_messages
#
#
# # 2.调用大模型
# llm = OpenAI(api_key="sk-f5d3982f6b0346a09641f6f2dd8768fa",
#              base_url="https://dashscope.aliyuncs.com/compatible-mode/v1"
#              )
#
#
# # 定义api接口
# def call_llm(texts):
#     for text in texts:
#         res = llm.chat.completions.create(
#             model="qwen-plus",
#             messages=init_prompt() + [
#                 {"role": "user", "content": text}
#             ]
#         )
#         result = res.choices[0].message.content
#         print(f'{text}的分类结果是:{result}')
#
#
# if __name__ == '__main__':
#     texts = [
#         '2025-02-15，寓意吉祥的节日，股票佰笃[BD]美股开盘价10美元，虽然经历了波动，但最终以13美元收盘，成交量微幅增加至460,000，投资者情绪较为平稳。',
#         '2025-04-05，市场迎来轻松氛围，股票盘古(0021)开盘价23元，尽管经历了波动，但最终以26美元收盘，成交量缩小至310,000，投资者保持观望态度。'
#     ]
#     call_llm(texts)


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
