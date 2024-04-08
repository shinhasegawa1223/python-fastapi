from fastapi import FastAPI
from routers import item

# routerを使用したお作法
app = FastAPI()
app.include_router(item.router)
# ++++

if __name__ == "__main__":
    import uvicorn
    
    #  uvicorn main:app --reload --host 0.0.0.0 --port 8081
    uvicorn.run(app, host="127.0.0.1", port=8800)

 