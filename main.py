from fastapi import FastAPI, Query, UploadFile, File
import collections, shutil
from typing import List

app = FastAPI()

@app.post('/filter')
def post_word(request: List[str] = Query([])):
    dup_reqeust = [item for item, count in collections.Counter(request).items() if count > 1]
    r1 = [x.lower() for x in request]
    r2 = [x.lower() for x in dup_reqeust]
    res = list(set(r1) ^ set(r2))
    return res

@app.post("/upload/<file_name>")
async def Data_aggregation(file: List[UploadFile] = File(...)):
    for ing in file:
        with open(f'{ing.filename}', 'wb') as buffer:
            shutil.copyfileobj(ing.file, buffer)
    return {"file_name": "good"}