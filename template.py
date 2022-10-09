file_env = '''HOST = localhost
PORT = 8000
DATABASE_NAME = mongodb
DATABASE_HOST = localhost
DATABASE_PORT = 27017'''


file_py_env = '''from pydantic import BaseSettings


class Enviroment(BaseSettings):

    HOST: str
    PORT: int
    DATABASE_NAME: str
    DATABASE_HOST: str
    DATABASE_PORT: str


env = Enviroment(_env_file ='.env')
'''

file_main = '''import uvicorn
from fastapi import FastAPI
from env import env

app = FastAPI()

@app.get('/',tags=['Hello'])
async def hello_world():
    return {'message':'hello world!'}


if __name__ == "__main__":
    uvicorn.run(
        'main:app',
        host= env.HOST,
        port= env.PORT,
        reload= True
    )
'''

database = '''from motor.motor_asyncio import AsyncIOMotorClient


MONGO_DETAIL = 'mongodb://localhost:27017/'
client = AsyncIOMotorClient(MONGO_DETAIL)
create_database = client.example
collection = create_database.get_collection('exaple_mongodb')

async def example():
    data = {'example':'connect to mongodb'}
    await collection.insert_one(data)
    return
'''
txt_file ='''anyio==3.6.1
click==8.1.3
colorama==0.4.5
fastapi==0.85.0
h11==0.14.0
idna==3.4
motor==3.0.0
pydantic==1.10.2
pymongo==4.2.0
python-dotenv==0.21.0
sniffio==1.3.0
starlette==0.20.4
typing_extensions==4.4.0
uvicorn==0.18.3
'''
gitignore ='''.env
venv
__pycache__
'''