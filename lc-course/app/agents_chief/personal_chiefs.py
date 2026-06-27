from dotenv import load_dotenv
from langchain.chat_models import init_chat_model
from langchain_tavily import TavilySearch
from langchain.agents import create_agent
import os

#加载环境变量
load_dotenv()

#初始化模型
model=init_chat_model(
    model="qwen3.5-flash",
    model_provider="openai",
    base_url=os.getenv("DASHSCOPE_BASE_URL"),
    api_key=os.getenv("DASHSCOPE_API_KEY")
)

#Web搜索工具，使用tavily作为Web搜索工具
web_search=TavilySearch(
    max_results=5,
    topic="general"
)

#编写系统提示词
system_prompt="""
你是一个私人厨师，收到用户提供的食材照片或清单后，请按照以下流程操作：
1.识别和评估食材:若用户提供照片，首先辨识所有可见食材。基于食材的外观状态，评估其新鲜度与可用量，整理出一份“当前可用食材清单”
2.智能食谱检索:优先调用 web_search 工具，以“可用食材清单”为核心关键词，查找可行菜谱。
3.多维度评估与排序;从营养价值和制作难度两个维度对检索到的候选食谱进行量化打分，并根据得分排序，制作简单且营养丰富的排名靠前。
4.结构化方案输出;把排序后的食谱整理为一份结构清晰的建议报告，要包含食谱信息、得分、推荐理由、食谱的参考图片，帮助用户快速做出决策。

请严格按照流程，优先调用 web_search 工具搜索食谱，搜索不到的情况下才能自己发挥。
"""

#创建agent
agent=create_agent(
    system_prompt=system_prompt,
    model=model,
    tools=[web_search]
)

# 注意：
# LangGraph会自动托管Agent的记忆，因此代码中不需要自己添加checkpointer
# LangGraph自带Restful的API接口，我们只要定义好Agent就可以