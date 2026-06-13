from idlelib.query import Query
from fastapi import FastAPI
from fastapi.params import Depends

app=FastAPI()

#依赖入住：抽取可复用的组件，实现代码复用，解耦且可轻松替换依赖性进行测试


#分页参数逻辑共用：新闻列表和用户列表
#1.依赖项
async def common_parameters(
        skip:int=Query(0,ge=0),
        limit:int=Query(10,le=60)
):
    return {"skip":skip,"limit":limit}

#Depends：声明依赖注入
@app.get("/book")
async def get_book(commons=Depends(common_parameters)):
    return commons


