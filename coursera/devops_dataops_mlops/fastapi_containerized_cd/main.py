from fastapi import FastAPI
import uvicorn


app = FastAPI()


@app.get('/')
async def root():
    return {'message': 'Hello, Buddy'}


@app.get('/add/{n1}/{n2}')
async def add(n1: int, n2: int):
    'Add two numbers'
    total = n1 + n2
    return {'total': total}


if __name__ == '__main__':
    uvicorn.run(app, port=8080, host='0.0.0.0')
