from fastapi import FastAPI, Path, Query,HTTPException
from pydantic import BaseModel,Field
from starlette.responses import HTMLResponse, FileResponse

#创建 FastAPI实例
app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}


# 访问 /hello 响应结果 msg：你好
@app.get("/hello")
async def say_hello():
    return {"message":"hello"}

#路径参数 - 类型注解 Path
#Path常用参数：gt/gt lt/le description min_length/max_length
@app.get("/book/{id}")
async def get_book(id:int = Path(...,gt=0,lt=101,description="书籍id，取值1-100")):
    return {"id":id,"message":"book"}

#查询参数
@app.get("/news/news_list")
async def get_news_list(
        skip:int=Query(0,description="跳过的记录数",lt=100),
        limit:int=Query(10,description="返回的记录数")):
    return {"skip":skip,"limit":limit}

#请求体参数
#Field类型注解常用参数：gt/ge lt/le default description min_length/max_length
class User(BaseModel):
    username: str=Field(default="张三",min_length=1,max_length=20,description="用户名1-20")
    password: str=Field(default="123",min_length=8,max_length=20,description="密码默认123")

@app.post("/user")
async def create_user(user: User):
    return user

#响应类型设置方式

#1.装饰器中指定响应类
#场景：固定返回类型（HTML，纯文本等）
#response_class：定义返回响应的类型
@app.get("html",response_class=HTMLResponse)
async def get_html():
    return "<h1>Hello World</h1>"

#2.返回响应对象
#场景：文件下载，图片，流式响应
@app.get("file")
async def get_file():
    file_path = "./files/1.jpeg"
    return FileResponse(file_path)


#自定义响应数据格式
#response_model是路径操作装饰器的关键参数，它通过一个Pydantic模型来严格定义和约束API端点的输出格式
class News(BaseModel):
    id: int
    title: str
    content: str

#response_model：定义返回数据的结构
@app.get("/news/{id}",response_model=News)
async def get_news(id:int):
    return {
        "id":id,
        "title":f"这是第{id}本书",
        "content":"这是一本好书"
    }

#异常处理：应使用fastapi.HTTPException来中断正常处理流程，并返回标准错误响应
@app.get("/news/{id}")
async def get_news(id:int):
    id_list=[1,2,3,4,5,6]
    if id not in id_list:
        raise HTTPException(status_code=404,detail="当前id不存在")
    return {"id":id}