from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from fastapi.exceptions import HTTPException
import uvicorn

from ini_load import ini_load
from core import handler
from models.models import RequestModel, RespModel


app = FastAPI()
origins = ["*"]


app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)


ini_load()



@app.get('/ping')
def ping():
    return 'pong'



@app.post('/match_country', response_model=RespModel)
async def matches(baseParam:RequestModel):
    try:
        return JSONResponse(handler(baseParam.iso, baseParam.countries))
    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e))


if __name__ == '__main__':
    uvicorn.run(app, host="0.0.0.0", port=8000)
