import uvicorn
from blueprint.client import app

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
    #почему-то при работе с докером будет только так